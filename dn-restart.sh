#!/bin/bash

dnlist='dn-0109-18 dn-0109-20 dn-0109-26 dn-0109-28 dn-0109-32 dn-0109-34 dn-0109-38 dn-0109-40 dn-0109-42 dn-0109-44 dn-0110-20 dn-0110-26 dn-0110-28 dn-0110-30 dn-0110-32 dn-0110-34 dn-0110-36 dn-0110-38 dn-0110-40 dn-0110-42 dn-0110-44 dn-0111-18 dn-0111-20 dn-0111-26 dn-0111-28 dn-0111-30 dn-0111-32 dn-0111-34 dn-0111-36 dn-0111-38 dn-0111-40 dn-0111-42 dn-0111-44 dn-0112-16 dn-0112-18 dn-0112-20 dn-0112-26 dn-0112-28 dn-0112-30 dn-0112-34 dn-0112-36 dn-0112-38 dn-0113-02 dn-0113-06 dn-0113-10 dn-0113-14 dn-0113-16 dn-0113-18 dn-0113-20 dn-0113-26 dn-0113-28 dn-0113-30 dn-0113-32 dn-0113-34 dn-0113-36 dn-0113-38 dn-0113-40 dn-0201-02 dn-0201-04 dn-0201-06 dn-0201-08 dn-0201-10 dn-0201-12 dn-0201-16 dn-0201-18 dn-0202-02 dn-0202-04 dn-0202-06 dn-0203-10 dn-0203-12 dn-0203-14 dn-0203-36 dn-0203-38 dn-0203-40 dn-0203-44 dn-0204-06 dn-0204-08 dn-0204-10 dn-0204-12 dn-0204-14 dn-0204-16 dn-0204-18 dn-0204-20 dn-0204-26 dn-0204-28 dn-0204-32 dn-0204-34 dn-0204-40 dn-0205-02 dn-0205-08 dn-0205-10 dn-0205-12 dn-0205-16 dn-0205-18 dn-0205-20 dn-0205-26 dn-0205-30 dn-0205-32 dn-0205-36 dn-0205-40 dn-0206-02 dn-0206-04 dn-0206-06 dn-0206-08 dn-0206-10 dn-0206-12 dn-0206-14 dn-0206-16 dn-0206-18 dn-0206-20 dn-0207-30 dn-0207-34 dn-0207-36 dn-0207-38 dn-0207-40 dn-0207-42 dn-0208-38 dn-0208-40 dn-0208-44' 

for i in $dnlist; do
	ssh -o StrictHostKeyChecking=no root@$i "service hadoop-hdfs-datanode restart"
	if [ $? -ne 0 ]; then
                echo "ERROR: the datanode service on $i did not restart"
                exit 1
        else
                echo "SUCCESS: the datanode service on $i was restarted"
        fi
done

