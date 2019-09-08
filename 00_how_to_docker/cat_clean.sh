#!/bin/sh
files=$(ls)
for file in $files
do
	echo  "FILE: $file -----------------\n"
	cat $file
	echo "END OF FILE: $file ==============================\n\n\n\n\n\n\n"
done	
