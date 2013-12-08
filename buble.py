import os
import time



os.system("mpg123 buble.mp3 &")
time.sleep(0.3)

os.system("aplaymidi --port 14 buble.mid")


