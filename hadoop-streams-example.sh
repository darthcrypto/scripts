#!/bin/bash
usage="Usage: ./list-old-hdfs-files.sh [path] [days]"

if [ ! "$1" ]
then
  echo $usage;
  exit 1;
fi

if [ ! "$2" ]
then
  echo $usage;
  exit 1;
fi

now=$(date +%s);

# Loop through files
#sudo -u hdfs hdfs dfs -ls $1 | while read f; do
hdfs dfs -ls $1 | while read f; do
  # Get File Date and File Name
  file_date=`echo $f | awk '{print $6}'`;
  file_name=`echo $f | awk '{print $8}'`;

  # Calculate Days Difference
  difference=$(( ($now - $(date -d "$file_date" +%s)) / (24 * 60 * 60) ));
  if [ $difference -gt $2 ] && [ $file_name != "/tmp/hierarchyExport/cache" ]; then
    echo "$file_name is dated $file_date." 2>&1 | tee -a /var/log/hierarchyExportRetention.log
    hadoop fs -rm -r $file_name 2>&1 | tee -a /var/log/hierarchyExportRetention.log
      if [ $? -ne 0 ]; then
         echo "ERROR: $file_name was not deleted" 2>&1 | tee -a /var/log/hierarchyExportRetention.log
         exit 1
      else
         echo "$file_name has been successfully deleted" 2>&1 | tee -a /var/log/hierarchyExportRetention.log
      fi
  fi
done


#in order to print to screen and append to log:
#echo "$file_name is dated $file_date." 2>&1 | tee -a /var/log/hierarchyExportRetention.log

#in order to just append to log:
#echo "$file_name is dated $file_date." >> /var/log/hierarchyExportRetention.log 2>&1
