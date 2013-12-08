import os
import time



os.system("timidity transient.mid &")
time.sleep(1.8)

os.system("aplaymidi --port 14 transient.mid")


