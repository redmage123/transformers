import openai
import os

# Set up API credentials
with open('/home/bbrelin/key.txt') as key:
    openai.api_key = key.readline().strip()


# Set up prompt
prompt = "Write a short story about a robot that learns to love."

# Set max token length
max_tokens = 2048

# Split prompt into multiple smaller prompts
prompts = [prompt[i:i+max_tokens] for i in range(0, len(prompt), max_tokens)]

# Initialize output text variable
output_text = ""

# Generate text using the GPT-3 language model
for prompt in prompts:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output_text += response.choices[0].text

# Print the generated text
print(output_text)

