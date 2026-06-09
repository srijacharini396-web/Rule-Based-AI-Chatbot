print("🤖 Welcome! I am a Rule-Based AI Chatbot.")
print("Type 'bye', 'exit', or 'quit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi there!")

    elif user_input == "hi":
        print("Bot: Hello!")

    elif user_input == "hey":
        print("Bot: Hey! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")