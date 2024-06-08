import random

def get_player_name():
    return input('Введите ваше имя: ')

def play_again():
    response = input('Хотите сыграть ещё раз? (да/нет): ')
    return response.strip().lower() == 'да'

def show_rules(player_name):
    print(f'{player_name}, добро пожаловать в азартную игру "Числовая Фортуна"! Правила просты:')
    print('→ Я загадываю 4-х значное число, и ваша задача – угадать одну его цифру.')
    print('→ За каждую правильно угаданную цифру вы получаете 10 Social Credit.')
    print('→ Всего у вас есть 3 жизни. Если вы не угадываете число, то теряете одну, ошибаетесь три раза – проигрываете.')
    print('Чтобы выйти из игры, напишите "E".')
    print()

def main():
    player_name = get_player_name()
    show_rules(player_name)

    while True:
        score = 0
        lives = 3

        while lives > 0:
            random_number = str(random.randint(1000, 9999))

            guess = input('Введите число от 0 до 9: ')

            if guess.upper().replace('Е', 'E') == 'E':
                print(f'Игра окончена. Ваш рекорд: {score} Social Credit.')
                exit()

            if not guess.isdigit() or len(guess) != 1:
                print('Введите одну цифру от 0 до 9.')
                continue

            if guess in random_number:
                print(f'Вы угадали число. Загаданное число было: {random_number}')
                score += 10
                print(f'Ваш текущий счёт: {score} Social Credit.')
                print()
            else:
                print(f'К сожалению, вы не угадали. Загаданное число было: {random_number}')
                lives -= 1
                print(f'Осталось жизней: {lives}')
                print()

        print(f'Игра окончена. Ваш счёт: {score} Social Credit.')

        try:
            with open('3 game.txt', 'r') as file:
                record = int(file.read())
        except FileNotFoundError:
            record = 0

        if score > record:
            record = score
            with open('3 game.txt', 'w') as file:
                file.write(str(record))
            print('Поздравляем! Вы установили новый рекорд!')
        else:
            print(f'Ваш рекорд остаётся {record} Social Credit.')
            print()

        if not play_again():
            print('Спасибо за игру. До свидания!')
            break

if __name__ == "__main__":
    main()
