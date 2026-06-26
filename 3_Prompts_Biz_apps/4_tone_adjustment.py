from wrapper import get_response

raw_draft = "Hey, we are launching a new tier of our software next week. It costs $50/month and has better analytics. Buy it here."

prompt = f"""
Rewrite the following raw draft into a polished B2B email.
The tone should be formal, persuasive, and value-driven. 
Address the reader as a Chief Marketing Officer (CMO).

Draft: {raw_draft}
"""
print(get_response(prompt, temperature=0.6))
