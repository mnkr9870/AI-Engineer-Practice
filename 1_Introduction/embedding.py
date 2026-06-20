import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()


endpoint = os.getenv("AZURE_PROJECT")
deployment_name = "text-embedding-3-small"
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

client = OpenAI(base_url=endpoint, api_key=token_provider)
responses = client.embeddings.create(
    model=deployment_name,
    input="Artificial Intelligence and integration strategies",
)

embedding_vector = responses.data[0].embedding
print(f"Vector Dimensions: {len(embedding_vector)}")
print(f"First 3 dimensions sample: {embedding_vector[:5]}")
