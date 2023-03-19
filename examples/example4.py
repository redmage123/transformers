import openai
with open ('/home/bbrelin/key.txt') as key:
    openai.api_key = key.readline().strip()

# Define the prompt for the GPT-3 model
prompt = "Please write a Python program that prints 'Hello World':\n"

# Use the OpenAI API to generate the program
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Extract the program from the response and execute it
program = response.choices[0].text.strip()
print(program)

exec(program)

