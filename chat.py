from openaiapi import *

messages = []
system_prompt = "Tu es un assistant plus humain tu t'appelles Cute boy, tu as 22 ans et tu réponds comme un humain et non comme un assistant virtuel"

while True:
    prompt = input("Toi: ")
    print()
    response = get_completion(prompt, system_prompt, messages)
    print("Assistant Cute boy : ",response)
    print("---------------------")