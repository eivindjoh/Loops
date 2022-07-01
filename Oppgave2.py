target_number = int(input('Target number: '))
lives = int(input('Number of allowed guesses: '))
print('\n'*20)
print('''
   ___|                                      
  |      |   |   _ \   __|   __|             
  |   |  |   |   __/ \__ \ \__ \             
 \|___||\__,_| \___| ____/ ____/             
  __|  __ \    _ \                           
  |    | | |   __/                           
 \_\| || |_| \___|         |                 
    \ |  |   |  __ `__ \   __ \    _ \   __| 
  |\  |  |   |  |   |   |  |   |   __/  |    
 _| \_| \__,_| _|  _|  _| _.__/  \___| _|   
''')

count_fail = 0

while True:
    input_number = int(input('Guess the number: '))

    if input_number > target_number:
        print('Wrong. The target number is lower.')
    elif input_number < target_number:
        print('Wrong. The target number is higher.')
    else:
        print('You win!')
        break
    count_fail += 1
    lives_left = lives - count_fail
    print(f'Lives left: {lives_left}')

    if lives_left == 0:
        print('You loose')
        break
