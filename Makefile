install:
	make install-screenshot
	make install-deps
	make install-sounds

install-screenshot:
	sudo pacman -S --noconfirm maim
	sudo ln -fs ${HOME}/.config/qtile/.init-scripts/screenshot.sh /usr/bin/screenshot
	sudo ln -fs ${HOME}/.config/qtile/.init-scripts/screenshot-all.sh /usr/bin/screenshot-all

install-deps:
	sudo pacman -S --noconfirm rofi git-delta qtile kitty alsa-utils python-iwlib python-psutil xcb-util-cursor xclip xorg-xev yay

intsall-sounds:
	sudo pacman -S --noconfirm  pavucontrol bluez bluez-utils blueman pipewire pipewire-audio pipewire-pulse
