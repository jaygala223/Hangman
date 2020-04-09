import random

print('''
Lets Play Hangman
  ____
 |    |
 |    O
 |  \_|_/
 |   _|_
 |  |   |
_|_________
    ''')
hp_names = ['ram', 'sita', 'hanuman', 'laxman','ravan','sugreev','bali','dashrath']

picked_name = random.choice(hp_names)

correct = []
hanged = False
right_counter = 0
wrong_counter = 0

while not hanged:
    guess = input("Guess a Letter!")

    if guess in picked_name:
        print('YES!')
        right_counter += 1
        correct.append(guess)
        for x in range(0,len(picked_name)):
            if picked_name[x] == guess:
                print(picked_name[x])
            else:
                print('_')
    else:
        print('Try Again!')
        wrong_counter += 1
        if wrong_counter == 6:
            hanged = True
            print('''
                ____
               |    |
               |    @
               |  \_|_/
               |   _|_
               |  |   |
              _|_________
            ''')
        if wrong_counter == 5:
            print('''
                ____
               |    |
               |    @
               |  \_|_/
               |    |
               |
              _|_________
            ''')
        if wrong_counter == 4:
            print('''
                ____
               |    |
               |    @
               |    |
               |    |
               |
              _|_________
            ''')
        if wrong_counter == 3:
            print('''
                ____
               |    |
               |    @
               |
               |
               |
              _|_________
            ''')
        if wrong_counter == 2:
            print('''
                ____
               |    |
               |
               |
               |
               |
              _|_________
            ''')
        if wrong_counter == 1:
            print('''
                ____
               |
               |
               |
               |
               |
              _|_________
            ''')

    if right_counter == len(picked_name):
        full_name = input("Write the answer: ")
        if full_name == picked_name:
            print("You Won!")
            print(f"The word was {picked_name}")
            hanged = True


if wrong_counter == 6:
    print("You Lose!")
