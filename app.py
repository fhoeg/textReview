from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)
openai.api_key = api_key

def load_system():
    with open('system.txt', encoding='utf8') as f:
        global system_text
        system_text = f.read()
        # print(system_text)

def main():
    msgs = []
    load_system()
    # Get the chatbot type and name from the user
    system_msg = system_text
    msgs.append({"role": "system", "content": system_msg})
    
    chatbot_name = input("What would you like to name your chatbot?\n")

    print(f"Say hello to {chatbot_name}! Type 'quit()' when done.")
    
    # Main loop
    while True:
        msg = input("\033[94mYOU: \033[0m")  # Blue text
        msg = msg.strip()  # Remove extra whitespaces

        if msg.lower() == "quit()":
            break

        msgs.append({"role": "user", "content": msg})
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            temperature=0,
            messages=msgs
        )
        reply = response["choices"][0]["message"]["content"]
        msgs.append({"role": "assistant", "content": reply})
        print(f"\033[92m\n{chatbot_name}: {reply}\033[0m\n")  # Green text

if __name__ == "__main__":
    main()