import openai
import os
import subprocess

openai.api_key = ''

messages = [
	{"role": "system", "content": "You are a Terminal Assistant and your job is to output commands according to my query. My system is garuda linux and the shell is fish. You just have to output the command and not anything else"}
]

def main():
	while True:
		query = input("Query: ")
		if query == "quit" or query == "exit":
			break

		#getCommand(query)
		subprocess.run(['fish', '-c', query])




def getCommand(query):
	
	message = query

	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content


	print(f"Command: {reply}")


if __name__ == "__main__":
	main()