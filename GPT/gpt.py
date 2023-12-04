import requests

def sendQuestionPrivate(qContent:str):
    headers={
        "Authorization": "Bearer token",
        "Content-Type": "application/json"
    }
    data={
        "model": "pai-001-light-beta",
        "max_tokens": 100,
        "messages": [
            {"role": "user", "content": qContent}
        ]
    }
    try:
        response = requests.post(
            url="https://api.pawan.krd/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        print(response.json())
        return {"status": True, "data": response.json()['choices'][0]['message']['content']}
    except:
        return {"status": False, "data": None}