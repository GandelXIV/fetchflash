import sys
import os

if sys.argv[1] == "install":
	os.system("python3 /usr/lib/fetchflash/fetchflash.py {} {}".format(sys.argv[2],sys.argv[3]))
elif sys.argv[1] == "play":
	os.system("/usr/lib/fetchflash/flashplayer.linux {}".format(sys.argv[2]))
