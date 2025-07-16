import json
import os
import urllib.request
import base64

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

        instance_id = event['detail']['instance-id']
        state = event['detail']['state']
        region = event['region']

        payload = json.dumps({
            "detail": {
                "instance-id": instance_id,
                "state": state
            },
            "region": region
        }).encode("utf-8")

        url = os.environ['SN_URL']
        user = os.environ['SN_USER']
        pwd = os.environ['SN_PASS']
        credentials = f"{user}:{pwd}"
        encoded_credentials = base64.b64encode(credentials.encode("ascii")).decode("ascii")

        req = urllib.request.Request(
            url,
            data=payload,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Basic {encoded_credentials}"
            }
        )

        with urllib.request.urlopen(req) as response:
            status = response.status
            body = response.read().decode()
            print("ServiceNow response:", status, body)

        return {
            'statusCode': status,
            'body': body
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
