import os
import time



os.system("mpg123 -q /home/pi/pi-lightorgan-read-only/nowell.mp3 &")
time.sleep(0.7)

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/nowell.mid")


