from openai import OpenAI

import os
import subprocess


client = OpenAI(api_key='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')

messages = [
	{"role": "system", "content": "You are a Terminal Assistant and your job is to output commands according to my query. My system is garuda linux and the shell is fish. You just have to output the command and not anything else"}
]

def main():
	while True:
		query = input("Query: ")
		if query == "quit" or query == "exit":
			break

		query = query + "output commands only"
			
		command = getCommand(query)

		x = input('y or n: ')

		if x == 'y':
			subprocess.run(['fish', '-c', command])
		

def getCommand(query):
	
	message = query

	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
	reply = chat.choices[0].message.content


	print(f"Command: {reply}")

	return reply


if __name__ == "__main__":
	main()