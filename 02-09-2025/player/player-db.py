import json
#list
players =[
    {'id':101,'name':'jaiswal'},
    {'id':102,'name':'gill'},
]
print(players)

#opening the file and write it close automaticly
with open('players.json','w') as file:
    json.dump(players,file)

#read from the json
with open('players.json','r') as reader:
    players_from_json = json.load(reader)
    print(players_from_json)