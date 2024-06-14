from flask import Blueprint, render_template
from flask import request
import random
import string

kirjainpeli_bp = Blueprint('kirjainpeli', __name__, template_folder='templates')

@kirjainpeli_bp.route('/kirjainpeli', methods=['GET', 'POST'])
def kirjainpeli():
    message = ''
    if request.method == 'GET':
        letter_to_display = random.choice(string.ascii_uppercase)
    else:
        user_input = request.form['input_letter'].upper()
        correct = (user_input == request.form['hidden_letter'])
        if correct:
            message = 'Oikein!'
            letter_to_display = random.choice(string.ascii_uppercase)
        else:
            message = 'Yritä uudelleen'
            letter_to_display = request.form['hidden_letter']
    return render_template('kirjainpeli.html', letter=letter_to_display, message=message)