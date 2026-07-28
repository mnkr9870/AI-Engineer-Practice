from chatbotWrapper import chat_with_bot
# Initialize the conversation with the System Prompt
conversation_history = [
    {
        "role": "system",
        "content": "You are a polite customer support agent for a shoe company called SoleMates.",
    }
]

# Turn 1: User asks a question
user_input_1 = "Do you offer free shipping?"
conversation_history.append({"role": "user", "content": user_input_1})

# Get and store response
bot_response_1 = chat_with_bot(conversation_history)
print(f"Bot: {bot_response_1}")
conversation_history.append({"role": "assistant", "content": bot_response_1})

# Turn 2: User asks a follow-up (relies on memory)
user_input_2 = "What about returns on them?"
conversation_history.append({"role": "user", "content": user_input_2})

bot_response_2 = chat_with_bot(conversation_history)
print(f"Bot: {bot_response_2}")
