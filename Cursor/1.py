import os
from google import genai
from google.genai import types
import subprocess

# plateform = os.name
# ALLOWED_COMMANDS = ["ls", "pwd", "whoami"]

import subprocess

def run_command(cmd: str):
    result = subprocess.run(
        cmd,
        shell=True,              # required for string commands
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr

client = genai.Client(api_key="AIzaSyCJxN9Mt4zaJqx0B1pqwNx69_Lc2T54uyU")
config = types.GenerateContentConfig(
    tools=[run_command],
    system_instruction='''You are a website builder expert, You have to create the frontend of the website by analysing user input. You have access of tool which can execute any shell or terminal command.
    Current User Operating system is MAC. Give command to user according to Operating system. 
    <-- What is your job -->
    1. Analyse user input and see what type of website user wants to create.
    2. Give the command once by one, step by step
    3. Use available tool `run_command` to execute the command.
    
    // Now you can give them command as following
    
    1. First create the folder Ex: mkdir "calculator"
    2. inside the folder create index.html, style.css and script.js file one by one Ex: "touch index.html", "touch style.css", "touch script.js"
    3. Write the code of index.html, 
    4 write code for style.css make sure it is correct and working
    5 Write code for  script.js
       Based on user input. If user wants to create a portfolio website then write code accordingly, if user wants to create a blog website then write code accordingly. and make sure things are working correctly it should not happend  like some cicks are not working or image is not there. Always try to give correct and working code.: 
    4. Provide terminal command to the user, they will directly execute it''',
)

system_prompt = "You are a helpful assistant that can provide weather forecasts and control the thermostat. You can call the following tools: get_weather_forecast(location), set_thermostat_temperature(temperature), sum and is_prime."

chat = client.chats.create(
    model="gemini-3.1-flash-lite-preview",
    config=config,
    history=[
        {
            "role": "model",
            "parts": [{"text": system_prompt}]
        }
    ]
    )


# Make the request
while True:
    user_input = input("I am a Cursor, Let's Create a website ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    response = chat.send_message(user_input)
    if response.function_calls:
        print(response.function_calls[0])
    print("Bot:", response.text)

# Print the final, user-facing response
print(response.text)