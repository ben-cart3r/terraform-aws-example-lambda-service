import boto3
from aws_lambda_powertools import Logger

logger = Logger(service="get-object")

@logger.inject_lambda_context(log_event=True)
def handle_event(event, context):
    s3 = boto3.client("s3", region_name="eu-west-1")

    response = s3.get_object(
        Bucket="my-bucket",
        Key="example.json",
    )

    return {
        "status_code": 200,
        "body": response["Body"].read()
    }
