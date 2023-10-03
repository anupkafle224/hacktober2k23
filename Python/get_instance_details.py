import boto3

def get_instance_status(instance_id):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        if response['Reservations']:
            instance = response['Reservations'][0]['Instances'][0]
            return instance['State']['Name']
        else:
            return "Instance not found"
    except Exception as e:
        return f"Error: {str(e)}"

def lambda_handler(event, context):
    instance_id = 'your-instance-id'
    
    status = get_instance_status(instance_id)
    
    return {
        'statusCode': 200,
        'body': f"Instance status: {status}"
    }
