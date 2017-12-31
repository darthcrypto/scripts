#!/bin/bash


namelist='agarnet amagoon anichols ashah asunder asuryavanshi cconnell clacy cschammel dbarnett djoseph dmurnane dsachs dsinghal eangeloni gmurnane ipakeymaster jbidwell jsteel jtabeling jwu khardwick lsamuels mconrad mgersten mmarcus mnepo mspada nconrad sknippenberg sromack tgray'

for i in $namelist; do
	chown -R $i:$i /home/$i
	if [ $? -ne 0 ]; then
		echo "ERROR: the permissions on $i's home directory were not changed"
		exit 1
	else
		echo "the permissions on $i's home directory were changed successfully"
	fi
done
