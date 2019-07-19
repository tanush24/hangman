#allows time.sleep function to work
import time

#allows random word to be generated
import random

#stage of drawing the hangman
stage = 0

#number of guesses
guessNumber = 6

#array of guesses made by partcipant
guessed = ['list of words you have guessed: ']

#list of possible words
words = ['VISA','Mastercard','authorization','payments','clearing','interchange','settlement','issuer','acquirer','merchant','cardholder','consumer','commercial','fee','bank','reading','global','tax','security','fraud','cybersource','cyber','developer','tester','software','tester','online','business','analyst','iterative','CV','currency','exchange','rates','interest','waterfall','agile','treasury']

#correct guess check
def correct(guess):
    if guess in i:
        if guess not in guessed:
            print("Correct")
            return(True)
    else:
        if guess not in i and len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyz':
            if guess not in guessed:
                print("Incorrect!")
                return(False)

#initial drawing
one = ("  ________")
two = ("  | / {}")
three = ("  |/ {}")
four = ("  | {}")
five = ("  | {}")
six = ("  |____")


print("Welcome to hangman!")
time.sleep(0.5)
print('All words have a financial theme.')
time.sleep(0.5)
print("You can input any letter from a-z.")

#picks a random word from the word list
i = random.choice(words).lower()


#shows the number of letters in the word and the number of blank spaces left
guessed_letters = len(i) * ['_']
print(' '.join(guessed_letters))

#activates when you still have guesses left
while guessNumber > 0:
    
    #boolean to check for repeated guesses
    isGuess = True
    
    #activates once you have guessed all letters
    if '_' not in guessed_letters :
        print('You have guessed the word, congrats!')
        break
    
    #asks for an input
    guess = str(input('Guess a letter ')).lower()

    #checks if the user inputted a letter and handles type errors and repeated letter errors
    if len(guess) != 1 or guess not in ('abcdefghijklmnopqrstuvwxyz '):
        time.sleep(0.25)
        print("That is not a letter, try again. ")
    if guess in guessed:
        time.sleep(0.25)
        print("You have already guessed that letter, try again. ")
        
        #makes sure the repeated letter isn't added to list of guessed letters
        isGuess = False

        
    iscorrect = correct(guess)
    
    #check if guess already exist, if yes do not add to list of guessed words
    if isGuess == True:
        guessed.append(guess)
        print(guessed)

    #if the guessed letter is in the random word then fill the blanks that letter fills
    if iscorrect == True:
        for position, letter in enumerate(i):
          if letter == guess:
            guessed_letters[position] = letter
        print(' '.join(guessed_letters))

    #if guess is incorrect remove a life
    if iscorrect == False and guessNumber > 0:
        guessNumber = guessNumber - 1

        #if the guess is incorrect and the user runs out of lives the hangman stops being drawn and the game ends
        if guessNumber == 0:
            time.sleep(0.5)

            #shows what the correct word is
            print("You lose, the word was", i)

        #if the guess is incorrect but the user still has remaining lives, continue drawing the hangman
        else:
            print('Retry, you have', guessNumber, 'lives remaining ')
        stage = stage + 1

        #different stages of the hangman drawing
        if stage == 1:

            print(one)
            print(two.format(" "))
            print(three.format(" "))
            print(four.format(" "))
            print(five.format(" "))
            print(six)

        if stage == 2:
            print(one)
            print(two.format("|"))
            print(three.format(" "))
            print(four.format(" "))
            print(five.format(" "))
            print(six)

        if stage == 3:
            print(one)
            print(two.format("|"))
            print(three.format(" O"))
            print(four.format(" "))
            print(five.format(" "))
            print(six)

        if stage == 4:
            print(one)
            print(two.format("|"))
            print(three.format(" O"))
            print(four.format("--|--"))
            print(five.format(" "))
            print(six)

        if stage == 5:
            print(one)
            print(two.format("|"))
            print(three.format(" O"))
            print(four.format("--|--"))
            print(five.format(" / \\"))
            print(six)


            

