

from nim_engine_new import get_bunches, put_stones, is_game_over, take_from_bunch
from termcolor import cprint, colored


put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color="green")
    cprint(get_bunches(), color="green")
    if user_number == 1:
        cprint('Ход игрока {}'.format(user_number), color="blue")
        pos = input(colored('Откуда берем?', color="blue"))
        qua = input(colored('Сколько берем?', color="blue"))
    else:
        cprint('Ход игрока {}'.format(user_number), color="yellow")
        pos = input(colored('Откуда берем?', color="yellow"))
        qua = input(colored('Сколько берем?', color="yellow"))
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_game_over():
        break
    user_number = 2 if user_number == 1 else 1

cprint('Выиграл игрок номер {}'.format(user_number), color='red')
