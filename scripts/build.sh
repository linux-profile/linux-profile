#!/bin/sh

chmod +x linux_profile.py

cp ./linux_profile.py ./linuxp
mkdir -p ~/linuxp

cp -r ./core/ ~/linuxp/ 
cp ./linux_profile ~/linuxp/linux_profile
