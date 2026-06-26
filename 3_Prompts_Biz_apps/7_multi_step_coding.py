from wrapper import get_response

legacy_code = """
def get_user(id):
    # connects to db
    user = db.query("SELECT * FROM users WHERE id = " + id)
    return user
"""

prompt = f"""
Review and modify the provided Python code by following these steps:

Step 1: Identify the critical security vulnerability (SQL Injection).
Step 2: Rewrite the function to use parameterized queries to fix the vulnerability.
Step 3: Add basic `try/except` error handling.

Code:
{legacy_code}
"""
print(get_response(prompt, temperature=0.0))
