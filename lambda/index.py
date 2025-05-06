# lambda/index.py
import json
import urllib.request

def handler(event, context):
    body = json.loads(event['body'])
    message = body.get("message", "")

    data = json.dumps({"message": message}).encode("utf-8")
    req = urllib.request.Request(
        "https://2fbe-34-168-53-203.ngrok-free.app/predict",  # ← あなたの ngrok URL に変更する
        data=data,
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as res:
            res_body = res.read()
            res_data = json.loads(res_body)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": res_data["response"]})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
