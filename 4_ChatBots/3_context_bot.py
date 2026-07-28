from chatbotWrapper import chat_with_bot

history_with_context = [
    {
        "role": "system",
        "content": "You are an IT helpdesk bot. Format your replies exactly like the examples.",
    },
    # Few-shot context injection
    {"role": "user", "content": "My screen is totally black."},
    {
        "role": "assistant",
        "content": "ACTION_REQUIRED: Check monitor power cable. TICKET_PRIORITY: Low.",
    },
    {
        "role": "user",
        "content": "The main database has crashed and the website is down!",
    },
    {
        "role": "assistant",
        "content": "ACTION_REQUIRED: Page the on-call DevOps engineer immediately. TICKET_PRIORITY: Critical.",
    },
    # Real query
    {"role": "user", "content": "I forgot my email password again."},
]

print(chat_with_bot(history_with_context, temperature=0.0))
# Expected Output: ACTION_REQUIRED: Send automated password reset link. TICKET_PRIORITY: Low.
