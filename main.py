import openai

# set up the OpenAI API key
openai.api_key = 'YOUR API KEY'

# set up the OpenAI model ID
model_id = 'text-davinci-003'



# define a function to interact with ChatGPT
def chat_with_gpt(message):
    # generate a response message using the OpenAI API
    response = openai.Completion.create(
        engine=model_id,
        prompt=f'You: {message}\nChatGPT:',
        max_tokens=200
    ).choices[0].text.strip()
    # print the response message
    print(f'ChatGPT: {response}')

# start a loop to interact with ChatGPT
while True:
    # read a message from the user
    message = input('You: ')
    # exit the loop if the user enters 'quit'
    if message == 'quit':
        break
    # interact with ChatGPT
    chat_with_gpt(message)
