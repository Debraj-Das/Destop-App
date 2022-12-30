@ECHO OFF
if EXIST "skjhfwher2832928yr294hgq923ery1h37et123" goto UNLOCK

if NOT EXIST "Personal folder" goto make_new_dir

ren "Personal folder" "skjhfwher2832928yr294hgq923ery1h37et123"
attrib +h +s "skjhfwher2832928yr294hgq923ery1h37et123"
echo Folder locked
goto End

:UNLOCK
echo Enter password to Unlock Your Secure Folder
set/p "pass=>> "
if NOT %pass%== 6033 goto End
attrib -h -s "skjhfwher2832928yr294hgq923ery1h37et123"
ren "skjhfwher2832928yr294hgq923ery1h37et123" "Personal folder"
goto End


:make_new_dir
md "Personal folder"
goto End

:End