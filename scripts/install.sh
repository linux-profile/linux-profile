#!/bin/sh

git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master

echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc
