def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm AI Chatbot!"
    elif user_input == "help":
        return "Try saying: hello, hi, how are you, what is your name, bye."
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

def run_chatbot():
    print("AI Chatbot!")
    print("Type something to begin. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    run_chatbot()
