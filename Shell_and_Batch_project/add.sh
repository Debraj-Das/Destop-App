#!/usr/bin/bash
#* it alias is add
#* This script do move file to /usr/add folder
if [ -n "$1" ]
 then
    sudo mv "$1" /usr/add/
fi
