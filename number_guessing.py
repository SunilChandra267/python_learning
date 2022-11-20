import random

guess_count = 0
guess_number = random.randint(1, 10)


while guess_count < 3:
    guess_data = int(input('guess? :'))
    if guess_data > 10:
        print('please enter the value between 1 - 10')
        continue
    else:
        guess_count += 1
    if guess_data < guess_number:
        print('too less')
    elif guess_data > guess_number:
        print('too high')
    else:
        print('you won')
        break
else:
    print('you lost')
    print('guess number is ' + str(guess_number))
