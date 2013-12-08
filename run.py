import os
count = 0
while (count < 1000):
	os.system("gpio write 0 1;gpio write 1 1;gpio write 2 1;gpio write 3 1;gpio write 4 1;gpio write 5 1;gpio write 6 1;gpio write 7 1;")

	os.system("amixer set PCM 90%")
	os.system("mpg123 vineyard2.mp3 > /dev/null")


	os.system("amixer set PCM 100%")

	os.system("gpio write 0 0;gpio write 1 0;gpio write 2 0;gpio write 3 0;gpio write 4 0;gpio write 5 0;gpio write 6 0;gpio write 7 0;")
	os.system("python coventry.py")
	os.system("amixer set PCM 90%")
	os.system("python wizards.py")
	os.system("amixer set PCM 100%")
	os.system("python bells.py")
	os.system("python noel.py")
	os.system("python wenceslas.py")
