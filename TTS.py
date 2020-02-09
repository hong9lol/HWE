import sys
import re
from google.cloud import texttospeech

# Set google TTS config
# Instantiates a client
client = texttospeech.TextToSpeechClient()
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)


# Parse Eng text from a input file
PREFIX_PATH = "/home/jake/workspace/HWE/"
input_text_list = []

if len(sys.argv) == 1:          # 옵션 없으면 도움말 출력하고 종료
    print("Put the name of text(.txt) file")
    sys.exit(1)
try:
    f = open(PREFIX_PATH + "data/" + sys.argv[1] + ".txt", 'rt')
    try:
        input_text = ""
        for line in f:
            if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', line)):
                continue
            elif len(line) <= 1:
                input_text_list.append(input_text)
                input_text = ""
            else:
                input_text += line
    finally:
        f.close()
except IOError:
    print("Can not open the file(", PREFIX_PATH +
          "data/" + sys.argv[1]+".txt", ")")
except:
    print("unexpected expection occur")

# Extract mp3 files
for idx, input_text in enumerate(input_text_list):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=input_text)
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    # The response's audio_content is binary.
    with open(PREFIX_PATH + "mp3/Output_TTS/" + sys.argv[1] + "_output" + str(idx+1) + ".mp3", 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print("Complete extract mp3 files(", idx +
              1, "/", len(input_text_list), ")")

print("Done")
