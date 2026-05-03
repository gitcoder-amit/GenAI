import os
from google import genai
from google.genai import types

# Example Functions

def add_numbers(x: int, y: int) -> int:
    """Returns the sum of two numbers."""
    print(f"Tool Call: add_numbers(x={x}, y={y})")
    result = x + y
    print(f"Tool Response: {result}")
    return result

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    print(f"Tool Call: is_prime(n={n})")
    if n <= 1:
        result = False
    else:
        result = all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    print(f"Tool Response: {result}")
    return result

def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client(api_key="AIzaSyAa61fFQhgZbJf3qBY2LqR4UR4X5ugrpsY")
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature, add_numbers, is_prime],
    system_instruction="You are a AI agent. YOu can use tools to answer user queries. Always try to use tools when appropriate. If user asks general questions, answer them directly. If user asks specific questions that require tools, use the tools to get the answer. Always try to use tools when appropriate.",
)

system_prompt = "You are a helpful assistant that can provide weather forecasts and control the thermostat. You can call the following tools: get_weather_forecast(location), set_thermostat_temperature(temperature), sum and is_prime."

chat = client.chats.create(
    model="gemini-2.5-flash",
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
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    response = chat.send_message(user_input)
    if response.function_calls:
        print(response.function_calls[0])
    print("Bot:", response.text)

# Print the final, user-facing response
print(response.text)