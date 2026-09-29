# Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

# Chat starts
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Chatbot:", response)

    if user.lower() == "bye":
        break
