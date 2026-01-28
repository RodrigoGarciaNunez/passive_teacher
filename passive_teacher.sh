#!/bin/bash

TARGET_HOUR=18
TARGET_MIN=30

SELECTED_CHEATSHEET=$(python3 model/file_selector.py)
echo $SELECTED_CHEATSHEET 

while true; do
    CURRENT_HOUR=$(date +%H)
    CURRENT_MIN=$(date +%M)

    if [[ $CURRENT_HOUR -gt $TARGET_HOUR ]] || \
       [[ $CURRENT_HOUR -eq $TARGET_HOUR && $CURRENT_MIN -ge $TARGET_MIN ]]; then
        echo "Hora alcanzada, ejecutando programa..."
        python3 model/sender.py "$SELECTED_CHEATSHEET"
	break
    fi

    sleep 30
done
