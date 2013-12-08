import os
import time




os.system("mpg123 -q carol-of-the-bells.mp3 &")
time.sleep(0.55)

os.system("aplaymidi --port 14 carol-of-the-bells.mid")


