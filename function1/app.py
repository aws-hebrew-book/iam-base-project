import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')
    response = client.invoke(FunctionName="function1-iam")
    print(response["Payload"])
