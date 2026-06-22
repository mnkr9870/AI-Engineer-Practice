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


def route_inquiry(customer_message):
    prompt = f"""
    Analyze the customer message delimited by ###.
    
    Step 1: Determine if the message is a "Complaint", "Question", or "Praise".
    Step 2: If it is a "Complaint", output "URGENT_QUEUE".
    Step 3: If it is a "Question" or "Praise", output "STANDARD_QUEUE".
    
    ###
    {customer_message}
    ###
    
    Output ONLY the queue name.
    """
    return get_response(prompt, temperature=0.0)


print(route_inquiry("My package never arrived and I want a refund now!"))
# Expected Output: URGENT_QUEUE

print(route_inquiry("My package has arrive in time and I am happy with the product!"))
# Expected Output: STANDARD_QUEUE
