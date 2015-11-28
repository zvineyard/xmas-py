import os
import time

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/audio/monsters.mid &")

time.sleep(1.5)

os.system("mpg123 /home/pi/pi-lightorgan-read-only/audio/monsters.mp3 & > /dev/null")
