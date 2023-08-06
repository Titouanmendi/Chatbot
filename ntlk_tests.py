import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

conversation_samples = [
    ("Hi", "Hello! How can I help you today?"),
    ("What's your name?", "I'm a friendly chatbot."),
    ("How are you?", "I'm doing well, thank you! How about you?"),
    ("Tell me a joke", "Sure, here's one: Why don’t scientists trust atoms? Because they make up everything!"),
    ("Goodbye", "Goodbye! Have a great day!")
]

def chatbot_response(user_input):
    chat_pairs = Chat(conversation_samples, reflections)
    response = chat_pairs.respond(user_input)
    return response

def main():
    print("Chatbot: Hi! I'm a friendly chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
