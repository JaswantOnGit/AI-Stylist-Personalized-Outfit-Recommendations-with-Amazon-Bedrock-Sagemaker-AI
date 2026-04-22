"""
AI Stylist - Lambda Function
Author: Jaswant Singh
Generates personalized outfit recommendations using Amazon Bedrock (Nova Micro + Nova Canvas).
Deployed as a serverless AWS Lambda function behind API Gateway.
"""

import json
import boto3
import base64
import uuid
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
s3 = boto3.client("s3")

S3_BUCKET = os.environ.get("S3_BUCKET_NAME", "ai-stylist-outputs")


def build_outfit_prompt(user_input: dict) -> str:
    """Construct a structured prompt from user preferences."""
    return (
        f"You are a professional fashion stylist. Create a detailed outfit recommendation for:\n"
        f"- Occasion: {user_input.get('occasion', 'Casual')}\n"
        f"- Season: {user_input.get('season', 'Spring')}\n"
        f"- Style: {', '.join(user_input.get('styles', ['Classic']))}\n"
        f"- Preferred Colors: {', '.join(user_input.get('colors', ['Neutral']))}\n"
        f"- Gender: {user_input.get('gender', 'neutral')}\n"
        f"- Notes: {user_input.get('custom_prompt', '')}\n\n"
        f"Provide: 1) Complete outfit description, 2) Key pieces, 3) Styling tips."
    )


def generate_outfit_text(prompt: str) -> str:
    """Call Bedrock Nova Micro for outfit description text."""
    response = bedrock.invoke_model(
        modelId="amazon.nova-micro-v1:0",
        body=json.dumps({
            "messages": [{"role": "user", "content": prompt}]
        }),
        contentType="application/json",
        accept="application/json"
    )
    body = json.loads(response["body"].read())
    return body["output"]["message"]["content"][0]["text"]


def generate_outfit_image(description: str) -> str:
    """Call Bedrock Nova Canvas to generate outfit image. Returns S3 URL."""
    image_prompt = f"Fashion photography, full outfit: {description[:300]}"
    response = bedrock.invoke_model(
        modelId="amazon.nova-canvas-v1:0",
        body=json.dumps({
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": image_prompt},
            "imageGenerationConfig": {
                "width": 512,
                "height": 512,
                "numberOfImages": 1
            }
        }),
        contentType="application/json",
        accept="application/json"
    )
    body = json.loads(response["body"].read())
    image_data = base64.b64decode(body["images"][0])

    image_key = f"outfits/{uuid.uuid4()}.png"
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=image_key,
        Body=image_data,
        ContentType="image/png"
    )
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{image_key}"


def lambda_handler(event, context):
    """Main Lambda entry point - called by API Gateway."""
    try:
        body = json.loads(event.get("body", "{}"))
        logger.info(f"Request received: {body}")

        prompt = build_outfit_prompt(body)
        outfit_text = generate_outfit_text(prompt)
        image_url = generate_outfit_image(outfit_text)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "outfit_description": outfit_text,
                "image_url": image_url
            })
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
