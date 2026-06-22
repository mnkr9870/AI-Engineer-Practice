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


multi_step_prompt = """
Please plan a 3-day itinerary for Tokyo by following these steps strictly in order:

Step 1 - Area Selection: Choose a specific neighborhood in Tokyo suitable for a first-time visitor and explain why in one sentence.
Step 2 - Accommodation: Recommend one mid-range hotel in that specific neighborhood.
Step 3 - Itinerary: Create a bulleted list of 2 activities per day, ensuring they are geographically close to the hotel chosen in Step 2.
Step 4 - Budget: Provide a rough estimated daily cost in USD for the activities listed.

Output your response clearly divided by these step numbers.
"""
print(get_response(multi_step_prompt, temperature=0.5))
