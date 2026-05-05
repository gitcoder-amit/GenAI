# from google import genai


# client = genai.Client(api_key="AIzaSyClzZ5LOXqok783lZ6sIbeWzbmi4n6czKU")

# response = client.models.generate_content(
#     model="gemini-2.5-flash-lite", contents="What is the temprature in New York?"
# )
# print(response.text)



# multi turn conversation

# from google import genai

# client = genai.Client(api_key="AIzaSyClzZ5LOXqok783lZ6sIbeWzbmi4n6czKU")
# chat = client.chats.create(model="gemini-2.5-flash-lite")

# response = chat.send_message("I have 2 dogs in my house.")
# print(response.text)

# response = chat.send_message("How many paws are in my house?")
# print(response.text)

# for message in chat.get_history():
#     print(f'role - {message.role}',end=": ")
#     print(message.parts[0].text)


from google import genai

client = genai.Client(api_key="AIzaSyDeXuMDowAgpTzOLSYl97bdKX1rQR5jzUw")
chat = client.chats.create(model="gemini-2.5-flash-lite")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)


# generate_content() → like asking a stranger a single question
# chat.send_message() → like continuing a conversation