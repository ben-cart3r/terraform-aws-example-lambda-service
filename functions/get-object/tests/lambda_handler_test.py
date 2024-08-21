import json
import os

import boto3
from moto import mock_aws

from src.lambda_handler import handle_event


@mock_aws
def test_lambda_returns_object(lambda_environment, lambda_context):
    # Setup the dependent resources
    bucket_name = os.environ["BUCKET"]
    s3 = boto3.client("s3", region_name="eu-west-1")
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )
    s3.put_object(
        Bucket=bucket_name,
        Key="example.json",
        Body=json.dumps({"message": "hello world"}),
    )

    # Invoke the lambda to retrieve the object
    response = handle_event({}, lambda_context)
    response_body = json.loads(response["body"])

    # Verify the content of the returned object
    assert response["status_code"] == 200
    assert response_body["message"] == "hello world"
