import json

filename = 'user_setting.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
player_1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'awards': ['SA', 'DS', 'FD']
}

player_2 = {
    'PlayerName': 'Egor',
    'Score': 346,
    'awards': ['DD', 'QQ', 'FF']

}

my_players = []
my_players.append(player_1)
my_players.append(player_2)

# --------------- SAVE by JSON ---------------

json.dump(my_players, myfile) # сохранили в джейсон. джейсон сохранить
myfile.close()

# TODO Выше все сделано чтобы сохранить в файл данные в формате джейсон.
# TODO А теперь мы хотим прочитать все что там есть

# ---------------- LOAD by Json ---------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile) # читаем из myfile и засунет в json_data и будет равна массиву my_players

for user in json_data:
    print('Player name is: ' + str(user['PlayerName'])) # вызываем ключ. все читается как обьект и поэтому в строку конвертируем. потому что мы используем это как текст
    print('Player score is: ' + str(user['Score']))
    print('Player awards: ' + str(user['awards'][0]))
    print('Player awards: ' + str(user['awards'][1]))
    print('Player awards: ' + str(user['awards'][2]))
    print('-------------------\n\n')