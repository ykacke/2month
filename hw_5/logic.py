import random
from decouple import Config, Csv

config = Config()

lower = config.getint('gamer_conf', 'lower')
higher = config.getint('gamer_conf', 'higher')
initial_bet = config.getint('gamer_conf', 'player_bet')
max_guesses = config.getint('gamer_conf', 'guesses_made')

def start_game():
    secret_number = random.randint(lower, higher)
    capital = initial_bet
    guesses_made = 0

    print(f"Добро пожаловать в игру! У вас {capital} монет.")
    print(f"Загадываю число от {lower} до {higher}.")
    print(f"У вас {max_guesses} попыток, чтобы угадать число.")

    while guesses_made < max_guesses:
        try:
            bet = int(input(f"Ваша ставка: {capital}. Введите число от {lower} до {higher}: "))

            if bet < lower or bet > higher:
                print(f"Введите число в пределах от {lower} до {higher}.")
                continue

            if bet == secret_number:
                capital *= 2
                print(f"Вы угадали число! Ваш новый капитал: {capital}.")
                break
            else:
                capital -= 10
                print(f"Неправильно! Загаданное число больше или меньше вашего. Ваш капитал: {capital}.")
            guesses_made += 1
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            if guesses_made == max_guesses:
                print(f"У вас закончились попытки. Загаданное число было: {secret_number}. Ваш капитал: {capital}.")