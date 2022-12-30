#!/usr/bin/bash
#* it alias is mvpy
echo "Python file(python.py) move pyfolder in window dir****"
read -r -p 'Only new name of the Python file :: ' name
name+=".py"
cp python.py "$name"
mv "$name" /mnt/c/Users/debra/Desktop/programming/Vs_code/pyfolder
echo "***Done***"