#!/bin/bash
#Declare array with 4 elements
ARRAY=( 'Debian Linux' 'Redhat Linux' Ubuntu Linux )
# get number of elements in the array
ELEMENTS=${#ARRAY[@]}
echo $ELEMENTS
echo $ARRAY
echo $ARRAY[@]
# echo each element in array 
# for loop
echo ''
for (( i=0;i<$ELEMENTS;i++));
do
    echo ${ARRAY[${i}]}
done 

for ((i=0;i<10;i++));
do
	echo $i
done
