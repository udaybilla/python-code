import boto3
import json

ec2 = boto3.resource('ec2',region_name='us-east-1')
base = ec2.volumes.all()
filters = [{
        'Name': 'status',
            'Values': ['available']
            }]
filtered = base.filter(Filters=filters)

myList=[]
def lambda_handler(event, context):
      deleteEbsVolumes()
      copySnapshots()
      return myList
        

def deleteEbsVolumes():
            for vol in filtered:
                    snap = vol.create_snapshot(vol.id)
                        print ("Snapshot taken successfully")
                            vol.delete(vol.id)
                                print ("Deleting the orphaned EBS volumes" +vol.id)
                                    myList.extend([vol.id,snap.id])
                                        
def copySnapshots()                                          
  print (myList)
