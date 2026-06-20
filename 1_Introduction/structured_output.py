import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential,get_bearer_token_provider
from pydantic import BaseModel,Field
load_dotenv()
class User(BaseModel):
    name : str
    age : int
    programming_languages : list[str] = Field(description="List of programming languages")


endpoint = os.getenv("AZURE_PROJECT")
deployment_name = "gpt-4.1"
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint, api_key=token_provider)
responses = client.chat.completions.parse(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Extract data: Alex is a 28-year-old developer fluent in Python and Go.",
        }
    ],
    response_format=User
)

profile = responses.choices[0].message.parsed
print(profile.name)
print(profile.age)
print(profile.programming_languages)
