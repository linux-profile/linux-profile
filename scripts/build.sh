#!/bin/sh

chmod +x linux_profile.py

cp linux_profile.py linux_profile
mkdir -p ~/linuxp

cp -r core/ ~/linuxp/ 
cp linux_profile ~/linuxp/linux_profile
