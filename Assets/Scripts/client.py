import sys
import json
import requests

def send_question(prompt, id = 0):
    response = requests.post('http://127.0.0.1:5050/ask', json={'prompt': prompt, 'id': id})
    return response.json()

def tts(prompt):
    response = requests.post('http://127.0.0.1:5050/tts', json={'prompt': prompt})
    return response.json()

def generate_image(prompt):
    response = requests.post('http://127.0.0.1:5050/image', json={'prompt': prompt})
    return response.json()

def parse(prompt):
    response = requests.post('http://127.0.0.1:5050/parse', json={'prompt': prompt})
    return response.json()

if __name__ == "__main__":
    # first parameter is the question
    # read from the command line
    if len(sys.argv) < 2:
        # prompt = "```json\n{\n\"Title\": \"The Sword Master's Tale\",\n\"Characters\": [\"Caleb - The Sword Master\", \"Eva - Caleb's Daughter\", \"King Leonard\", \"Sir Ronald - King's Knight\", \"Lady Eleanor - King's Daughter\"],\n\"Acts\": [\n\t{\"act_title\": \"Act 1: The arrant knight\",\n \t \"scenes\": [\n\t {\"scene_index\": 1,\n\t  \"scene_title\": \"The Sword Master's Hut\",\n\t  \"stage_setting\": \"A quaint hut filled with swords, shields and armors. The ambiance is rustic.\",\n\t  \"involved_characters\": [\"Caleb - The Sword Master\", \"Eva - Caleb's Daughter\"],\n\t  \"plot\": \"Caleb, a retired but proud sword master, teaching his only daughter, Eva, the art of sword fighting.\"},\n\t  {\"scene_index\": 2,\n\t  \"scene_title\": \"The King's Announcement\",\n\t  \"stage_setting\": \"The Royal Palace of King Leonard. A grand hall filled with nobles.\",\n\t  \"involved_characters\": [\"King Leonard\"],\n\t  \"plot\": \"King Leonard announcing a tournament to find the new Captain of the Guard.\"},\n\t  {\"scene_index\": 3,\n\t  \"scene_title\": \"The Training Begins\",\n\t  \"stage_setting\": \"Back at the hut, a makeshift training ground in the forest.\",\n\t  \"involved_characters\": [\"Caleb - The Sword Master\", \"Eva - Caleb's Daughter\"],\n\t  \"plot\": \"Upon hearing the news, Caleb decides to train Eva for the tournament, aiming to make her the first female Captain of the Guard.\" }\n\t]\n},\n\t{\"act_title\": \"Act 2: The promise of a sword\",\n \t \"scenes\": [\n\t {\"scene_index\": 1,\n\t  \"scene_title\": \"The Rivalry Intensifies\",\n\t  \"stage_setting\": \"At the tournament ground. It's filled with energy, excitement, and anxiousness.\",\n\t  \"involved_characters\": [\"Eva - Caleb's Daughter\", \"Sir Ronald - King's Knight\", \"King Leonard\"],\n\t  \"plot\": \"Eva, under disguise, enters the tournament while Sir Ronald, a strong and intimidating knight, becomes her toughest competitor.\"},\n\t  {\"scene_index\": 2,\n\t  \"scene_title\": \"A Noble Encounter\",\n\t  \"stage_setting\": \"The Palace Gardens. A beautiful setting filled with blossoming flowers and a gentle stream.\",\n\t  \"involved_characters\": [\"Eva - Caleb's Daughter\", \"Lady Eleanor - King's Daughter\"],\n\t  \"plot\": \"Eva inadvertently meets Lady Eleanor, who becomes her confidante.\"},\n      {\"scene_index\": 3,\n\t  \"scene_title\": \"The Final Face-Off\",\n\t  \"stage_setting\": \"Back at the tournament ground. The crowd eagerly awaits the final match.\",\n\t  \"involved_characters\": [\"Eva - Caleb's Daughter\", \"Sir Ronald - King's Knight\"],\n\t  \"plot\": \"Eva and Sir Ronald make it to the finals and face off in a thrilling fight.\"}\n\t]\n},\n\t{\"act_title\": \"Act 3: Victory claimed\",\n \t \"scenes\": [\n\t {\"scene_index\": 1,\n\t  \"scene_title\": \"The Reveal and Victory\",\n\t  \"stage_setting\": \"The tournament ground. The crowd is stunned with the reveal of Eva's identity, and her victory.\",\n\t  \"involved_characters\": [\"Eva - Caleb's Daughter\", \"King Leonard\"],\n\t  \"plot\": \"Eva wins the tournament, reveals her true identity, and gets the acceptance of the King.\"},\n\t  {\"scene_index\": 2,\n\t  \"scene_title\": \"A Royal Proposal\",\n\t  \"stage_setting\": \"The Royal Palace. A private meeting of the King and Eva.\",\n\t  \"involved_characters\": [\"Eva - Caleb's Daughter\", \"King Leonard\"],\n\t  \"plot\": \"King Leonard, impressed with Eva, proposes to make her the Captain of the Guard.\"},\n\t   {\"scene_index\": 3,\n\t  \"scene_title\": \"A Proud Father\",\n\t  \"stage_setting\": \"The Sword Master's Hut. A proud and touching reunion.\",\n\t  \"involved_characters\": [\"Caleb - The Sword Master\", \"Eva - Caleb's Daughter\"],\n\t  \"plot\": \"Filled with Pride, Caleb welcomes his victorious Daughter who's now the first female Captain of the Guard.\"}\n\t  \n\t]\n}\n],\n\"Epilogue\": \"Eva makes history in the King's guard and paves the way for other women. Caleb, filled with immense pride, retires peacefully, knowing his daughter will continue his legacy.\"\n}\n```"
        # answer = send_question(prompt, 999)
        with open(f"Assets/Server/answer.json", 'r', encoding='utf-8') as file:
            temp = json.load(file)
        prompt = temp["answer"]
        print(prompt)
        answer = parse(prompt)
    elif sys.argv[1] == "ask":
        prompt = sys.argv[2]
        id = sys.argv[3]
        answer = send_question(prompt, id)
    elif sys.argv[1] == "tts":
        prompt = sys.argv[2]
        answer = tts(prompt)
    elif sys.argv[1] == "image":
        prompt = sys.argv[2]
        answer = generate_image(prompt)
    elif sys.argv[1] == "parse":
        with open(f"Assets/Server/answer.json", 'r', encoding='utf-8') as file:
            temp = json.load(file)
        prompt = temp["answer"]
        answer = parse(prompt)
    else:
        answer = "unknown task"

    print(answer)