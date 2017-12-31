#!/bin/bash
rsync_procs=`ps aux | grep melgayar | wc - l`
$rsync_procs

#if ${rsync_procs} -gt 5; then
#     echo "CRITICAL - Over 1,000 rsync processes running"
#     exit 2
#else
#     echo "OK - Less than 1,000 rsync processes running"
#     exit 0
#fi
