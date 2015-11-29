## Getting Started

Step 1: Follow the setup guide on [zacvineyard.com](http://zacvineyard.com/blog/2013/11/building-a-christmas-music-light-show-with-a-raspberry-pi).

Step 2: Start lightorgan with sudo:

	sudo ./lightorgan

Step 3: Run any of the Python scripts to hear audio and see lights

	python bells.py

To stop all lights and audio, you can kill the processes:

	killall aplaymidi && killall mpg123

### Getting the audio to sync up

Make sure you adjust the `time.sleep(0.6)` in each Python script to get mp3 and midi audio to sync up on your device. You may also need to invert which file starts playing first, the midi or the mp3.

Mp3 and Midi files were downloaded for free from this website: [http://www.mfiles.co.uk/christmas-music-and-carols.htm](http://www.mfiles.co.uk/christmas-music-and-carols.htmhttp://example.net/). The monsters.py file is for ["Scary Monsters And Nice Sprites"](https://www.youtube.com/watch?v=WSeNSzJ2-Jw) by SKRILLEX. The elvis.py is for ["Blue Christmas"](https://www.youtube.com/watch?v=6d2RfblImA4) by Elvis. You'll need to download those audio files on your own.