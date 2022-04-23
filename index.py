def secretnumber(a=0):
        from random import randint
        print('-=-'*30)
        print('                           Guess The Number Game                       ')
        print('-=-'*30) 
        a = randint(1, 10)
        return a
        

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
print(f'The right number is {secret}')
print('Thank you for playing Guess The Number, if you wanna play again just start the software again :D"')
