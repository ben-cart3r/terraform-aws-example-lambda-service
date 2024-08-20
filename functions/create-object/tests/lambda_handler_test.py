import json

import boto3
from moto import mock_aws

from src.lambda_handler import handle_event


@mock_aws
def test_lambda_creates_object(lambda_context):
    # Setup the dependent resources
    bucket_name = "my-bucket"
    s3 = boto3.client("s3", region_name="eu-west-1")
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )

    # Invoke the lambda to create the object
    handle_event({}, lambda_context)

    # Verify an object was created
    list_objects_response = s3.list_objects_v2(
        Bucket=bucket_name,
    )

    assert len(list_objects_response["Contents"]) == 1
    assert list_objects_response["Contents"][0]["Key"] == "example.json"

    # Verify the content of the created object
    get_object_response = s3.get_object(
        Bucket=bucket_name,
        Key=list_objects_response["Contents"][0]["Key"],
    )

    object_content = json.loads(get_object_response["Body"].read())

    assert "message" in object_content
    assert object_content["message"] == "hello world"
