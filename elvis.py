import os
import time


os.system("aplaymidi --port 14 blue.mid &")

time.sleep(3)

os.system("mpg123 elvis.mp3")





