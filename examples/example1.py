import openai
import os

# Set up API credentials
with open("/home/bbrelin/key.txt") as key:
    openai.api_key = key.readline().strip()

# Set up prompt
prompt = "Write a short story about a robot that learns to love."

# Generate text using the GPT-3 language model
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
print(response.choices[0].text)
