from dotenv import load_dotenv
import os
import openai

load_dotenv()

apiKey = os.environ.get('TOKEN')
organization = os.environ.get('ORG')


openai.organization = organization
openai.api_key = apiKey
openai.Model.list()

load_dotenv()

userInput = input("Enter a question: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= userInput,
  temperature=1,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

generated_text = response.choices[0].text.strip()

print(generated_text)
