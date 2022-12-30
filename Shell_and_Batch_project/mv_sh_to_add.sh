#!/usr/bin/bash
#* it alias is shadd
echo "Move Script shell file(script.sh) to add folder****"
read -r -p "Only name of new Script file :: " file_name
file_name+=".sh"
cp script.sh $file_name
chmod +x $file_name
sudo mv $file_name /usr/add 
clear
