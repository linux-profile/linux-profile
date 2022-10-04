#!/bin/sh

echo "1 - Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master

echo "2 - Creating new line in '.bashrc' file with project configuration."
echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

echo "3 - Exporting project configuration."
export PATH=$PATH":$HOME/linuxp"
