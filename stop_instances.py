import boto3
import os

def handler(event, context):
    ec2 = boto3.client('ec2')
    filters = [{ 'Name': 'tag:{0}'.format(os.getenv('TAG_NAME')), 'Values': ['ON', 'On', 'on', 'TRUE', 'True', 'true', '1'] }]
    responce = ec2.describe_instances(Filters = filters)
    instanceIds = []
    for reservation in responce['Reservations']:
        for instance in reservation['Instances']:
            instanceIds.append(instance["InstanceId"])
    print ("Stop Instances {0}".format(instanceIds))
    ec2.stop_instances(InstanceIds = instanceIds)
