# CodeAlpha Basic Chatbot

A beginner-friendly, rule-based chatbot built with Python as part of the
CodeAlpha Python Internship.

## Project Overview

This chatbot interacts with users through the command line. It
recognizes a small set of predefined messages and responds with
predefined replies using Python conditional statements and functions.

## Features

-   Displays a welcome message when the chatbot starts.
-   Accepts messages from the user through the terminal.
-   Recognizes greetings such as `hi`, `hello`, and `hey`.
-   Responds to `how are you?` and `what is your name?`.
-   Handles unrecognized messages with a default response.
-   Accepts `bye`, `exit`, or `quit` to end the conversation.
-   Handles uppercase and lowercase input.
-   Removes leading and trailing whitespace from messages.

## Technologies Used

-   Python 3
-   Python built-in functions and string methods

No external Python packages are required.

## Project Structure

``` text
CodeAlpha_BasicChatbot/
└── main.py
```

## Requirements

-   Python 3 installed on your computer.
-   A terminal or code editor such as Visual Studio Code.

## How to Run

1.  Clone or download this repository.
2.  Open the project folder in a terminal.
3.  Run the following command:

``` bash
python main.py
```

On some systems, you may need to use:

``` bash
python3 main.py
```

## Example Interaction

``` text
==============================
       CODEALPHA CHATBOT
==============================
Hello! I am your friendly chatbot.
How can I assist you today?
Type 'bye' to exit.
------------------------------
You: hello
Chatbot: Hello! How can I assist you today?
You: how are you?
Chatbot: I'm just a program, but I'm functioning well! How about you?
You: what is your name?
Chatbot: I am your friendly chatbot. Developed by Shiyadh.
You: something else
Chatbot: Sorry, I don't understand. Please try asking something else.
You: bye
Chatbot: Goodbye! Have a great day!
```

## Python Concepts Practiced

-   Functions (`def`)
-   While loops
-   Conditional statements (`if`, `elif`, `else`)
-   User input and console output (`input()` and `print()`)
-   String methods (`lower()` and `strip()`)
-   Returning values from functions (`return`)
-   Loop control (`break`)
-   Main-module execution guard (`if __name__ == "__main__"`)

## Limitations

This is a simple rule-based chatbot. It does not use artificial
intelligence, machine learning, or a language model. It can only respond
to the messages explicitly defined in its code.

## Internship Task

This project was developed for **Task 4: Basic Chatbot** under the
CodeAlpha Python Internship.

## Author

**Mohammed Shiyadh**
