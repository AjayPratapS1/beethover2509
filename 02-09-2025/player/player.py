#list
players =[
    {'id':101,'name':'jaiswal'},
    {'id':102,'name':'gill'},
]
print(players)
print(type(players))
#tuple
player_tuple = [
    (101,'jaiswal'),
    (102,'gill')
]
print(type(player_tuple[0]))

#Dictionaries
player = {}
#player = dict()
player['id'] = 102
player['name'] = 'abhishek'

print(player)
print(type(player))

players.append(player)
print(players)

for player in players: #O(N)
    if player['id'] == 103:
        print(player)

players_dict = {101:players[0],102:players[1],103:players[2]}
print(players_dict[103])
print(players_dict[101])
print(players_dict[102])