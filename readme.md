## Getting Started

Step 1: Follow the setup guide on [zacvineyard.com](http://zacvineyard.com/blog/2013/11/building-a-christmas-music-light-show-with-a-raspberry-pi).

Step 2: Compile lightorgan:

	make
	(optional: sudo make install)

Step 3: Start lightorgan with sudo:

	sudo ./lightorgan

Step 4: Run the Python script to hear audio and see lights

	python run.py

To stop all lights and audio, you can kill the processes:

	killall aplaymidi && killall mpg123

### Getting the audio to sync up

Make sure you adjust the time offset in run.py to get mp3 and midi audio to sync up on your device. You may also need to invert which file starts playing first, the midi or the mp3.

Mp3 and Midi files were downloaded for free from this website: [http://www.mfiles.co.uk/christmas-muarols.htm](http://www.mfiles.co.uk/christmas-music-and-carols.htmhttp://example.net/). 
