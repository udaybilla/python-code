import boto3
import json

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    
    fileName = 'B-patch-01-09-2018.json'
    content_object = s3.Object('cookeryportal', fileName)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    
    json_content = json.loads(file_content)
    
    
   
    booking = ""
    
    newChar = "\n"
    fileName = 'david_test/'+fileName
    
    for x in json_content['Bookings']:
        x = str(x).replace("'", "\"").replace("None","null")
        booking+=str(x)
        print(x)
        
        booking+=","
        booking+=newChar
    
    object = s3.Object('cookeryportal', fileName)
    object.put(Body=(booking))
    


