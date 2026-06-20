import os,json
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential,get_bearer_token_provider

load_dotenv()

endpoint = os.getenv("AZURE_PROJECT")
api_key = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)
deployment_name = "gpt-4.1"

client = OpenAI(api_key=api_key,base_url=endpoint)

def get_stock_price(ticker):
    if ticker == "MSFT":
        return {"price":450.50, "currency":"USD"}
    return {"price":"unknown"}

tools = [{
    "type":"function",
    "function":{
        "name":"get_stock_price",
        "description": "Get the current stock price of a given ticker.",
        "parameters":{
            "type":"object",
            "properties":{
                "ticker":{"type":"string","description":"The stock ticker, e.g. AAPL, MSFT"}
            },
            "required":["ticker"]
        }
    }
}]

messages = [{
    "role":"user",
    "content":"How much is Microsoft stock right now?"
}]

response = client.chat.completions.create(
    model = deployment_name,
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

response_message = response.choices[0].message

if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]
    function_args = json.loads(tool_call.function.arguments)

    function_result = get_stock_price(ticker=function_args.get("ticker"))

    messages.append(response_message)
    messages.append({
        "role":"tool",
        "tool_call_id":tool_call.id,
        "name":"get_stock_price",
        "content":json.dumps(function_result)
    })

    final_response = client.chat.completions.create(
        model=deployment_name,
        messages=messages
    )

    print(final_response.choices[0].message.content)
