import os
import sys

PREFIX_PATH = "/home/jake/workspace/HWE/mp3/"
JOIN_FILE_LIST_PATH = "temp_video_join.txt"

if(len(sys.argv) < 5):
    print("1st argument(necessary): Put Color (e.g. Blue1)")
    print("2nd argument(necessary): Put Chapter (e.g. 1)")
    print("3rd argument(necessary): Put The number of output mp3 files (e.g. 21)")
    print("4th argument(necessary): Put repetation number (e.g. 3)")
    exit(1)

if not sys.argv[2].isdecimal():
    print("Put chapter number correctly")
    exit(1)

if not sys.argv[3].isdecimal():
    print("Put The number of output mp3 files correctly")
    exit(1)

if not sys.argv[4].isdecimal():
    print("Put repetation number correctly")
    exit(1)

f = open(JOIN_FILE_LIST_PATH, 'w')
for i in range(0, int(sys.argv[3])):
    for _ in range(0, int(sys.argv[4])):
        f.write("file \'" + PREFIX_PATH + sys.argv[1] + "/" + sys.argv[2] +
                "/" + sys.argv[1] + sys.argv[2] + "_output" + str(i + 1) + ".mp3\'\n")
        f.write("file \'" + PREFIX_PATH + "one_and_half_sec_empty.mp3\'\n")
    f.write("file \'" + PREFIX_PATH + "one_and_half_sec_empty.mp3\'\n")

f.close()
print("ffmpeg -f concat -safe 0 -i ./" + JOIN_FILE_LIST_PATH +
      " -c copy " + PREFIX_PATH + "Output_Join/" + sys.argv[1] + sys.argv[2] + ".mp3")
os.system("ffmpeg -f concat -safe 0 -i ./" + JOIN_FILE_LIST_PATH +
          " -c copy " + PREFIX_PATH + "Output_Join/" + sys.argv[1] + sys.argv[2] + ".mp3")
