import boto3

ec2 = boto3.resource('ec2',
aws_access_key_id = 'ENTER ACCESS KEY OR IGNORE', #You can ignore if your AWS CLI environment is configured
aws_secret_access_key = 'ENTER SECRET KEY OR IGNORE', #You can ignore if your AWS CLI environment is configured
region_name = 'eu-central-1'
)

ServerName = (input("Please enter an EC2 Instance Name or '*' to show all Servers: "))

if ServerName == "*":
    for instance in ec2.instances.all():
        print(
         "INSTANCE-ID:  {0}\nINSTANCE-TYPE:  {1}\nSTATUS:  {2}\nPRIVATE-IPv4:  {3}\nPUBLIC-IPv4:  {4}\nTOTAL-EBS-VOLUME:  {5}\n ".format(
         instance.id, instance.instance_type, instance.state, instance.private_ip_address, instance.public_ip_address, instance.state, 
         )
     )
     
else:
    Instance = ec2.describe_instances(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                ServerName
            ]
        },
    ]
)
    print("Requested Server details " + ServerName)


print("Thank You!!!")

