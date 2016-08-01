#/bin/bash
name=fossee
#file=out.txt
count=`wc -w $1 | cut -d " " -f -1 -`
echo $count
echo 'You Rock!!!!'
