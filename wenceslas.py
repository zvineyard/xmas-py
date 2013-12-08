import os
import time



os.system("mpg123 -q wenceslas.mp3 &")
time.sleep(0.6)

os.system("aplaymidi --port 14 wenceslas.mid")


