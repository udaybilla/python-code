import json
import boto3

def lambda_handler(event, context):
    
    '''#Stopping Ec2 instances
    ec2 = boto3.resource('ec2')
    
    #Filter running instances
    running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])
    
    for instance in running_instances:
        print(instance.instance_id)
        instance.stop()
    '''
    
    
    
    #Stopping RDS instances
    rds = boto3.client('rds')
    rds_instances = rds.describe_db_instances()
    print(rds_instances)
    

    rds_availability = rds_instances.get('DBInstances')[0].get('DBInstanceStatus')
    rds_name = rds_instances.get('DBInstances')[0].get('DBInstanceIdentifier')
    print("instance {} status: {}".format(rds_name,rds_availability))
        
        
    for i in rds_instances:
        if rds_availability == 'available' and rds_name == 'cookeryportaldb':
          rds.stop_db_instance(DBInstanceIdentifier=rds_name)
          print("instance {} succesfully stopped".format(rds_name))
        elif rds_availability == 'stopped':
            print("instance {} is already stopped".format(rds_name))
          
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('succesfully stopped!')
    }
