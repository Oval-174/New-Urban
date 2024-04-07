def draw_area():
    print('  1', '2', '3')
    for i in range(3):
        print(i + 1, *area[i])


def check_winner():
    # диагонали
    if [area[0][0], area[1][1], area[2][2]] == ['X', 'X', 'X']:
        return 'X'
    if [area[0][2], area[1][1], area[2][0]] == ['X', 'X', 'X']:
        return 'X'
    if [area[0][0], area[1][1], area[2][2]] == ['O', 'O', 'O']:
        return 'O'
    if [area[0][2], area[1][1], area[2][0]] == ['O', 'O', 'O']:
        return 'O'
    for i in range(3):
        # строки
        if area[i] == ['X', 'X', 'X']:
            return 'X'
        if area[i] == ['O', 'O', 'O']:
            return 'O'
        # столбцы
        if [area[0][i], area[1][i], area[2][i]] == ['X', 'X', 'X']:
            return 'X'
        if [area[0][i], area[1][i], area[2][i]] == ['O', 'O', 'O']:
            return 'O'
    return '*'


area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в игру крестики-нолики')
print('---------------------------------------')
draw_area()
turn = 1
turn_error = 0
while turn < 10:
    print('Ход №', turn)
    if (turn + turn_error) % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки  (1, 2 или 3): ')) - 1
    column = int(input('Введите номер столбца (1, 2 или 3): ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Поле ' + str(row) + ',' + str(column) + ' занято. Вы пропукаете ход!')
        draw_area()
        turn_error = turn_error + 1
        if turn_error > 3:
            print('Очень много ошибок!  Объявляется ничья!')
            break
        continue
    turn = turn + 1
    draw_area()
    if check_winner() == 'X':
        print('Победили крестики. Game over!')
        break
    if check_winner() == 'O':
        print('Победили нолики. Game over!')
        break
    if turn == 10 and check_winner() == '*':
        print('Победила дружба. Game over!')
        break
