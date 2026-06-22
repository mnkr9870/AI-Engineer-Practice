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

logic_puzzle = """
Roger has 5 tennis balls. He buys 2 more cans of tennis balls. 
Each can has 3 tennis balls. How many tennis balls does he have now?
"""

# Without CoT: The model might jump to the wrong math.
# With Zero-Shot CoT:
cot_prompt = logic_puzzle + "\nLet's think step by step."

print(get_response(cot_prompt, temperature=0.0))
