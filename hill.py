import os
import time




os.system("mpg123 hill.mp3 & ")

time.sleep(1.3)


os.system("aplaymidi --port 14 hill.mid")





