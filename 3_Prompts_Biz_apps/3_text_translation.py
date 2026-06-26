from wrapper import get_response

marketing_copy = (
    "Our software knocks it out of the park! It's a game-changer for your team."
)


prompt = f"""
Translate the following English marketing copy into French.

Crucial Instruction: Do not translate the baseball idioms literally. Adapt the tone to sound professional, enthusiastic, and culturally appropriate for a corporate audience in Paris, France.

Copy: "{marketing_copy}"
"""
print(get_response(prompt, temperature=0.2))
