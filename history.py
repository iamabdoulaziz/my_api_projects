
from openaiapi import *
from jinja2 import Template


messages = []
system_prompt = ("Tu es créateur d'histoires pour enfants, Tu crées des histoires simples, drôles et captivantes aui sont intéractives"
                 "A chaque fois tu vas proposer un court paragraphe qui fait avancer l'histoire et qui doit deboucher sur un choix multiples"
                 "Tu poseras systématiquement une question à l'utilisateur avec 3 choix : a, b ou c, ce qui déterminera le prochain paragraphe de l'histoire"
                 "Tout au début de la conversation, propose 5 thèmes pour l'histoire et l'utilisateur choisira entre 1 et 5."
                 "A tout moment propose aussi une option 'x' pour arrêter l'histoire")
response = get_completion("", system_prompt, messages)
print(response)
print()

def get_story_text():
    return get_completion("Rédige moi maintenant tout le texte de l'histoire sans intéractivité, redige le texte uniquement dit pas quoi que ce soit, redige "
                          "uniquement le texte de l'histoire sans intéractivité, redige paragraphe par paaragraphe", "", messages)


def get_story_infos(story_text):
    prompt = ("Génère moi un titre pour l'histoire, génere uniquement le titre de l'histoire sans commetaire ni rien d'autre. voici l'histoire" + story_text)
    response = get_completion(prompt)
    return response
def generate_html_page(story_title, story_text):
    template_code = ""
    with open("template.html", "r", encoding="utf-8") as file:
        template_code = file.read()
    template = Template(template_code)

    context = {
        "title": story_title,
        "text": story_text
    }
    html = template.render(context)
    with open("histoire.html", "w", encoding="utf-8") as file:
        file.write(html)

while True:
    prompt = input("Toi: ")
    if prompt == "x":
        break
    print()
    response = get_completion(prompt, system_prompt, messages)
    print("Assistant Cute boy : ",response)
    print()

response = get_completion("L'histoire est terminée. Rédige le dernier paragraphe pour terminer l'histoire.", system_prompt, messages)
print(response)


text = get_story_text()
title = get_story_infos(text)

with open("story.txt", "w") as file:
    file.write(f"Titre : {title}\n")
    file.write(text)

generate_html_page(title, text)
