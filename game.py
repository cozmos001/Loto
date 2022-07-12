from card import Card
from bag import Bag
from player import PlayerCPU, PlayerHuman
import random


# Функция для проверки на продолжение игры
# def check_contin(players):
#     for item in players:
#         if not (item.win is None):
#             return False
#     return True

# Универсальная функция для проверки на продолжения игры и определения победителя/проигравшего
def check_contin_win(players):
    for player in players:
        if player.win is True:
            for player in players:
                if player.win is None:
                    player.win = False
            return False
        elif player.win is False:
            for player in players:
                if player.win is None:
                    player.win = True
            return False
    return True


# Сколько человек играет?
count = int(input('Введите количество игроков: '))

# Создание игроков
players = []
cpu_count = 1
for player in range(count):
    nums = random.sample(range(1, 91), 15)
    # Кто играет компьютер или человек
    who = int(input('Кто играет компьютер/человек, 0/1: '))
    if who:
        name = input('Введите имя игрока: ')
        players.append(PlayerHuman(name, Card(nums)))
    else:
        players.append(PlayerCPU(f'CPU {cpu_count}', Card(nums)))
        cpu_count += 1

# Создание мешка
bag = Bag()

while check_contin_win(players):
    num = bag.choise()
    print(f'Новый боченок: {num} (осталось {len(bag)})')
    for player in players:
        print(player)
        print(player.card)
        if 'CPU' not in player.name:
            answer = input('Зачеркнуть? y/n: ')
            player.step(num, answer)
        else:
            player.step(num)

# Вывод победителя/проигравщего если используется универсальная функция
for player in players:
    if player.win is True:
        print(f'{player} Win')
    else:
        print(f'{player} Loos')

# Вывод победителя/проигравщего если используется просто функция для проверки на продолжение игры
# if True in [player.win for player in players]:
#     for player in players:
#         if player.win is True:
#             print(f'{player.name} Win')
#         else:
#             print(f'{player.name} Loos')
# else:
#     for player in players:
#         if player.win is False:
#             print(f'{player.name} Loos')
#         else:
#             print(f'{player.name} Win')
