import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Use the client to describe instances
response = ec2_client.describe_instances()

# Loop through the instances and print their details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Private IP Address: {instance['PrivateIpAddress']}")
        print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
        print(f"State: {instance['State']['Name']}")
        print("---")

