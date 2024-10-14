#!/bin/bash

# Get the current veriosn from command line

if [ -z "$1" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

# remove v from version
version=$(echo $1 | sed 's/v//')

echo "Setting version to $version"

# Set the "image: simple2b/svarog-app:latest" with "image: simple2b/svarog-app:$1" in compose.yml
sed -i "s|simple2b/svarog-app:.*|simple2b/svarog-app:$version|g" compose.yaml # this is for linux, won't work on mac

