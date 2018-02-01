import sys
import time
import os

time.sleep(int(sys.argv[1]))
os.system("killall ssh")
os.system("echo -e 'student123\ngeorgerocks\ngeorgerocks' | passwd")

