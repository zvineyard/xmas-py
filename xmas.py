import os
import time

os.system("aplaymidi --port 14 godresty.mid &")
time.sleep(1.5)
os.system("timidity godresty.mid")
