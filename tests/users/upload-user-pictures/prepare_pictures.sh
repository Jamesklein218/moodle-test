#!/usr/bin/bash

# Script for preparing data for bulk upload user pictures
# First argument is the list of usernames on the Mount Orange School demo site
# Second argument is the output zip archive name

if [ ! -f "$1" ]; then
    echo "File $1 does not exist. Aborting"
    exit 1
fi

if [ -z "$2" ]; then
    echo "Output zip archive name not provided. Aborting"
    exit 1
fi

readarray -t usernames < "$1"

BASE_IMAGE="base-image.jpeg"
curl -s -o "$BASE_IMAGE" "https://images.pexels.com/photos/346529/pexels-photo-346529.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"

for username in "${usernames[@]}"; do
    cp "$BASE_IMAGE" "${username}.jpeg"
done

picture_names=("${usernames[@]/%/.jpeg}")

zip -q "$2" "${picture_names[@]}"

# Cleanup
rm "$BASE_IMAGE" "${picture_names[@]}"

