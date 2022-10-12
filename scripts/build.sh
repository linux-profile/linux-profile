#!/bin/sh

chmod +x setup.py

cp ./setup.py ./linuxp
mkdir -p ~/linuxp

cp -r ./linux_profile/ ~/linuxp/ 
cp ./linuxp ~/linuxp/linuxp
