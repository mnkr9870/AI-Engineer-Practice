from wrapper import get_response

product_idea = "A smart coffee mug that keeps coffee exactly at 135 degrees Fahrenheit and charges wirelessly."

prompt = f"""
Write a compelling product description for the following item: {product_idea}

Requirements:
* Write a catchy headline.
* Write a one-paragraph emotional hook targeting busy professionals.
* List 3 key benefits (not just features).
"""

system = "You are an expert e-commerce copywriter."
print(get_response(prompt, system_message=system, temperature=0.7))
