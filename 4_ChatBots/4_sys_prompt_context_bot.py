from chatbotWrapper import chat_with_bot

company_faq = """
--- FAQ ---
Q: What are your holiday hours?
A: We are open 9AM-2PM on Christmas Eve, and closed on Christmas Day.

Q: Do you validate parking?
A: Yes, we validate parking for the Main Street Garage only.
--- END FAQ ---
"""

system_prompt = f"""
You are a helpful receptionist. 
Answer user questions using ONLY the information provided in the FAQ below.
If the answer is not in the FAQ, say "I don't have that information, please call the front desk."

{company_faq}
"""

convo = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Can I park in the alleyway behind the store?"},
]

print(chat_with_bot(convo, temperature=0.0))
# Expected Output: "I don't have that information, please call the front desk." (Because alleyway parking is not in the FAQ).
