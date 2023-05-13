import boto3

from app.shared.database.partitions.feedback_partition import FeedbackPartition

class DynamodbClient:

    def __init__(self) -> None:

        # create dynamodb resources
        dynamodb = boto3.resource('dynamodb')
        graphidot_objects_table = dynamodb.Table('graphidot_objects_dev')
        client = boto3.client('dynamodb')

        # Instantiate a class for each partition for the graphidot objects table
        self.feedback = FeedbackPartition(graphidot_objects_table, client)