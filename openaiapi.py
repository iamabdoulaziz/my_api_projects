
from openai import OpenAI
from openaikey import OPENAI_KEY

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= OPENAI_KEY
)
"""
completion = client.chat.completions.create(

#  extra_headers={
#    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#  },
  model="openai/gpt-4o",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
#print(completion.choices[0].message.content)
print(completion)
"""

def get_completion(prompt, system_prompt = ""):
    messages = []
    if system_prompt != "":
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    messages.append(
        {"role": "user", "content": prompt}
    )
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=messages
        )
        text = completion.choices[0].message.content
        return text
    except Exception as e:
        print("OpenAi Exception: " + str(e))
    return None
#print(completion)
print(get_completion("Salut !"))

print("Pose moi toutes tes questions, pour stoper tape juste sur enter !")
while True:
    prompt = input("Prompt: ")
    print(get_completion(prompt))
    #condition to continue or not the loop
    if prompt == "":
        break
print("Bye")
