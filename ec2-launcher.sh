#!/bin/bash

#launches centos 7 image in dev shared vpc with ssh access 

aws ec2 run-instances \
--image-id ami-a679ebb0 \
--instance-type t2.micro \
--security-group-ids sg-15d7336a \
--key-name ops-us-east-1 \
--subnet-id subnet-23a6be6a \
--count 1 \
--query 'Instances[0].InstanceId'
