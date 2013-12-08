import os
import time



os.system("mpg123 monsters.mp3 &")
time.sleep(0)

os.system("aplaymidi --port 14 monsters.mid")


