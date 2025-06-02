#!/bin/bash
cd ~/
export XDG_CONFIG_HOME=~/dotfiles/
pacman -S python3 wofi waybar
python -m venv .venv
source .venv/bin/activate
pip install psutil