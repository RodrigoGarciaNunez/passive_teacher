#!/bin/bash

set -e  # aborta ante errores (opcional pero recomendado)

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
            CONTACT_DIR=$(python3 model/contact_dir_reader.py "$OPTARG")
            ;;
        *)
            echo "Uso: $0 -d <contact_dir>"
            exit 1
            ;;
    esac
done

# Validación
if [[ -z "$CONTACT_DIR" ]]; then
    echo "Error: falta el directorio de contactos (-d)"
    exit 1
fi

# -------------------------
# Selección de cheatsheet
# -------------------------
SELECTED_CHEATSHEET=$(python3 model/file_selector.py)

echo "Cheatsheet seleccionado: $SELECTED_CHEATSHEET"
echo "Directorio de contactos: $CONTACT_DIR"

# -------------------------
# Loop principal
# -------------------------
while true; do
    if [[ "$SENT_TODAY" -eq 1 ]]; then

        CURRENT_HOUR=$(date +%H)
        CURRENT_MIN=$(date +%M)

        if [[ "$CURRENT_HOUR" -gt "$TARGET_HOUR" ]] || \
           [[ "$CURRENT_HOUR" -eq "$TARGET_HOUR" && "$CURRENT_MIN" -ge "$TARGET_MIN" ]]; then

            echo "Hora alcanzada, ejecutando programa..."
            python3 model/sender.py "$SELECTED_CHEATSHEET" "$CONTACT_DIR"
            break
        fi
    fi

    sleep 30
done
