
all:
	gcc lightorgan.c -lasound -lwiringPi -g -Wall -o lightorgan

install: all
	sudo cp lightorgan /usr/sbin
	sudo chmod 700 /usr/sbin/lightorgan
	sudo chown root /usr/sbin/lightorgan


