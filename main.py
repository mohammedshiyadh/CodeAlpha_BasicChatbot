def welcome_message():
    print("=" * 30)
    print("       CODEALPHA CHATBOT")
    print("=" * 30)
    print("Hello! I am your friendly chatbot.")
    print("How can I assist you today?")
    print("Type 'bye' to exit.")
    print("-" * 30)


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"

    elif user_input == "how are you?":
        return "I'm just a program, but I'm functioning well! How about you?"

    elif user_input == "what is your name?":
        return "I am your friendly chatbot. Developed by Shiyadh."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand. Please try asking something else."


def chatbot():
    welcome_message()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    chatbot()
