import os
count = 0

while (count < 1000):
	os.system("sudo gpio write 0 1;sudo gpio write 1 1;sudo gpio write 2 1;sudo gpio write 3 1;sudo gpio write 4 1;sudo gpio write 5 1;sudo gpio write 6 1;sudo gpio write 7 1;")

	os.system("sudo amixer set PCM 90%")
	os.system("mpg123 /home/pi/pi-lightorgan-read-only/vineyard2.mp3 > /dev/null")

	os.system("sudo amixer set PCM 100%")

	os.system("sudo gpio write 0 0;sudo gpio write 1 0;sudo gpio write 2 0;sudo gpio write 3 0;sudo gpio write 4 0;sudo gpio write 5 0;sudo gpio write 6 0;sudo gpio write 7 0;")
	os.system("python /home/pi/pi-lightorgan-read-only/coventry.py")
	os.system("sudo amixer set PCM 90%")
	os.system("python /home/pi/pi-lightorgan-read-only/wizards.py")
	os.system("sudo amixer set PCM 100%")
	os.system("python /home/pi/pi-lightorgan-read-only/bells.py")
	os.system("python /home/pi/pi-lightorgan-read-only/noel.py")
	os.system("python /home/pi/pi-lightorgan-read-only/wenceslas.py")