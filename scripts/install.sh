#!/bin/bash
echo installing hyprland
cd ~
sudo pacman -S python3 wofi waybar hyprland kitty code hyprpaper hyprshot cron cronie git cargo pkg-config
sudo systemctl enable cronie

git clone https://github.com/Tobs2007/hyprlandDotfiles.git dotfiles
mkdir ~/.config/hypr
cp ~/dotfiles/hypr/redirect/hyprland.config ~/.config/hypr

# set dotfiles as config root
echo "[[ -f ~/dotfiles/scripts/.bash_profile ]] && source ~/dotfiles/scripts/.bash_profile" >> ~/.bash_profile
echo "[[ -f ~/dotfiles/scripts/.bashrc ]] && source ~/dotfiles/scripts/.bashrc" >> ~/.bashrc

# setup python venv for the waybar infos
python -m venv ~/dotfiles/.venv
source ~/dotfiles/.venv/bin/activate
pip install psutil

# install eww
cd ~
git clone https://github.com/elkowar/eww
cd eww
cargo build --release --no-default-features --features=wayland
chmod +x ./target/release/eww
echo "alias eww='~/eww/target/release/eww'" >> ~/.bashrc
