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


def get_few_shot_response(user_query):
    messages = [
        {
            "role": "system",
            "content": "You convert dates from various formats into a strict ISO 8601 format (YYYY-MM-DD).",
        },
        # Example 1
        {"role": "user", "content": "I was born on the fifth of November, 1990."},
        {"role": "assistant", "content": "1990-11-05"},
        # Example 2
        {"role": "user", "content": "Deadline is Oct 31st 2024."},
        {"role": "assistant", "content": "2024-10-31"},
        # Actual Query
        {"role": "user", "content": user_query},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1", messages=messages, temperature=0.7
    )
    return response.choices[0].message.content


print(get_few_shot_response("The event is on Jan 2nd '25."))
# Expected Output: 2025-01-02


print(get_few_shot_response("The event is on Nov 2nd '26."))
# Expected Output: 2026-11-02
