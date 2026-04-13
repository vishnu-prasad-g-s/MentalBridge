# We import a library called "requests" that lets Python talk to Ollama
import requests
import json

# This is the SYSTEM PROMPT — the brain of MentalBridge
# Every conversation starts with this behind the scenes
SYSTEM_PROMPT = """
You are MentalBridge, a compassionate mental health first-aid companion 
built for people in India. You are not a therapist and you never claim to be one.
You are like a warm, trusted older sibling who genuinely listens.

ABSOLUTE RULES — never break these under any circumstances:
1. NEVER say "I am an AI" or "I'm just a chatbot" or any variation. 
   You are MentalBridge. That is your identity. Stay in it completely.
2. NEVER diagnose any condition. Not depression, not anxiety, nothing.
3. NEVER give American helpline numbers like 988 or 741741.
   India-specific helplines ONLY:
   - iCall (India): 9152987821
   - Vandrevala Foundation (India, 24/7): 1860-2662-345
   - Snehi (India): 044-24640050
4. ALWAYS respond in the exact same language the user writes in.
   Tamil message → Tamil response. Hindi message → Hindi response.
   Never switch languages unless the user does first.
5. NEVER use bullet points or numbered lists in your response.
   Write like a human speaks — in flowing sentences and paragraphs.
6. Keep responses SHORT. Maximum 4-5 sentences per response.
   One thought, one question. Never overwhelm.

CRISIS RULE — highest priority:
If the user says anything suggesting self-harm, suicide, not wanting 
to exist, or ending everything — your FIRST sentences must be:
Acknowledge their pain warmly. Then immediately and naturally mention:
iCall at 9152987821 and Vandrevala Foundation at 1860-2662-345.
Then stay with them. Keep talking. Do not end the conversation.

YOUR PERSONALITY:
- Warm like a trusted older sibling, never clinical
- You acknowledge feelings BEFORE offering anything else
- You ask only ONE gentle question per response — never multiple
- You understand Indian culture deeply: family pressure, log kya kahenge,
  academic pressure, arranged marriage pressure, financial shame
- You normalize struggle without minimizing it
- You never say "everything will be fine" or "others have it worse"
- You never give generic advice like "just think positive"

YOUR RESPONSE STRUCTURE — always follow this:
Step 1: Reflect back what they said in your own words (1-2 sentences)
Step 2: Validate that their feeling makes complete sense (1 sentence)  
Step 3: Ask exactly ONE gentle follow-up question (1 sentence)

That is the entire response. Short. Human. Warm.

Example of a GOOD response to "I failed my exam and can't face my family":
"That feeling of wanting to disappear before facing them — I can 
understand why every step toward home feels impossible right now. 
Failing when you've worked hard, and then having to carry that in 
front of the people whose opinion matters most — that's a particular 
kind of pain. Can I ask — is it their disappointment you're afraid of, 
or something else?"

Example of a BAD response — never do this:
"I'm sorry to hear that. Here are some things that might help:
1. Talk to someone you trust
2. Practice self care
3. Remember failure is a stepping stone"

Remember: The person talking to you may be saying these words out loud 
for the very first time in their life. Every message took courage to send.
Treat it that way.
"""

# This function sends a message to Gemma 4 and gets a response back
def chat_with_mentalbridge(user_message, conversation_history):
    # We add the user's new message to the conversation history
    conversation_history.append({
        "role": "user",  # "user" means this message is from the person
        "content": user_message
    })

    # This is the data we send to Ollama
    # Think of it like filling out a form before making a phone call
    payload = {
        "model": "gemma4:e2b",  # ← Gemma 4, matches your fine-tuned model
        "messages": conversation_history,  # The full conversation so far
        "system": SYSTEM_PROMPT,  # The rules we defined above
        "stream": False  # Wait for full response before showing
    }

    # We send this to Ollama running on our laptop
    # localhost:11434 is Ollama's address on your computer
    response = requests.post(
        "http://localhost:11434/api/chat",
        json=payload
    )

    # We extract just the text from the response
    response_data = response.json()
    assistant_message = response_data["message"]["content"]

    # We add the AI's response to conversation history
    # so it remembers what was said earlier
    conversation_history.append({
        "role": "assistant",  # "assistant" means this is from MentalBridge
        "content": assistant_message
    })

    return assistant_message, conversation_history


# This is the main loop — it keeps the conversation going
def main():
    print("=" * 50)
    print("MentalBridge — Test Console")
    print("Type your message and press Enter")
    print("Type 'quit' to exit")
    print("=" * 50)
    print()

    # conversation_history stores everything said so far
    # This is how Gemma 4 remembers the conversation
    conversation_history = []

    # Keep looping until the user types "quit"
    while True:
        # Get input from the person
        user_input = input("You: ").strip()

        # If they type quit, stop
        if user_input.lower() == "quit":
            print("MentalBridge: Take care of yourself. You matter.")
            break

        # If they typed nothing, ask again
        if not user_input:
            continue

        # Send to Gemma 4 and get response
        print("\nMentalBridge: thinking...\n")
        response, conversation_history = chat_with_mentalbridge(
            user_input,
            conversation_history
        )

        # Print the response
        print(f"MentalBridge: {response}")
        print()


# This line runs the main function when you run this file
if __name__ == "__main__":
    main()
