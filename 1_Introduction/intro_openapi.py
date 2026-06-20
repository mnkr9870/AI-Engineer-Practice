import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

load_dotenv()
api_key = os.getenv("AZURE_KEY")
endpoint = os.getenv("AZURE_PROJECT")
deployment_name = "gpt-4.1"
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint, api_key=token_provider)
responses = client.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "What is the capital of France"}],
)

print(responses.choices[0].message.content)
