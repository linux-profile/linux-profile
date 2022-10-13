#!/bin/sh

echo "1 - Installing dependencies"
sudo apt install curl git python-setuptools

echo "2 - Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile.git ~/linuxp/linux_profile --branch pypi

cp -r ./linux_profile ~/linuxp/linux_profile
cp ./setup_dev.py ~/linuxp/setup_dev.py

chmod +x ~/linuxp/setup_dev.py
mv ~/linuxp/setup_dev.py ~/linuxp/linuxp


echo "3 - Creating new line in '.bashrc' file with project configuration."
echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

echo "4 - Exporting project configuration."
export PATH=$PATH":$HOME/linuxp"
