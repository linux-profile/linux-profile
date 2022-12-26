#!/bin/sh

APP='/opt/linuxp'

echo "1 - Installing dependencies"
pacman -Sy
pacman -S git

echo "2 - Download Github Repository"
git clone https://github.com/MyLinuxProfile/linux-profile.git $APP/temp --branch master

echo "3 - Creating project structure"
rm -r $APP/linux_profile
mv $APP/temp/linux_profile $APP/linux_profile
mv $APP/temp/linuxp.py $APP/linuxp

echo "4 - Creating executable"
chmod +x $APP/linuxp
rm -r $APP/temp/

echo "5 - Creating new line in '.bashrc' file with project configuration."
echo '' >> ~/.bashrc
echo "# LinuxP" >> ~/.bashrc
echo 'PATH=$PATH":/opt/linuxp"' >> ~/.bashrc
echo '' >> ~/.bashrc

echo "6 - Exporting project configuration."
PATH=$PATH":/opt/linuxp"; export PATH
exec bash