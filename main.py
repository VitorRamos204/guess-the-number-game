def secretnumber(a=0):
        from random import randint
        print('-=-'*30)
        print('                           Guess The Number Game                       ')
        print('-=-'*30) 
        a = randint(1, 10)
        return a


def game():
    secret = secretnumber()
    attempts = 5
    while True:
        choice = int(input('Guess the number (1 at 10): '))
        if choice == secret:
            print('Great! you choice the secret number')
            break
        elif choice != secret:
            attempts -= 1
            print(f'Wrong number, try again, you have {attempts} attempts')
            if attempts == 0:
                break


# Main
game()
while True:
    newgame = str(input(('Play again? \n1. Yes \n2. No\n Y/N: ')))
    if newgame in 'Yy':
        game()
    else:
        print('Thank you for playing Guess The Number =)')
        break
       