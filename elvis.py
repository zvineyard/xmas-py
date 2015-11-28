import os
import time

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/audio/elvis.mid &")

time.sleep(8.05)

os.system("mpg123 /home/pi/pi-lightorgan-read-only/audio/elvis.mp3 & > /dev/null")
