#lambda function to snapshot ipa-master

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    region = "us-east-1"
    
    #create snapshot of ipa-master
    result = ec2.create_snapshot(VolumeId='vol-0af59b956e05c36a2', Description='Created by Lambda function ebs-snapshots')

    #get snapshot resource
    ec2resource = boto3.resource("ec2", region_name=region)
    snapshot = ec2resource.Snapshot(result['SnapshotId'])

    #add tag to snapshot
    snapshot.create_tags(Tags=[{'Key': 'Name','Value': 'ipa-master-backup'}])

