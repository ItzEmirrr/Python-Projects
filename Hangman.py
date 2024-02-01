import random

HANGMAN_PICS = ['1', '2', '3', '4', '5', '6', '7']
words = 'яблоко собака кошка кролик ручка карандаш шапка рубашка джинсы '.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Пожалуйста, напишите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Напишите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже угадали эту букву!')
        elif guess not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Это не буква. Напишите букву')
        else:
            return guess


def playAgain():
    print('Хотите сыграть еще раз? Д/Н')
    return input().upper().startswith('Д')


def main():
    print('В И С Е Л И Ц А')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameFinished = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Да! Секретным словом было "' + secretWord + '"! Вы выиграли!')
                gameFinished = True
        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('Вы проиграли' , str(len(missedLetters)),' неправильные отгадывания и ', str(
                    len(correctLetters)), ' правильные отгадывания, слово было "' , secretWord , '"')
                gameFinished = True
        if gameFinished:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameFinished = False
                secretWord = getRandomWord(words)
            else:
                break


if __name__ == '__main__':
    main()
