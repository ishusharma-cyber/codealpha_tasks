
import random
from datetime import datetime

name = ""

greetings = ["hello", "hi", "hey"]
greet_responses = ["Hi!", "Hello!", "Hey there!"]

how_are_you_responses = [
    "I'm doing great!",
    "All good here.",
    "I'm fine, thanks!"
]

unknown_responses = [
    "I didn't understand that.",
    "Can you rephrase?",
    "Hmm... interesting."
]

while True:
    user = input("You: ").lower()

    if "bye" in user or "exit" in user:
        print("Bot: Goodbye! ")
        break

    elif any(word in user for word in greetings):
        print("Bot:", random.choice(greet_responses))

    elif "my name is" in user:
        name = user.split("my name is")[-1].strip()
        print(f"Bot: Nice to meet you, {name}!")

    elif "what is my name" in user:
        if name:
            print(f"Bot: Your name is {name}.")
        else:
            print("Bot: I don't know your name yet.")

    elif "how are you" in user:
        print("Bot:", random.choice(how_are_you_responses))

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "help" in user:
        print("Bot: You can ask me things like:")
        print("- Say hello")
        print("- Tell me your name")
        print("- Ask the time")
        print("- Ask how I am")

    else:
        print("Bot:", random.choice(unknown_responses))
