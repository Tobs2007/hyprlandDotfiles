#!/bin/bash
cd ~/dotfiles
export XDG_CONFIG_HOME=~/dotfiles/
pacman -S python3 wofi waybar
python -m venv ~/dotfiles/.venv
source ~/dotfiles/.venv/bin/activate
pip install psutil
