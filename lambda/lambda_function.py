import boto3
import os

def lambda_handler(event, context):
    sns = boto3.client('sns')

    topic_arn = os.environ['SNS_TOPIC_ARN']

    sns.publish(
        TopicArn=topic_arn,
        Message='New Docker image built and pushed successfully!',
        Subject='CI/CD Notification'
    )

    return {"statusCode": 200}
