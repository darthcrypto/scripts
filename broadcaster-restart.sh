#!/bin/bash

dnlist='brc003 brc005 brc006 brc007 brc008 brc009 brc010 brd001 brd003 brd004 brd005 brd007 brd008 brd009 brd011 brd012 brd013 brd014 brd015 brd016 brd017'


for i in $dnlist; do
	ssh -o StrictHostKeyChecking=no root@$i "service broadcaster restart"
	if [ $? -ne 0 ]; then
                echo "ERROR: the datanode service on $i did not restart"
                exit 1
        else
                echo "SUCCESS: the datanode service on $i was restarted"
        fi
done

