#!/bin/bash

if [ -d "/opt/linuxp" ]; then
    sudo rm -r "/opt/linuxp"
fi

if [ -d "/tmp/linuxp" ]; then
    sudo rm -r "/tmp/linuxp"
fi

if [ -d "$HOME/.config/linuxp" ]; then
    sudo rm -r "$HOME/.config/linuxp"
fi
