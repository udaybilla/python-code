import boto3
import json

ec2 = boto3.resource('ec2',region_name='us-east-1')
client = boto3.client('ec2')
base = ec2.volumes.all()
filters = [{
        'Name': 'status',
            'Values': ['available']
            }]
filtered = base.filter(Filters=filters)

myEbs=[]
myEbsSnap=[]

def lambda_handler(event, context):
      deleteEbsVolumes()
        copySnapshots()
          return myEbs,myEbsSnap

      def deleteEbsVolumes():
            for vol in filtered:
                    snap = vol.create_snapshot(vol.id)
                        print ("Snapshot taken successfully")
                            vol.delete(vol.id)
                                print ("Deleting the orphaned EBS volumes" +vol.id)
                                    myEbs.append(vol.id)
                                        myEbsSnap.append(snap.id)
                                            
                                            def copySnapshots():
                                                   print (myEbsSnap,myEbs)
                                                      for snapId in myEbsSnap:
                                                               print (snapId)
                                                                    response = client.copy_snapshot(SourceRegion='us-east-1', DestinationRegion='us-east-2', SourceSnapshotId=snapId, Description='Copy of ebs snapshots')
