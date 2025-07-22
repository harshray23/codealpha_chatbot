# chatbot.py
"""
TASK 4 – Basic Rule‑Based Chatbot (extended)
-------------------------------------------
• Handles >10 predefined user inputs
• Uses a simple if‑elif chain and functions
• Shows current date/time when asked
"""

from datetime import datetime


def get_reply(msg: str) -> str:
    """Return a canned response based on the exact user message."""
    msg = msg.lower().strip()

    # 1. Greetings
    if msg in ("hello", "hi", "hey", "yo"):
        return "Hi there! 👋"

    # 2. How‑are‑you
    elif msg in ("how are you", "how r u", "how are you doing"):
        return "I'm doing great, thanks for asking! 😊"

    # 3. Farewell
    elif msg in ("bye", "goodbye", "see you", "exit"):
        return "Goodbye! 👋"

    # 4. Name / identity
    elif msg in ("what's your name", "whats your name", "who are you"):
        return "I'm CodeAlphaBot, nice to meet you! 🤖"

    # 5. Thanks
    elif msg in ("thank you", "thanks", "thanks a lot"):
        return "You're welcome! 🙏"

    # 6. Joke
    elif msg in ("tell me a joke", "joke", "make me laugh"):
        return "Why don't programmers like nature? It has too many bugs. 🐛"

    # 7. Help / capabilities
    elif msg in ("help", "what can you do", "commands"):
        return (
            "I can greet you, tell jokes, show the date or time, "
            "and chat about a few simple things. 🤗"
        )

    # 8. Date
    elif msg in ("what day is it", "what's the date", "date"):
        today = datetime.now().strftime("%A, %d %b %Y")
        return f"Today is {today}."

    # 9. Time
    elif msg in ("what time is it", "time", "current time"):
        now = datetime.now().strftime("%I:%M %p").lstrip("0")
        return f"It's {now}."

    # 10. Weather (placeholder)
    elif msg in ("weather", "how's the weather"):
        return "Sorry, I can’t check live weather yet. 🌦️"

    # 11. Origin
    elif msg in ("where are you from", "your origin"):
        return "I'm a virtual assistant created for the Code Alpha internship tasks. 🚀"

    # 12. Anything else
    else:
        return "I'm not sure how to respond to that. 🤔"


def main() -> None:
    print("🤖  Welcome! I’m CodeAlphaBot. Type 'exit' anytime to quit.")
    while True:
        user = input("You: ")
        if user.lower().strip() == "exit":
            print("Bot: Bye! 👋")
            break

        reply = get_reply(user)
        print("Bot:", reply)


if __name__ == "__main__":
    main()
