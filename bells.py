import os
import time

os.system("mpg123 -q /home/pi/pi-lightorgan-read-only/carol-of-the-bells.mp3 &")
time.sleep(0.55)

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/carol-of-the-bells.mid")