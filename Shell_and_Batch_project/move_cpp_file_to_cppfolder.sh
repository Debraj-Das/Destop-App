#!/usr/bin/bash
#* it alias is mvcpp
echo "C++ file(cppfile.cpp) move cppfolder in window dir***"
read -r -p 'Only name of the new C++ file :: ' name
name+=".cpp"
cp cppfile.cpp "$name"
mv "$name" /mnt/c/Users/debra/Desktop/programming/Vs_code/cppfolder
echo "***Done***"