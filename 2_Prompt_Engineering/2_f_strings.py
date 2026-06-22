import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

load_dotenv()

end_point = os.getenv("AZURE_PROJECT")
api_key = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=end_point, api_key=api_key)


def get_response(prompt, system_message="You are helpful assistant", temperature=0.7):
    """
    A foundational function to interact with OpenAI API
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1", messages=messages, temperature=temperature
    )

    return response.choices[0].message.content

user_review = "The battery life is terrible, but the screen is beautiful. Overall, I wouldn't buy it again."

# Using XML tags as delimiters
prompt = f"""
Summarize the sentiment of the following product review. 
Extract the primary positive and negative points.

<review>
{user_review}
</review>
"""

system = "You are a precise data extraction algorithm."
print(get_response(prompt, system_message=system, temperature=0.0))
