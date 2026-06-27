replies = {
    # Greetings
    "hi": "Hello! 👋",
    "hello": "Hi there! 😊",
    "hey": "Hey! How can I help you?",
    "good morning": "Good Morning! ☀️",
    "good afternoon": "Good Afternoon! 😊",
    "good evening": "Good Evening! 🌙",

    # Conversation
    "how are you": "I'm doing great! Thanks for asking.",
    "how's it going": "Everything is running perfectly.",
    "are you okay": "Absolutely! Ready to help.",

    # About Bot
    "what is your name": "My name is NInjaBot.",
    "who are you": "I am a Rule-Based AI Chatbot.",
    "who created you": "I was created by Abdullah Sheikh.",
    "what can you do": "I can answer simple questions using predefined rules.",

    # Programming
    "what is python": "Python is a high-level programming language.",
    "what is ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI that learns from data.",

    # Fun
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "another joke": "Why was Python so calm? Because it had no class issues. 😄",
    "quote": "Success is the sum of small efforts repeated daily.",
    "motivate me": "Discipline beats motivation.",

    # Appreciation
    "thanks": "You're welcome! 😊",
    "thank you": "Happy to help!",
    "thanks a lot": "Anytime!",

    # Compliments
    "good job": "Thank you! 😊",
    "awesome": "Glad you liked it!",
    "you are smart": "Thanks! I'm still learning.",

    # General
    "your favorite language": "Definitely Python! 🐍",
    "your favorite color": "Blue. 💙",
    "tell me something": "Learning never stops.",
    "who is your favorite programmer": "Every programmer who keeps learning.",

    # Help
    "help": """
Available Commands
------------------
• Greetings
• Ask my name
• Ask what I can do
• Ask about Python or AI
• Tell me a joke
• Get a motivational quote
• Ask for time/date
• Calculator
• Type exit to quit
""",

    # Farewell
    "bye": "Goodbye! Have a great day. 👋",
    "goodbye": "Take care! 😊",
    "exit": "Thanks for chatting with me!",
    "quit": "See you next time!"
}
                
    

print("====================\nNinjaBot, let's chat!\n====================")
status = True
while status:
    user = input("You:").strip().lower()
    found = False
    for keys, response in replies.items():
        if user in keys:
            print("Bot:", response)
            found = True
            if user in ("bye", "goodbye", "exit", "quit"):
                status = False
            break

    if not found:
        print("Bot: Sorry, I don't understand that. Please type 'help'.  ")



