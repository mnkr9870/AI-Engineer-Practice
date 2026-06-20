import os, json
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

endpoint = os.getenv("AZURE_PROJECT")
api_key = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)


client = OpenAI(api_key=api_key, base_url=endpoint)

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What details can you extract from this design?",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://waz.smartdraw.com/uml-diagram/img/activity-diagram-example.png?bn=2606171427",
                        "detail": "high",  # Controls token cost processing adjustments
                    },
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
