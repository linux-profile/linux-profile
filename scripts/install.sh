#!/bin/sh

echo "1 - Installing dependencies"
sudo apt install curl git python-setuptools

echo "2 - Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master

echo "3 - Creating new line in '.bashrc' file with project configuration."
echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

echo "4 - Exporting project configuration."
export PATH=$PATH":$HOME/linuxp"
