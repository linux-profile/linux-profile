#!/bin/sh

BEGIN='\033[94m\033[1m'
END='\033[0m'

echo "$BEGIN 1 -$END Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master

echo "$BEGIN 2 -$END Creating new line in '.bashrc' file with project configuration."
echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

echo "$BEGIN 3 -$END Exporting project configuration."
export PATH=$PATH":$HOME/linuxp"
