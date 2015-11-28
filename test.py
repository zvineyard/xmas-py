import os
os.system("sudo gpio write 0 1;sudo gpio write 1 1;sudo gpio write 2 1;sudo gpio write 3 1;sudo gpio write 4 1;sudo gpio write 5 1;sudo gpio write 6 1;sudo gpio write 7 1;")

os.system("sudo amixer set PCM 90%")
os.system("mpg123 /home/pi/pi-lightorgan-read-only/vineyard2.mp3 > /dev/null")
