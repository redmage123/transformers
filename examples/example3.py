import openai
import os

# Set up API credentials
with open('/home/bbrelin/key.txt' as key:
          openai.api_key = key.readline().strip()

# Set up prompt and memory
prompt = "Once upon a time"
memory = "Once upon a time, there was a magical kingdom where unicorns roamed free."

# Generate continuation using the GPT-3 language model and memory attribute
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
    memory=memory,
    memory_token_length=10,
)

# Print the generated continuation
print(response.choices[0].text)

