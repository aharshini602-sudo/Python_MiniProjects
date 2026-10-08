print("======================================")
print("           PYTHON CHATBOT")
print("======================================")

name = input("Bot: Hi! What is your name?\nYou: ")

print("Bot: Nice to meet you, " + name + "!")
print("Bot: How are you today?")

while True:

    user = input(name + ": ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello", name + "!")
        print("Bot: How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great!")
        print("Bot: Thanks for asking. How about you?")

    elif user == "good" or user == "fine":
        print("Bot: That's great to hear!")

    elif user == "what is your name":
        print("Bot: My name is PyBot.")
        print("Bot: I am a simple Python chatbot.")

    elif user == "what can you do":
        print("Bot: I can have a simple conversation with you.")
        print("Bot: I can also answer some basic questions.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "i am learning python":
        print("Bot: That's awesome!")
        print("Bot: Python is a great language for beginners.")

    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: It was nice talking with you, " + name + "!")
        print("Bot: Have a great day!")
        break

    else:
        print("Bot: Hmm... I don't understand that yet.")
        print("Bot: Try saying hello, how are you, or what can you do.")

print("\n======================================")
print("          CHAT ENDED")
print("======================================")