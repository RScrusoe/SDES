#!/bin/bash
HELLO=Hello
function hello {
	local HELLO=WORLD!
	echo $HELLO
}
echo $HELLO
hello
echo $HELLO
