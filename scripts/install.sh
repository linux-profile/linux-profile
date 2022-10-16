#!/bin/sh

echo "1 - Installing dependencies"
sudo apt install curl git

echo "2 - Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile.git ~/opt/linuxp/temp --branch pypi

echo "3 - Creating project structure"
mv ~/linuxp/temp/linux_profile ~/linuxp/linux_profile
mv ~/linuxp/temp/linuxp.py ~/linuxp/linuxp

echo "4 - Creating executable"
chmod +x ~/linuxp/linuxp
sudo rm -r ~/linuxp/temp/

echo "5 - Creating new line in '.bashrc' file with project configuration."
echo "# LinuxP" >> ~/.bashrc
echo 'PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

echo "6 - Exporting project configuration."
export PATH=$PATH":$HOME/linuxp"
