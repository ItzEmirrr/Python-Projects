import random
NUM_DIGITS = 3
MAX_GUESSES = 10
def get_secret_num():
    numbers = list('123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num
def get_clues(guess,secret_num):
    if guess == secret_num:
        return 'you got it!'
    clues = []
    for i,v in enumerate(guess):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
def main():
    while True:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('>')
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1
            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('you ran out guesse')
                print(f'the answer was {secret_num}')
        print('do you want to play again? (yes/no)')
        if not input('>').lower().startswith('y'):
            break

if __name__ == '__main__':
    main()