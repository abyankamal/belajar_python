import random
from flask import Flask
app = Flask(__name__)


class Guess():
    def __init__(self):
        self.correct_answer = random.randint(0, 9)

    def refresh(self):
        self.correct_answer = random.randint(0, 9)


guess = Guess()


@app.route('/')
def guess_number():
    global guess
    guess.refresh()
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guessed_number>')
def user_guess(guessed_number):
    global guess
    if guessed_number > guess.correct_answer:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guessed_number < guess.correct_answer:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)