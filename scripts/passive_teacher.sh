#!/bin/bash

set -e  # se sale por si hay error

TARGET_HOUR=7
TARGET_MIN=30
SENT_TODAY=1
CONTACT_DIR=""

# -------------------------
# Parseo de argumentos
# -------------------------
while getopts ":d:" opt; do
    case "$opt" in
        d)
            CONTACT_DIR=$(python3 -m model.contact_dir_reader "$OPTARG")
            ;;
        *)
            echo "Uso: $0 -d <contact_dir>"
            exit 1
            ;;
    esac
done

# Validación
# if [[ -z "$CONTACT_DIR" ]]; then
#     echo "Error: falta el directorio de contactos (-d)"
#     exit 1
# fi

# -------------------------
# Selecciona de cheatsheet
# -------------------------
#SELECTED_CHEATSHEET=$(python3 -m model.file_selector)

# echo "Cheatsheet seleccionado: $SELECTED_CHEATSHEET"
# echo "Directorio de contactos: $CONTACT_DIR"

# -------------------------
# Loop principal
# -------------------------
while true; do
        CURRENT_HOUR=$(date +%H)
        CURRENT_MIN=$(date +%M)
        CURRENT_DAY=$(date +%D)

        echo "En espera..."
    if [[ "$SENT_TODAY" -eq 1 ]]; then
 
            
        if [[ "$CURRENT_HOUR" -gt "$TARGET_HOUR" ]] || \
           [[ "$CURRENT_HOUR" -eq "$TARGET_HOUR" && "$CURRENT_MIN" -ge "$TARGET_MIN" ]]; then

            echo "Hora alcanzada, seleccionando archivo..."
            SELECTED_CHEATSHEET=$(python3 -m model.file_selector)
            echo "Cheatsheet seleccionado: $SELECTED_CHEATSHEET"

    
            curl -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendDocument -F chat_id=-$TELEGRAM_CHANNEL_ID -F document=@$SELECTED_CHEATSHEET

            SENT_TODAY=0
            SENDING_DATE=$CURRENT_DAY
            rm *.pdf
            echo "Archivo enviado!"
        
        fi
    fi

    if [[ "$SENT_TODAY" -eq 0 ]] && \
       [[ "$SENDING_DATE" -ne "$CURRENT_DAY" ]]; then     

        echo "Nuevo día! Esperando a enviar..."
        SENT_TODAY=1
    
    fi

    sleep 30
done
