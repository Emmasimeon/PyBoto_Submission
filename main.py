import eel
import boto3

# eel.init('Web')

# eel.start('index.html')

ec2 = boto3.resource('ec2')
sts_client = boto3.client('sts', region_name='eu-central-1', endpoint_url='https://sts.eu-central-1.amazonaws.com')
# for instance in ec2.instances.all():
#      print(
#          "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
#          instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
#          )
#      )

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)