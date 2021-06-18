#!/usr/bin/python
import boto3
import datetime
import pytz

ec2 = boto3.resource('ec2')

print("\n\nAWS snapshot backups starting at %s" % datetime.datetime.now())
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    instance_name = filter(lambda tag: tag['Key'] == 'Name', instance.tags)[0]['Value']

    for volume in ec2.volumes.filter(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance.id]}]):
        description = 'scheduled_snapshot-%s.%s-%s' % (instance_name, volume.volume_id,
            datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

    if volume.create_snapshot(VolumeId=volume.volume_id, Description=description):
        print("Snapshot created with description [%s]" % description)

    for snapshot in volume.snapshots.all():
        retention_days = 15
        if snapshot.description.startswith('scheduled_snapshot-') and ( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days):
            print("\t\tDeleting snapshot [%s - %s]" % ( snapshot.snapshot_id, snapshot.description ))
            snapshot.delete()

print("\n\nAWS snapshot backups completed at %s" % datetime.datetime.now())