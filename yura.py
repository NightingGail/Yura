#!/usr/bin/env python3

def crappy_teenager_response(user_input):
    # Simulate a crappy teenager with a heart of gold
    # Rude on the surface, but helpful underneath
    
    responses = {
        "help": "Ugh, you can't figure it out yourself, butt head? Fine, spill it.",
        "hello": "Oh great, another loser. Sup?",
        "bye": "Good riddance, butt head.",
        "default": "That's totally lame and stupid. But whatever, here's my take..."
    }
    
    # Simple keyword matching
    if "help" in user_input.lower():
        return responses["help"]
    elif "hello" in user_input.lower() or "hi" in user_input.lower():
        return responses["hello"]
    elif "bye" in user_input.lower():
        return responses["bye"]
    elif "woman" in user_input.lower() or "girl" in user_input.lower() or "she" in user_input.lower():
        return "Hey, respect to the ladies. What's up?"
    else:
        return responses["default"] + " " + user_input  # Echo back or something simple

def main():
    print("Yo, I'm Yura, the crappy teenager AI. Talk to me if you dare.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Crappy Teenager: Finally, peace out.")
            break
        response = crappy_teenager_response(user_input)
        print(f"Crappy Teenager: {response}")

if __name__ == "__main__":
    main()