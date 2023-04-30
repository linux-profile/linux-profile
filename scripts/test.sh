#!/bin/bash

LINUXP_PATH="/opt/linuxp"
APP_TEMP=$LINUXP_PATH/temp


copy_repository() {
    echo "- Copy Repository"

    if [ -d "$LINUXP_PATH" ]; then
        sudo rm -r $LINUXP_PATH
    fi

    if [ -d "$APP_TEMP" ]; then
        sudo rm -r $APP_TEMP
    fi

    sudo mkdir $LINUXP_PATH
    sudo mkdir $APP_TEMP
    sudo cp -r linux_profile/ $APP_TEMP/linux_profile
    sudo cp linuxp.py $APP_TEMP/linuxp.py

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
    copy_repository
    create_structure
    create_executable
}

main
