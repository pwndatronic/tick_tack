starting_field = [[' ', '0', '1', '2'],
                  ['0', '-', '-', '-'],
                  ['1', '-', '-', '-'],
                  ['2', '-', '-', '-']]

in_game_field = [['-' for x in range(3)] for y in range(3)]

print("\nДавайте сыграем в крестики нолики.\n\n"
      "Для того, чтоб ваш ход учелся, дайте ответ в виде числа,"
      "\nгде перва цифра отображает номер ряда, а вторая - столбика.\n")

def draw_field():
    for i in starting_field:
        print(' '.join(i))


def player_input(char):
    while True:
        player_in = input(f'\nХод {char}: ')
        if all([player_in.isdigit(),
                len(player_in) == 2,
                int(player_in) // 10 in range(3),
                int(player_in) % 10 in range(3)]):
            player_in = int(player_in)
            x = player_in // 10
            y = player_in % 10
            return x, y
        else:
            print("\nВы ввели неверный формат, попробуйте снова.")
            continue

def fill_the_boards(char):
    while True:
        x, y = player_input(char)
        if in_game_field[x][y] != '-':
            print("\nЭто поле уже занято, попробуйте снова.")
            continue
        else:
            in_game_field[x][y] = char
            starting_field[x + 1][y + 1] = char
        break

def win_condition(in_game_field):
    for x in in_game_field:
        if all([len(set(x)) == 1,
                list(set(x))[0] != '-']):
            return in_game_field
    if any([all([in_game_field[0][0] == in_game_field[1][0] == in_game_field[2][0], in_game_field[0][0] != '-']),
            all([in_game_field[0][1] == in_game_field[1][1] == in_game_field[2][1], in_game_field[0][1] != '-']),
            all([in_game_field[0][2] == in_game_field[1][2] == in_game_field[2][2], in_game_field[0][2] != '-']),
            all([in_game_field[0][0] == in_game_field[1][1] == in_game_field[2][2], in_game_field[0][0] != '-']),
            all([in_game_field[0][2] == in_game_field[1][1] == in_game_field[2][0], in_game_field[0][2] != '-'])]):
        return in_game_field
    else:
        return False

def lets_play():
    turn = 1
    while True:
        char = 'x' if (turn == 1 or turn % 2 != 0) else 'o'
        draw_field()
        fill_the_boards(char)
        print('\n')
        if turn > 4:
            if win_condition(in_game_field):
                draw_field()
                print(f"\nПобеда {char}!")
                break
        turn += 1
        if turn > 9:
            draw_field()
            print(f"\nНичья.")
            break

lets_play()