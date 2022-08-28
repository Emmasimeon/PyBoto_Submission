import boto3

ec2 = boto3.resource('ec2',
aws_access_key_id = 'AKIARVUON5BPH5H7S74C',
aws_secret_access_key = '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',
region_name = 'eu-central-1'
)

ServerName = (input("Please enter an EC2 Instance Name or '*' to show all Servers: "))

if ServerName == "*":
    for instance in ec2.instances.all():
        print(
         "INSTANCE-ID:  {0}\nINSTANCE-TYPE:  {1}\nSTATUS:  {2}\nPRIVATE-IPv4:  {3}\nPUBLIC-IPv4:  {4}\nTOTAL-EBS-VOLUME:  {5}\n  {6}\nVOLUME".format(
         instance.id, instance.instance_type, instance.state, instance.private_ip_address, instance.public_ip_address, instance.state, volume.volume
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

sts_client = boto3.client('sts', region_name='eu-central-1', endpoint_url='https://sts.amazonaws.com')



print("Thank You!!!")

