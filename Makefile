arch-install:
	sudo pacman -S --noconfirm rofi git-delta qtile kitty alsa-utils python-iwlib python-psutil xcb-util-cursor xclip maim
	sudo ln -fs ${HOME}/.config/qtile/.init-scripts/screenshot.sh /usr/bin/screenshot
	sudo ln -fs ${HOME}/.config/qtile/.init-scripts/screenshot-all.sh /usr/bin/screenshot-all
