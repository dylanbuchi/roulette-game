from random import randrange
from math import ceil
from time import sleep
from sys import exit
from os import system
from termcolor import colored


def deposit(minimum=10):
    user_bank = -1

    while user_bank < minimum:
        try:
            print(f"Welcome to the {colored('BiiigCasino', 'cyan')} :)")
            print(
                f"please deposit a minimum of {colored(f'{minimum:,}$','green')} to play"
            )
            user_bank = int(input())
            assert user_bank >= minimum

        except ValueError:
            print(colored("You didn't enter a valid number'", 'red'))

        except AssertionError:
            print(
                colored(
                    f"The minimum deposit is {colored(f'{minimum:,}$','green')}",
                    'red'))
    else:
        print(
            f"Your account has been credited with {colored(f'{user_bank:,}$','green')} Good Luck!"
        )
    return user_bank


def ask_for_bonus(bonus_amount):
    while True:
        bonus_answer = input(
            f"We offer you {colored(f'{bonus_amount:,}$','green')} with our Welcome bonus package!\n\
accept or decline this {colored('exclusive', 'cyan')} one time only offer! (y/n)"
        ).lower()
        try:
            if (bonus_answer == 'y'):
                print("Bonus activated!\n")
                return bonus_amount
            elif (bonus_answer == 'n'):
                print("Bonus declined")
                return 0
            else:
                raise ValueError
        except ValueError:
            print('Please type "y" or "n"')


def add_gains_to_(user_bank, amount):
    user_bank += amount
    return user_bank


def check_number_color(number):
    if (number == 0):
        return 'green'
    return number_is_odd(number)


def number_is_odd(number):
    return number % 2 != 0


def number_is_even(number):
    return not number_is_odd(number)


def get_number_color(number):
    colors = {True: 'red', False: 'yellow', 'green': 'green'}
    return colors[check_number_color(number)]


def play_roulette_game(user_bank, minimum_bet=10):
    roulette_number = randrange(37)
    user_bet = user_number = 0
    flag = False

    while True:
        try:
            if not flag:
                print_balance(user_bank)
                user_bet = int(input("Now place your bet: "))
                if (user_bet > user_bank):
                    print(
                        colored("You can't bet more than your balance", 'red'))

                elif user_bet < minimum_bet:
                    print(
                        f"The minimum bet for this game is {colored(f'{minimum_bet:,}$', 'green')}"
                    )
                else:
                    flag = True
                continue

            user_number = int(
                input(
                    f"Choose a number between {colored('(0-36)', 'cyan')}: \n")
            )
            assert 0 <= user_number <= 49

        except AssertionError:
            print(colored("Please choose a number between (0-36)", 'red'))
            continue
        except ValueError:
            print(colored("Please enter a valid integer", 'red'))
            continue
        else:
            break
    roulette_number_color = get_number_color(roulette_number)
    user_color = get_number_color(user_number)

    print("Waiting for the roulette to stop...\n")
    sleep(2)
    print(
        f"...and it stopped on number {colored(roulette_number, roulette_number_color.lower())} !!\n"
    )
    sleep(1)
    print(f"your number was {colored(user_number, user_color.lower())}\n")

    winnings = ceil(user_bet // 2)

    if user_number == roulette_number:
        print('Big Win! You guessed the winning number!')
        winnings = user_bet * 3

        print(f'+{colored(f"{winnings}$", "green")}')
        user_bank += winnings

    elif user_number != 0 and number_is_odd(roulette_number) and number_is_odd(user_number) or \
        user_number != 0 and number_is_even(roulette_number) and number_is_even(user_number):
        if (user_color == 'yellow'):
            user_color = 'black'

        print(
            f'Congratulations! Your number was {colored(user_color.upper(), get_number_color(user_number))}'
        )
        print(f'+{colored(f"{winnings}$", "green")}')
        user_bank += winnings

    else:
        print(
            f'Sorry! Better luck next time! -{colored(f"{user_bet}$", "red")}\n'
        )
        user_bank -= user_bet

    return user_bank


def print_balance(user_bank):
    print(f'Your balance: {colored(f"{user_bank:,}$", "green")}')


def check_welcome_bonus(claimed_bonus):
    bonus_amount = 0

    if not claimed_bonus:
        bonus_amount = ask_for_bonus(45)

    return bonus_amount


def user_interface():
    claimed_bonus = False
    user_bank = deposit()
    minimum_bet = 10
    print_balance(user_bank)

    while True:
        bonus_amount = check_welcome_bonus(claimed_bonus)
        if bonus_amount:
            claimed_bonus = True
            user_bank += bonus_amount

        user_bank = play_roulette_game(user_bank)

        if (user_bank <= minimum_bet):
            print_balance(user_bank)
            print(
                f"Not enough money to play, deposit at least {colored(f'{minimum_bet}$', 'green')} and come back later"
            )
            exit()

        play_again = input("Play again ? (y/n)").lower()

        if ('y' in play_again):
            continue
        else:
            print(
                f"You have {colored(f'{user_bank:,}$','green')}, see you next time."
            )
            exit()


def main():
    user_interface()


if __name__ == "__main__":
    system('color')
    main()
    system('pause')
