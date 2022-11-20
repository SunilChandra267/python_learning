import random, sys

print('Rock O, Paper #, Scissor X Game')
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Loses, %s Ties ' % (wins, losses, ties))
    while True:
        print('''Enter Your Move
Rock : O 
Paper : #  
Scissor : X
Exit Game : Q
        ''')
        player_move = input().upper()
        if player_move == 'Q':
            print('exiting game ')
            
            sys.exit()
        if player_move == 'O' or player_move == '#' or player_move == 'X':
            break
        print('please enter correct choice for Rock (O), Paper (#), Scissors (X)')
    if player_move == 'O':
        user_choice = 'Rock'
    elif player_move == '#':
        user_choice = 'Paper'
    else:
        user_choice = 'Scissor'
    print(f'{user_choice} versus')

    #code to get computer choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        sys_choice = 'Rock'
    elif random_number == 2:
        sys_choice = 'Paper'
    else:
        sys_choice = 'Scissor'
    print(sys_choice)

    if user_choice == sys_choice:
        print('Tie!!!')
        ties += 1
    elif (user_choice == 'Rock' and sys_choice == 'Paper') or (user_choice == 'Paper' and sys_choice == 'Scissor') or (
            'Scissor' == user_choice and sys_choice == 'Rock'):
        print('You Lose!!')
        losses += 1
    else:
        print('You win!!')
        wins += 1






