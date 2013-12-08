import os
count = 0
while (count < 1000):

	# Turn on all the lights
	os.system("gpio write 0 1;gpio write 1 1;gpio write 2 1;gpio write 3 1;gpio write 4 1;gpio write 5 1;gpio write 6 1;gpio write 7 1;")

	# Set the volume
	os.system("amixer set PCM 90%")

	# Play a welcome message
	os.system("mpg123 welcome.mp3")

	# Reset Volume
	os.system("amixer set PCM 100%")

	# Turn off all the lights
	os.system("gpio write 0 0;gpio write 1 0;gpio write 2 0;gpio write 3 0;gpio write 4 0;gpio write 5 0;gpio write 6 0;gpio write 7 0;")

	# Play songs
	os.system("python coventry.py")

	os.system("amixer set PCM 90%")
	os.system("python wizards.py")

	os.system("amixer set PCM 100%")
	os.system("python bells.py")

	os.system("python noel.py")
	os.system("python wenceslas.py")