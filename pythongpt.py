import openai
openai.api_key = "<your-api-key>"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == ["exit", "quit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)