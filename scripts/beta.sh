#!/bin/bash

if  [ ! -n "$1" ]
then 
	branch='develop'
else 
	branch=$1
fi

DISTRO=$(cat /etc/*-release | grep -w ID | cut -d= -f2 | tr -d '"')

LINUXP_PATH="/opt/linuxp"
APP_TEMP=$LINUXP_PATH/temp
URL=https://github.com/MyLinuxProfile/linux-profile.git


update_linux() {

    if [[ $DISTRO == "ubuntu" ]]; then
        echo "- Update $DISTRO"
        sudo apt update -y > /dev/null 2>&1
    fi

    if [[ $DISTRO == "arch" ]]; then
        echo "- Update $DISTRO"
        sudo pacman -Sy
    fi

}

install_dependencies() {

    if [[ $DISTRO == "ubuntu" ]]; then
        echo "- Installing dependencies [Git]"
        sudo apt install git -y > /dev/null 2>&1
    fi

    if [[ $DISTRO == "arch" ]]; then
        echo "- Installing dependencies [Git]"
        sudo pacman -S git
    fi

}

clone_repository() {
    echo "- Cloning Repository --branch $branch"

    if [ -d "$APP_TEMP" ]; then
        sudo rm -r $APP_TEMP    
    fi

    sudo git clone $URL $APP_TEMP --branch $branch > /dev/null 2>&1

}

create_structure() {
    echo "- Creating project structure"

    if [ -d "$LINUXP_PATH/linux_profile" ]; then
        sudo rm -r $LINUXP_PATH/linux_profile
    fi

    sudo mv $APP_TEMP/linux_profile $LINUXP_PATH/linux_profile
    sudo mv $APP_TEMP/linuxp.py $LINUXP_PATH/linuxp
}

create_executable() {
    echo "- Creating executable"

    sudo chmod +x $LINUXP_PATH/linuxp

    if [ -d "$APP_TEMP" ]; then
        sudo rm -r $APP_TEMP
    fi
    
}

main() {
    update_linux
    install_dependencies
    clone_repository
    create_structure
    create_executable
}


main

echo "- Creating configuration in .bashrc file"
echo 'PATH=$PATH":/opt/linuxp"' >> ~/.bashrc

echo "- Exporting path"
PATH=$PATH":$LINUXP_PATH"; export PATH

exec $SHELL
