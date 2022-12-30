#!/usr/bin/bash
#* it alias is run
#* This script do complied and run any complied code files
if make "$1"; then
    if [ "$2" == $"t" ]; then
        echo
        time ./"$1"
        echo
    elif [ "$2" == $"s" ]; then
        echo
        valgrind ./"$1"
        echo
    else
        echo
        ./"$1"
        echo
    fi
fi
