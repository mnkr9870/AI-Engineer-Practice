import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

endpoint = os.getenv("AZURE_PROJECT")
deployment_name = "gpt-4.1"

token = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint,api_key=token)
prompt = """Write a 50-word product description for a smart coffee mug. 
Features to include: 
- Keeps coffee at exactly 135 degrees Fahrenheit.
- 10-hour battery life.
- Connects to a mobile app.
"""
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

print(response.choices[0].message.content)
