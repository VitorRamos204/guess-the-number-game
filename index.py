from random import randint

secretnumber = randint(1, 10)
attempts = 5
print('-=-'*30)
print('                           Guess The Number Game                       ')
print('-=-'*30)
while True:
    choice = int(input('Guess the number (1 at 10): '))
    if choice == secretnumber:
        print('Great! you choice the secret number')
        break
    elif choice != secretnumber:
        attempts -= 1
        print(f'Wrong number, try again, you have {attempts} attempts')
        if attempts == 0:
            break
    else:
        print(f'The right number is {secretnumber}')
print('Thank you for playing Guess The Number, if you wanna play again just start the software again :D"')
