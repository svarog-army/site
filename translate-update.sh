#!/bin/bash

# set current directory of the script
cd "$(dirname "$0")"

# Extract messages
pybabel extract -F babel.cfg -o messages.pot .
# Update translations
pybabel update -i messages.pot -d translations
