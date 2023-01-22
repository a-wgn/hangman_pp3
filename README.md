# Hangman game - Project 3 - Python 

![scrrenshot of application](https://user-images.githubusercontent.com/114663540/213947448-8b711c3e-4c36-4dde-bd10-01ba0ff18021.png)


## [Link to application](https://hamngman-pp3.herokuapp.com/)

## Project Documentation 
### Welcome to the [Hangman game!](https://hamngman-pp3.herokuapp.com/)

Hangman is a game that has been played by many children and adults for years. This game has been developed using Python3 for the full stack development course at Code Instute. 

# Features of the Hangman game 

## Words 
For this game 6 random words have been choosen, which will be displayed in dashes of the "Current word". The game will only display words without '-' or ' '. 

## Letters
When the letter is in the word, the dash will display the correct guessed letter. When the letter is not part of the word, the user will see the letter in the used letters and will not be able to use the word and is shown a message 'You already guessed this letter. Try again your luck!'

![screenshot1](https://user-images.githubusercontent.com/114663540/213946396-4d1d9eb4-0c96-4cbb-ad5d-dc96783cdc15.png)
![screenshot2](https://user-images.githubusercontent.com/114663540/213946418-b6ba7f54-9f2d-4564-bc22-d5551f1c531e.png)

## Lives 
The user will directly see how many lives they have. Each time the user guesses the wrong letter, a live will be decuted til 0 lives are left. When the user used all of his lives, the game will inform and dispaly, that the game is lost. 

![screenshot3](https://user-images.githubusercontent.com/114663540/213946464-37efd52f-d4b7-450c-a9a5-d23f0c491cd8.png)

## Invalid characters
Users are not able to use characters within this game which are not letters. 

![screenshot5](https://user-images.githubusercontent.com/114663540/213946587-db8e40e3-5f08-4e92-ba86-8eaeaa366f57.png)

## Game won 
The game is won, when the user has guessed the word correctly and they have still more than 6 lives left. 

![screenshot4](https://user-images.githubusercontent.com/114663540/213946494-be1cd472-69b0-499e-aaee-5b7104b2515b.png)


# Testing 

- Tested that the lives are being shown correct and decuted when the user guessed a wrong letter. When user has 0 lives, the user will see the message 'You have lost the game!'

- Tested that if the letter is correct and in the word, that the letter will be displayed at the 'Current word: _ _ O_"

- Tested that the letters that are incorrect are correclty dispaley '6 lives and used letters: T G K'

- Tested that if the user provides an invalid character that the message 'Invalid letter. Try again!' is being displayed.

- Tested that if lives are left and the user guessed the word corrclty, the user sees the message 'Congrats, you have guessed the word!'

# Validation 

## Python 
Python Linter was the main resource during the code validation process. The code has passed without any error message being displayed. 

### run.py
![Validation](https://user-images.githubusercontent.com/114663540/213946270-51c75bb9-6687-4eb9-ad79-da49fd41b74e.png)

### words.py
![Validation](https://user-images.githubusercontent.com/114663540/213946280-ef315bd1-c2ca-4c55-bb13-10cd18451974.png)

# Bugs 

- No bugs where encountered during development

# Deployment 

The Hangman application has been deployed using Heroku Cloud Platform. 

You can find a [template](https://github.com/Code-Institute-Org/python-essentials-template) prepared by Code Institute that is designed to display this backend application in a modern web browser. This allows the project to be accessible for users without the need of any third party software other than an Internet browser application.

GitPod is the main platform that has been used to develope the project. 

# Credits and References 

This Hangman game has been devloped in the same way that children and adults would play on a piece of paper! 

# Closing Remarks
