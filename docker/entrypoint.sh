#!/bin/sh
set -e

cd /opt/cortex/analyzers/Crowdsec || exit
pip3 install -r requirements.txt

# Cortex entrypoint requires to be in the good path
cd /opt/cortex/ || exit
# Execute the Cortex application with any additional arguments
exec /opt/cortex/entrypoint "$@"