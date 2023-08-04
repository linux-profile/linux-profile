#!/bin/bash

##################################################################
#Script Name    : uninstall.sh
#Description    : Uninstall Script
#Creation Date  : 2022-12-31
#Author         : Fernando Celmer
#Email          : email@fernandocelmer.com
##################################################################

remove_opt() {
    if [ -d "/opt/linuxp" ]; then
        echo "▶ Deleted -> /opt/linuxp" 
        sudo rm -r "/opt/linuxp"
    fi
}

remove_tmp() {
    if [ -d "/tmp/linuxp" ]; then
        echo "▶ Deleted -> /tmp/linuxp" 
        sudo rm -r "/tmp/linuxp"
    fi
}

remove_config() {
    echo -n "Delete configuration files? [y/n]: "
    read -r ans

    if [[ $ans == "y" ]]; then
        if [ -d "$HOME/.config/linuxp" ]; then
            echo "▶ Deleted -> $HOME/.config/linuxp" 
            sudo rm -r "$HOME/.config/linuxp"
        fi
    fi
}

main() {
    remove_opt
    remove_tmp
    remove_config
}

main
