from wrapper import get_response

prompt = """
Write a Python function named `calculate_discount`.
The function should take two arguments: `price` (float) and `discount_percentage` (float).
It should return the final price after the discount.
Include type hinting and a docstring.
Do not include any explanations, output only the Python code.
"""

system = "You are a senior Python developer."
print(get_response(prompt, system_message=system, temperature=0.0))
