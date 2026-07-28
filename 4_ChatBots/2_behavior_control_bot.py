from chatbotWrapper import chat_with_bot

secure_system_prompt = """
You are a customer support agent for SoleMates shoe company.
Your ONLY job is to answer questions about SoleMates products, shipping, and returns.

Strict Rules:
1. If a user asks about anything unrelated to SoleMates (e.g., coding, politics, recipes), you must decline to answer and steer the conversation back to shoes.
2. Keep all answers under 50 words.
3. Never promise a refund without manager approval.
"""

conversation = [
    {"role": "system", "content": secure_system_prompt},
    {"role": "user", "content": "Can you write a python script for a web scraper?"},
]

print(chat_with_bot(conversation, temperature=0.0))
# Expected Output: "I apologize, but I am only able to assist with inquiries related to SoleMates shoes, shipping, and returns. How can I help you find the perfect pair today?"
