#!/bin/bash

# set current directory of the script
cd "$(dirname "$0")"

# Compile messages
pybabel compile -d translations
