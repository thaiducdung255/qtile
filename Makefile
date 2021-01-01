arch-install:
	sudo pacman -S rofi qtile termite xmessage alsa-utils python-iwlib python-psutil xcb-util-cursor xclip maim nitrogen
	sudo ln -s $HOME/.config/qtile/.init-scripts/screenshot.sh /usr/bin/screenshot
	sudo ln -s $HOME/.config/qtile/.init-scripts/screenshot-all.sh /usr/bin/screenshot-all
