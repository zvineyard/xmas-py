import os
import time

os.system("aplaymidi --port 14 white_christmas.mid &")
time.sleep(4.1)
os.system("timidity white_christmas.mid")
