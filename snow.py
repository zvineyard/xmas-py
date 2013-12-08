import os
import time



os.system("timidity let_it_snow.mid &")
time.sleep(0)

os.system("aplaymidi --port 14 let_it_snow.mid")


