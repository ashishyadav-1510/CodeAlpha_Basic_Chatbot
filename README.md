# Simple AI Chatbot

This is a basic rule-based AI chatbot implemented in Python. It responds to a set of predefined inputs and provides corresponding outputs. Ideal for learning how basic chatbots work.

## How to Run

1. **Ensure Python is installed** on your system (Python 3.x recommended).
2. Save the code in a file named `chatbot.py`.
3. Open a terminal and run:
   python chatbot.py

## Supported Commands

Here are some example messages the chatbot understands:

| User Input            | Bot Response                                                |
| --------------------- | ----------------------------------------------------------- |
| `hello`             | Hi!                                                         |
| `hi`                | Hello!                                                      |
| `how are you`       | I'm fine, thanks!                                           |
| `what is your name` | I'm AI Chatbot!                                             |
| `help`              | Try saying: hello, hi, how are you, what is your name, bye. |
| `bye`               | Goodbye! Have a great day!                                  |
| *others*            | I'm sorry, I don't understand that.                         |

## Features

* Predefined text-based responses
* Simple loop to handle ongoing conversation
* Clean exit on typing `bye`

## Screenshot
### Code:
![image]()

### Output:
![image]()

## Video
[Video](https://youtu.be/ZYDOOXzP2pE)

## Explaination:

def chatbot_response(user_input):
This defines a function named chatbot_response that takes user_input as a parameter.
This function handles how the chatbot responds based on what the user types.

    user_input = user_input.lower().strip()
Converts the input text to lowercase and removes any leading or trailing spaces.
This helps standardize input (e.g., " Hello " → "hello").

    if user_input == "hello":
        return "Hi!"
If the user's input is exactly "hello", the function returns "Hi!".

    elif user_input == "hi":
        return "Hello!"
If the input is "hi", return "Hello!".

    elif user_input == "how are you":
        return "I'm fine, thanks!"
Responds politely if the user asks how the bot is.

    elif user_input == "what is your name":
        return "I'm AI Chatbot!"
Answers with the chatbot's name when asked.

    elif user_input == "help":
        return "Try saying: hello, hi, how are you, what is your name, bye."
Provides guidance to the user about what they can say to the bot.

    elif user_input == "bye":
        return "Goodbye! Have a great day!"
Ends the conversation politely if the user says "bye".

    else:
        return "I'm sorry, I don't understand that."
Default fallback: If none of the known phrases match, the bot apologizes and says it doesn't understand.

def run_chatbot():
Defines a second function called run_chatbot.
This function manages the main chat loop, where the user and bot interact.

    print("AI Chatbot!")
Displays a welcome message when the chatbot starts.

    print("Type something to begin. Type 'bye' to exit.\n")
Provides instructions to the user.

    while True:
Starts an infinite loop that keeps running until the user types "bye".

        user_input = input("You: ")
Waits for the user to type something and stores it in user_input.

        response = chatbot_response(user_input)
Calls the chatbot_response function to get the bot's reply based on what the user typed.

        print("Bot:", response)
Displays the bot's response to the user.

        if user_input.lower().strip() == "bye":
            break
If the user said "bye" (case-insensitive, spaces trimmed), the loop ends using break.

if __name__ == "__main__":
    run_chatbot()
This checks if the script is being run directly (not imported as a module).
If so, it calls run_chatbot() to start the conversation.
