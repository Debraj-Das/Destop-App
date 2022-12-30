#!/usr/bin/bash
#* it alias is mvc
echo "C file(cfile.c) move cfolder in window dir***"
read -r -p 'Only new name of the C file :: ' name
name+=".c"
cp cfile.c "$name"
mv "$name" /mnt/c/Users/debra/Desktop/programming/Vs_code/cfolder
echo "***Done***"