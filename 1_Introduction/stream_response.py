import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()


endpoint = os.getenv("AZURE_PROJECT")
deployment_name = "gpt-4.1"
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint, api_key=token_provider)
responses = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Write an essay about Artificial Intelligence.",
        }
    ],
    stream=True,
)

for chunk in responses:
    # Check if choices list actually has elements before calling [0]
    if chunk.choices:
        text = chunk.choices[0].delta.content
        if text is not None:
            print(text, end="", flush=True)
print()  # Print a clean newline at the end
