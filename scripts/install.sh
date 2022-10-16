#!/bin/sh

echo "1 - Installing dependencies"
sudo apt install curl git

echo "2 - Download Github Repository"
sudo git clone https://github.com/MyLinuxProfile/linux-profile.git /opt/linuxp/temp --branch tests

echo "3 - Creating project structure"
sudo mv /opt/linuxp/temp/linux_profile /opt/linuxp/linux_profile
sudo mv /opt/linuxp/temp/linuxp.py /opt/linuxp/linuxp

echo "4 - Creating executable"
sudo chmod +x /opt/linuxp/linuxp
sudo rm -r /opt/linuxp/temp/

echo "5 - Creating new line in '.bashrc' file with project configuration."
echo '' >> ~/.bashrc
echo "# LinuxP" >> ~/.bashrc
echo 'PATH=$PATH":/opt/linuxp"' >> ~/.bashrc
echo '' >> ~/.bashrc

echo "6 - Exporting project configuration."
export PATH=$PATH":/opt/linuxp"
