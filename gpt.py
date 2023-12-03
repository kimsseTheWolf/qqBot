from openai import OpenAI
import requests

GPTClient = OpenAI(api_key="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")

def sendQuestion(qContent:str):
    response = GPTClient.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": qContent}
    ])
    print(response)
    return response['choices'][0]['message']['content']

def sendQuestionPrivate(qContent:str):
    headers={
        "Authorization": "Bearer pk-vUsOacudLYuZBALAzchjdeLVmapqoriSghvWjsNcEkjElBjP",
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