#!/bin/bash

for k in `seq -f"ics%03g" 001 072`; do 
	ssh -o StrictHostKeyChecking=no root@$k "hostname"
	ssh -o StrictHostKeyChecking=no root@$k "time"; 
done
