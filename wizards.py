import os
import time

os.system("timidity /home/pi/pi-lightorgan-read-only/transient.mid &")
time.sleep(1.8)

os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/transient.mid")