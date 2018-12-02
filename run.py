import os
import time

songs = {
	'as-with-gladness-men-of-old': 0.6,
	'away-in-a-manger': 0.6,
	'carol-of-the-bells': 0.55,
	'coventry-carol-keyboard': 0.6,
	#'cradled-in-a-manger-meanly-piano': 0.6,
	'deck-the-halls': 0.6,
	#'ding-dong-merrily-on-high': 0.6,
	#'gabriels-message-keyboard': 0.6,
	#'gaudete-rejoice': 0.6,
	'go-tell-it-on-the-mountain': 0.6,
	'god-rest-you-merry-gentlemen': 0.6,
	#'good-christian-men-rejoice': 0.6,
	'good-king-wenceslas': 0.6,
	'greensleeves': 0.6,
	'hark-the-herald-angels-sing': 0.6,
	#'i-saw-three-ships-tune-a-keyboard': 0.6,
	#'i-saw-three-ships-tune-b-keyboard': 0.6,
	#'il-est-ne-le-divin-enfant-keyboard': 0.6,
	#'in-the-bleak-midwinter': 0.6,
	'it-came-upon': 0.6,
	'jingle-bells-keyboard': 0.6,
	'joy-to-the-world': 0.6,
	#'mizerna-cicha-keyboard': 0.6,
	#'morning-has-broken': 0.6,
	'nowell': 0.7,
	#'o-christmas-tree': 0.6,
	'o-come-all-ye-faithful-keyboard': 0.6,
	'oh-little-town-of-bethlehem': 0.6,
	#'once-in-royal': 0.6,
	#'sans-day-carol-piano': 0.6,
	'silent-night': 0.6,
	'the-first-nowell': 0.6,
	#'the-holly-and-the-ivy': 0.6,
	#'the-huron-carol-piano': 0.6,
	#'the-wexford-carol-piano': 0.6,
	'we-three-kings-keyboard': 0.6,
	'wenceslas': 0.6,
	'while-shepherds-watched': 0.6
}

while True:

	# Turn all lights on
	os.system("sudo gpio write 0 1;sudo gpio write 1 1;sudo gpio write 2 1;sudo gpio write 3 1;sudo gpio write 4 1;sudo gpio write 5 1;sudo gpio write 6 1;sudo gpio write 7 1;")

	# ADjust volume and play into
	#os.system("sudo amixer set PCM 90%")
	#os.system("mpg123 /home/pi/pi-lightorgan-read-only/audio/vineyard.mp3 > /dev/null")

	os.system("sudo amixer set PCM 100%")

	# Turn all lights off
	os.system("sudo gpio write 0 0;sudo gpio write 1 0;sudo gpio write 2 0;sudo gpio write 3 0;sudo gpio write 4 0;sudo gpio write 5 0;sudo gpio write 6 0;sudo gpio write 7 0;")
	
	# Play songs for show
	for name, delay in songs.iteritems():
		os.system("mpg123 -q /home/pi/pi-lightorgan-read-only/audio/%s.mp3 &" % name)
		time.sleep(delay)
		os.system("aplaymidi --port 14 /home/pi/pi-lightorgan-read-only/audio/%s.mid" % name)



