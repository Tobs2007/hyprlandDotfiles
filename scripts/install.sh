#!/bin/bash
echo installing hyprland
cd ~
wget -r https://tobsstuff.com/data/dotfiles
mkdir ~/.config/hypr
cd ~/.config/hypr
wget https://tobsstuff.com/data/dotfiles/hypr/redirect/hyprland.config

sudo pacman -S python3 wofi waybar hyprland kitty code hyprpaper hyprshot
echo export XDG_CONFIG_HOME=~/dotfiles/ > ~/.bashrc
python -m venv ~/dotfiles/.venv
source ~/dotfiles/.venv/bin/activate
pip install psutil
