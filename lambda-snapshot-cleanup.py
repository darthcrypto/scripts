#delete ipa-master-backup snapshots older than retention period

import boto3
from botocore.exceptions import ClientError
from datetime import datetime,timedelta

def delete_snapshot(snapshot_id, region):
     
    region = "us-east-1"

    print "Deleting snapshot %s" % (snapshot_id)
    try:
        ec2resource = boto3.resource('ec2', region_name=region)
        snapshot = ec2resource.Snapshot(snapshot_id)
        snapshot.delete()
    except ClientError as e:
        print "Caught exception: %s" % e

    return

def lambda_handler(event, context):
         
    region = "us-east-1"

    #Get current timestamp in UTC
    now = datetime.now()
    
    #Define retention period in days
    retention_days = 60

    #Create EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    #Filter for any snapshot tagged ipa-master-backup
    filters = [{'Name': 'tag:Name', 'Values': ['ipa-master-backup']}]
    result = ec2.describe_snapshots.(Filters=filters)

    #Determine if snapshots need to be deleted
    for snapshot in result['Snapshots']:
       print "Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime'])
       snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
       if (now - snapshot_time) > timedelta(retention_days):
          print "Snapshot is older than configured retention of %d days" % (retention_days)
          delete_snapshot(snapshot['SnapshotId'], region)
       else:
          print "Snapshot is newer than configured retention of %d days so we keep it" % (retention_days)
