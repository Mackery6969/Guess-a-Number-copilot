# Pick a number between 1 and 10 and try to guess it.

# pick a random number between 1 and 10
import random

print('I am thinking of a number between 1 and 10.');
number = random.randint(1, 10);
guess = '';
guessList = [];
guessCount = 0;

# before the game starts ask if the player wants the difficulty to be easy or hard
difficulty = input('Do you want the game to be easy or hard? ');
if difficulty == 'easy':
    print('you have 3 guesses.');
elif difficulty == 'hard':
    print('you have 1 guess.');
else:
    print('invalid response')

while guess != number:
    # get a guess from the user
    guess = int(input('What is your guess? '));
    # add the guess to the list
    guessList.append(guess);
    # count the number of guesses
    guessCount += 1;
    # check if the guess is correct
    if guess == number:
        print('Good job! You guessed my number!');
    else:
        print('Nope. Better luck next time!');

    # check if the guess is valid
    if not guess < 1 or not guess > 10:
        print('sorry, you must guess a number between 1 and 10');

    # check if the user has guessed 1 time
    if guessCount == 1 and difficulty == 'hard':
        print('You have guessed 1 time.');
        print('you have failed');
        print('you were not able to guess the number');
        print('the number was', number);
        print('you guessed', guessList);
        break
    elif guessCount == 3 and difficulty == 'easy':
        print('You have guessed 3 times.');
        print('you were not able to guess the number');
        print('the number was', number);
        print('you guessed', guessList);
        break
    
# check if the player wants to play again
playAgain = input('Do you want to play again? (y/n) ');
if playAgain == 'y':
    guess = '';
    guessList = [];
    guessCount = 0;
    number = random.randint(1, 10);
    print('I am thinking of a number between 1 and 10.');
elif playAgain == 'n':
    print('Thanks for playing!');

# check if the user input a invalid response
else:
    print('Invalid response!');