import json
import os

import boto3
from aws_lambda_powertools import Logger

logger = Logger(service="create-item")


@logger.inject_lambda_context(log_event=True)
def handle_event(event, context):
    bucket_name = os.environ["BUCKET"]
    s3 = boto3.client("s3", region_name="eu-west-1")
    s3.put_object(
        Bucket=bucket_name,
        Key="example.json",
        Body=json.dumps({"message": "hello world"}),
    )

    return {"status_code": 200}
