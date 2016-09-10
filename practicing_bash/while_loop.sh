#!/bin/bash
CT=1
while [ $CT -le 10 ];
do
	echo $CT
	let CT=CT+1
done

for ls in  `ls` ;
do
	echo "File name is : $ls" 
done

read n1 n2
declare -i rs
rs=$n1*$n2
echo $rs

read n1 n2
let DIV=n1/n2
echo $DIV

 cat $1 2>&1 