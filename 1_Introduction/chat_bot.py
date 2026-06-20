import os
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_PROJECT")
deployment_model = "gpt-4.1"

token = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint, api_key=token)

chat_history = [
    {
        "role": "system",
        "content": "You are an helpful assistant who provides details and one-liner about the places requested.",
    }
]

while True:
    prompt = input("You:")
    if prompt.lower() == "quit":
        break
    chat_history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=deployment_model, messages=chat_history
    )
    ai_res = response.choices[0].message.content
    print(f"AI:{ai_res}")
    chat_history.append({"role": "assistant", "content": ai_res})
