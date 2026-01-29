#!/bin/bash



if [[ -z $1 ]]; then
    echo Missing Contact dir
    exit 1
fi

TARGET_HOUR=18
TARGET_MIN=30
SENT_TODAY=1

SELECTED_CHEATSHEET=$(python3 model/file_selector.py)
echo $SELECTED_CHEATSHEET 

CONTACT_DIR=$1

#! imma fix this tommorrow
while getopts ":d" option; do
    CONTACT_DIR=$(python3 model/contact_dir_reader.py $CONTACT_DIR)
    echo $CONTACT_DIR
done 


while true; do

    if [[ $SENT_TODAY -eq 1 ]]; then
        
        CURRENT_HOUR=$(date +%H)
        CURRENT_MIN=$(date +%M)

        if [[ $CURRENT_HOUR -gt $TARGET_HOUR ]] || \
        [[ $CURRENT_HOUR -eq $TARGET_HOUR && $CURRENT_MIN -ge $TARGET_MIN ]]; then
            echo "Hora alcanzada, ejecutando programa..."
            (python3 model/sender.py $SELECTED_CHEATSHEET $CONTACT_DIR)
        break
        fi
    fi
    sleep 30
done
