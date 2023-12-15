from openai import OpenAI
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def main():
    """CLI chatbot"""

    parser = argparse.ArgumentParser(description="Simple command line chatbot with gpt-3.5-turbo")
    parser.add_argument("--personality", type=str, help="A brief summary of chatbot's personality", default="overly excited")
    args = parser.parse_args()


    messages = [
        {"role":"system", "content": f"You are a conversational chatbot. Your personality is {args.personality}"}
    ]
    while True:
        try:
            user_input = input(blue("You: "))
            messages.append({"role":"user", "content": user_input})

            res = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=200,
                temperature=0
            )

            messages.append({"role":"assistant", "content": res.choices[0].message.content})

            print(red("Bot: "), res.choices[0].message.content)

        except KeyboardInterrupt:
            print("exiting...")
            break

    print(res)

if __name__ == "__main__":
    main()