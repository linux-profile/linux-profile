#!/bin/sh

APP='/opt/linuxp'

echo "1 - Installing dependencies"
sudo apt update
sudo apt install git

echo "2 - Download Github Repository"
sudo git clone https://github.com/MyLinuxProfile/linux-profile.git $APP/temp --branch master

echo "3 - Creating project structure"
sudo rm -r $APP/linux_profile
sudo mv $APP/temp/linux_profile $APP/linux_profile
sudo mv $APP/temp/linuxp.py $APP/linuxp

echo "4 - Creating executable"
sudo chmod +x $APP/linuxp
sudo rm -r $APP/temp/

echo "5 - Creating new line in '.bashrc' file with project configuration."
echo '' >> ~/.bashrc
echo "# LinuxP" >> ~/.bashrc
echo 'PATH=$PATH":/opt/linuxp"' >> ~/.bashrc
echo '' >> ~/.bashrc

echo "6 - Exporting project configuration."
PATH=$PATH":/opt/linuxp"; export PATH
exec bash