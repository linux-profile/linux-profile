#!/bin/sh

chmod +x linux_profile.py

cp linux_profile.py linux_profile
mkdir -p ~/linux_basic

cp -r core/ ~/linux_basic/ 
cp linux_profile ~/linux_basic/linux_profile
echo 'export PATH=$PATH":$HOME/linux_basic"' >> ~/.profile
