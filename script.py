import boto3

ec2 = boto3.resource('ec2',
aws_access_key_id = 'ENTER ACCESS KEY', #You can ignore if your AWS CLI environment is configured
aws_secret_access_key = 'ENTER SECRET KEY', #You can ignore if your AWS CLI environment is configured
region_name = 'eu-central-1'
)

ServerName = (input("Please enter an EC2 Instance Name or '*' to show all Servers: "))

instances = list(ec2.instances.filter(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                ServerName
            ]
        }
    ]
))


if len(instances) > 0:
    for instance in instances:
        print(
         "INSTANCE-ID:  {0}\nINSTANCE-TYPE:  {1}\nSTATUS:  {2}\nPRIVATE-IPv4:  {3}\nPUBLIC-IPv4:  {4}\nINSTANCE-NAME:  {5}\n ".format(
         instance.id, instance.instance_type, instance.state, instance.private_ip_address, instance.public_ip_address, instance.tags[0], 
         )
     )
else:
    print("No instance found with the provided name")


