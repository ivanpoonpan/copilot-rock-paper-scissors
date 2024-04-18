from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['POST'])
def play_game():
    user_choice = request.json['choice']
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    if user_choice not in choices:
        return jsonify({'error': 'Invalid choice'}), 400

    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (user_choice == 'rock' and (computer_choice == 'scissors' or computer_choice == 'lizard')) or \
         (user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock')) or \
         (user_choice == 'scissors' and (computer_choice == 'paper' or computer_choice == 'lizard')) or \
         (user_choice == 'lizard' and (computer_choice == 'spock' or computer_choice == 'paper')) or \
         (user_choice == 'spock' and (computer_choice == 'scissors' or computer_choice == 'rock')):
        result = 'You win!'
    else:
        result = 'You lose!'
    return jsonify({'result': result}), 200

if __name__ == "__main__":
    app.run(debug=True)