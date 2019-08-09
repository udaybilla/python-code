import boto3
import json

ec2 = boto3.resource('ec2',region_name='us-east-1')
base = ec2.volumes.all()
filters = [{
        'Name': 'status',
            'Values': ['available']
            }]
filtered = base.filter(Filters=filters)
def lambda_handler(event, context):
      for vol in filtered:
              vol.delete(vol.id)
                  print ("Deleting the orphaned EBS volumes" +vol.id)
                      return vol.id
