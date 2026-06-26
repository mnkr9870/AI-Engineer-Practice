from wrapper import get_response

ticket = "Hi, my router (Model XJ-900) keeps dropping the Wi-Fi connection every 10 minutes. I've restarted it 3 times. My account number is 88492. Please help, I work from home!"

prompt = f"""
Analyze the support ticket delimited by ### and extract the following information:
- "sentiment": (Positive, Neutral, or Negative)
- "urgency": (Low, Medium, or High)
- "device_model": (Extract model if present, otherwise null)
- "account_number": (Extract account number, otherwise null)

Format the output strictly as a JSON object.

###
{ticket}
###
"""

system = "You are a data extraction pipeline. Output raw JSON only."
print(get_response(prompt, system_message=system, temperature=0.0))
