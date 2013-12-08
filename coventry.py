import os
import time



os.system("mpg123 coventry-carol.mp3 & > /dev/null")
time.sleep(0.6)

os.system("aplaymidi --port 14 coventry-carol.mid > /dev/null")


