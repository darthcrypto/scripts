#!/bin/bash


namelist='dsinghal ebennet jborrero test1 tgraytest'

for i in $namelist; do
	chown -R $i:$i /home/$i
	if [ $? -ne 0 ]; then
		echo "ERROR: the permissions on $i's home directory were not changed"
		exit 1
	else
		echo "the permissions on $i's home directory were changed successfully"
	fi
done
