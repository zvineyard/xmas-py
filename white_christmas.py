import os
import time

os.system("aplaymidi --port 14 bc_white_christmas.mid &")
time.sleep(4.7)
os.system("mpg123 white_christmas.mp3")
