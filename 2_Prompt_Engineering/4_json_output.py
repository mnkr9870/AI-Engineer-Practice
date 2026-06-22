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

text_data = "John Doe is 28 years old and works as a Software Engineer in New York."

prompt = f"""
Extract the information from the text into a JSON object.
Use the following keys: "name", "age", "profession", "city".

Text: {text_data}
"""

system = "You are an API that only returns valid JSON. Never return markdown formatting or conversational text."
# Setting temperature to 0 is crucial for predictable formatting
print(get_response(prompt, system_message=system, temperature=0.0))
