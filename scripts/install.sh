#!/bin/sh

# Download Github Repository.
git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master

# Creating new line in '.bashrc' file with project configuration.
echo 'export PATH=$PATH":$HOME/linuxp"' >> ~/.bashrc

# Exporting project configuration
export PATH=$PATH":$HOME/linuxp"
