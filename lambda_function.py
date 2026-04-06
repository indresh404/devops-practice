def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Serverless!'
    }


if __name__ == "__main__":
    response = lambda_handler({}, {})
    print(response)