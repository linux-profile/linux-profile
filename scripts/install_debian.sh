#!/bin/bash

APP_TEMP=$LINUXP_PATH/temp
URL=https://github.com/MyLinuxProfile/linux-profile.git


update_linux() {
    echo "- Update linux"
    sudo apt update -y > /dev/null 2>&1

}

install_dependencies() {
    echo "- Installing dependencies [Git]"
    sudo apt install git -y > /dev/null 2>&1

}

clone_repository() {
    echo "- Cloning Repository"

    if [ -d "$APP_TEMP" ]; then
        sudo rm -r $APP_TEMP    
    fi

    sudo git clone $URL $APP_TEMP --branch master > /dev/null 2>&1

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
