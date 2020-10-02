import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.resource('ec2')
    cw = boto3.client('cloudwatch')
    running_instances = ec2.instances.filter(Filters=[{'Name': 'tag:percona_db','Values': ['Node1-master'],}])
    action=event['Action']
    if action == 'Launch':
      for instance in running_instances:
                    #DiskSpaceUtilization Alarms when > 50 %
                        cw.put_metric_alarm(
                         AlarmName="DiskSpaceUtilization(Lambda)-alaram",
                         AlarmDescription='DiskSpaceUtilization',
                         ActionsEnabled=False,
                         MetricName='DiskSpaceUtilization',
                         Namespace='System/Linux',
                         Statistic='Average',
                         TreatMissingData='notBreaching',
                         Period=300,
                         EvaluationPeriods=1,
                         Threshold=50,
                         ComparisonOperator='GreaterThanThreshold',
                         Dimensions =[{'Name': 'MountPath', 'Value': '/'},
                         {'Name': 'InstanceId', 'Value':'i-097a19830849621d8'},
                         {'Name': 'Filesystem', 'Value': '/dev/xvda1'}],)
            
      return {
        'statusCode': 200,
        'body': json.dumps('Alarm created')
      }
           
            
    elif action == "Terminated":
        response = cw.delete_alarms(
           AlarmNames=[
        'DiskSpaceUtilization(Lambda)-alaram',
            ]
        )
    else:
        return {
        'statusCode': 200,
        'body': json.dumps('No alaram created')
        }

      