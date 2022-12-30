#!/usr/bin/bash
#* this above line used for all shell script
#* which interpeter absoult path is /usr/bin/bash

## Creator :: Debraj Das
## This Script create for store improtance syntex of scripting of shell

# #~ Special type variable

# echo "File name : $0"
# echo "First parameter : $3"
# echo "Exit status of previous : $?"
# echo "Quoted Vaules: $*"
# echo "No of Patameter : $#"
# echo "process number : $$"

# #~ looping of command

# for Token in $*
# do
#         echo "$Token"
# done

# #~ general command
# echo "what is your name? "
# read -r -p "for string"  Person
# readonly Person  // this command use for change the variable into constant
# unset Person   // this command use for delete the variable
# echo "Hello, $Person"
# echo -n "no trailing newline"
# printf "\ttryout printf command\n"
# printf "number is %d\n\n" "10"

# #~ Arithmetic Operator

# a=5  // assignment operator
# b=2

# Sum=$((a+b))
# echo "print the vaule of Sum = $Sum"
# Sum=$((a-b))
# echo "print the vaule of subtraction = $Sum"
# Sum=$((a*b))
# echo "print the vaule of mul = $Sum"
# Sum=$((b/a))
# echo "print the vaule of division = $Sum"
# Sum=$((b%a))
# echo "print the vaule of mod = $Sum"
# Sum=$((a**b))
# echo "vaule of expotential : $Sum"
# #* arithmatic operation with integer number
# var=$((30+10))
# echo "vaule of var = $var"
# var=$((5/2))
# echo "vaule of $var"
# #* arithmatic operation with float type number
# bc <<< 'scale=2; 100/3'
# echo "vaule by printed $(bc <<< 'scale=4; 32.5/3')"
# var=$(bc <<< 'scale=4; 10.5/3')
# echo "vaule of var $var"

# #~ breching
# a=34
# b=235

# #* relation opretion part
# if (( "$a"=="$b" ))
# then
#     echo "a is equal to b"
# else
#     echo "a is not equal to b"
# fi

# if  (( "$a"!="$b" ))
# then
#     echo "a is not equal to b"
# fi
# if(( "$a"<"$b" ))
# then
#     echo a is less than b.
# else
#     echo a is not less than b.
# fi

# if(( "$a"<="$b" ))
# then
#     echo a is less than or equal to b.
# else
#     echo a is not less than or equal to b.
# fi

# if (( "$a">"$b" ))
# then
#     echo a is greater than b.
# else
#     echo a is not greater than b.
# fi

# if(( "$a">="$b" ))
# then
#     echo a is greater than or equal to b.
# else
#     echo a is not greater than or equal to b.
# fi

# if [ "$a" == "$b" ]; then
#     echo "a is equal to b"
# elif [ "$a" -gt "$b" ]; then
#     echo "a is greater than b"
# elif [ "$a" -lt "$b" ]; then
#     echo "a is less than b"
# else
#     echo "None of the condition met"
# fi

# #* logical oprator part
# #reading data from the user
# read -r -p 'Enter a : ' a
# read -r -p 'Enter b : ' b

# if ((("$a" == "1") && ("$b" == "1")));
# then
#     echo Both are 1.
# else
#     echo Both are not 1.
# fi

# if ((("$a" == "1") || ("$b" == "1")));
# then
#     echo Atleast one of them is 1.
# else
#     echo None of them is 1.
# fi

# if ((!"$a" == "1"));
# then
#     echo "a" was initially false.
# else
#     echo "a" was initially 1.
# fi

# #* Boolean operation or Bitwish operation
# #reading data from the user
# read -r -p 'Enter a : ' a
# read -r -p 'Enter b : ' b

# bitwiseAND=$((a & b))
# echo Bitwise AND of a and b is $bitwiseAND

# bitwiseOR=$((a | b))
# echo Bitwise OR of a and b is $bitwiseOR

# bitwiseXOR=$((a ^ b))
# echo Bitwise XOR of a and b is $bitwiseXOR

# bitiwiseComplement=$((~a))
# echo Bitwise Compliment of a is $bitiwiseComplement

# leftshift=$((a << 1))
# echo Left Shift of a is $leftshift

# rightshift=$((b >> 1))
# echo Right Shift of b is $rightshift

# #* File Test Operator part
# #reading data from the user
# read -r -p 'Enter file name : ' FileName

# if [ -b "$FileName" ]; then
#     echo The given file is block Special file.
# else
#     echo The given file is not block Special file.
# fi

# if [ -c "$FileName" ]; then
#     echo The given file is character Special.
# else
#     echo The given file is not character Special.
# fi

# if [ -d "/usr/add" ]; then
#     echo The /usr/add dir is exit.
# else
#     echo The /usr/add dir is not exit.
# fi

# if [ -e "$FileName" ]; then
#     echo File Exist
# else
#     echo File doesnot exist
# fi

# if [ -s "$FileName" ]; then
#     echo The given file is not empty.
# else
#     echo The given file is empty.
# fi

# if [ -r "$FileName" ]; then
#     echo The given file has read access.
# else
#     echo The given file does not has read access.
# fi

# if [ -w "$FileName" ]; then
#     echo The given file has write access.
# else
#     echo The given file does not has write access.
# fi

# if [ -x "$FileName" ]; then
#     echo The given file has execute access.
# else
#     echo The given file does not has execute access.
# fi

# #* string operator part
# working with part of the string
# read -r name 
# part=${name:3:3}
# echo "$part"

# str1="GeeksforGeeks"
# str2="geeks"
# if [ $str1 = $str2 ]; then
#     echo "Both string are same"
# else
#     echo "Both string are not same"
# fi

# if [ $str1 != $str2 ]; then
#     echo "Both string are not same"
# else
#     echo "Both string are same"
# fi

# if [ $str1 \< $str2 ]; then
#     echo "$str1 is less than $str2"
# else
#     echo "$str1 is not less than $str2"
# fi

# if [ $str1 \> $str2 ]; then
#     echo "$str1 is greater than $str2"
# else
#     echo "$str1 is less than $str2"
# fi

# if [ -n "$str1" ]; then
#     echo "String is not empty"
# else
#     echo "String is empty"
# fi

# str=""
# if [ -z "$str" ]; then
#     echo "String is empty"
# else
#     echo "String is not empty"
# fi
### this point Basic operation is finish
### looping concept is start
# #* for loop example
# for var in 0 1 2 3 4 5 6 7 8 9
# do
#     echo "$var"
# done

# for var in {1..50..2} // for continous print numbers by 2 interval
# do
#     echo "$var"
# done

# #* while loop example
# a=0
# while  (("$a"<=10))
# do
#     echo $a
#     ((++a))
# done

# #* until loop example
# a=0
# until  ! (("$a"<=10))
# do
#     echo $a
#     ((++a))
# done

# #* nesting of loop example
# echo -n "Enter a number :: "
# read -r n
# a=0
# while (("$a" <= "$n")); do
#     b="$a"
#     while (("$b" >= 0)); do
#         echo -n "* "
#         ((--b))
#     done
#     echo
#     ((++a))
# done
# echo  # this read for newline

# #* infinite loop example
# i=0
# while true
# do
#     echo "$i"
#     ((++i))
# done

# #* control statement --> break and continue
# i=1
# while true
# do
#     if (("$i"==100))
#     then
#         break
#     fi
#     if (("$i%5"==0))
#     then
#         ((++i))
#         continue
#     fi
#     echo "$i"

#     ((++i))
# done
# ## finished the looping concept

# ## function concept is start
# #* Define function
# Hello() {
#     echo "Hello $1"
#     return 23
# }

# #* Invoke function
# Hello Debraj
# echo "$?"

# #* nesting of function
# number_one() 
# {
#     echo "Alpha online...over"
#     number_two
# }
# #@ function order need not be sequence // exception form C languege
# number_two() 
# {
#     echo "Beta online...over"
# }

# #* invoked function
# number_one
# ## function is finished

# #~ Shell Scription Crash Course's learning part is finish


