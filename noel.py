import os
import time



os.system("mpg123 -q nowell.mp3 &")
time.sleep(0.7)

os.system("aplaymidi --port 14 nowell.mid")


