#!/usr/bin/env bash

#set -eEo pipefail

echo "$(date) | INFO  | Configuring wasabi"
echo '[{ "username": "'${USER}'", "password": "'${PASS}'" }]' > accounts.json
cat accounts.json

# Check if ARGS variable is set
if [ -z "$ARGS" ]; then
  ARGS="--visible --lang it --geo IT"  # Default value if ARGS is not set
  echo "$(date) | WARN  | ARGS is not set, the default value will be " $ARGS
fi
    
echo "$(date) | INFO  | Starting wasabi"
python main.py ${ARGS}
            #--discord ${DISCORD_URL}
            #--telegram ${TELEGRAM_API_TOKEN} ${TELEGRAM_USERID}
