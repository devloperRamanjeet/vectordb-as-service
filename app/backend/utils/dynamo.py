import boto3
from flask import current_app

def store_metadata(item: dict):
    table_name = current_app.config["DYNAMO_TABLE"]
    region = current_app.config["AWS_REGION"]

    dynamo = boto3.resource("dynamodb", region_name=region)
    table = dynamo.Table(table_name)
    return table.put_item(Item=item)
