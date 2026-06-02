import boto3
import random
import json

# DynamoDB connection
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")

# Bedrock client
bedrock = boto3.client("bedrock-runtime")


def lambda_handler(event, context):

    # Busca os fatos do DynamoDB
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "fact": "Nenhum fato encontrado."
            })
        }

    # Escolhe fato aleatório
    fact = random.choice(items)["FactText"]

    # Prompt enviado para Claude
    prompt = f"""
    Transforme esse fato sobre computação em nuvem em algo divertido,
    inteligente e curto em português brasileiro:

    {fact}
    """

    try:

        response = bedrock.converse(
            modelId="arn:aws:bedrock:us-east-1:905663669292:application-inference-profile/ta11c63gn6l5",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 100,
                "temperature": 0.7
            }
        )

        generated_fact = response["output"]["message"]["content"][0]["text"]

    except Exception as e:

        generated_fact = f"Erro no Bedrock: {str(e)}"

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
    "fact": generated_fact
}, ensure_ascii=False)
    }