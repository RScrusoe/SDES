#!/bin/bash
# Nested if statements
if [ $1 -gt 100 ]
then
echo "Hey that's a large number."
if (( $1 % 2 == 0 ))
then
echo "And is also an even number."
fi
fi


echo "Enter any 2 numbers"
read n1 n2
if [ $n1 -lt $n2 ]; then
	echo "1st < 2nd"
elif [ $n1 -gt $n2 ]; then
	echo "1st > 2nd"
else
	echo "1st == 2nd" 
fi
