from flask import Flask, render_template, request
from checkmypass import main, pwned_api_check

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        password = request.form['password']
        # print(password)
        if password == '':
            return render_template('index.html', message='Please enter a password')
        # main(count)
        count = pwned_api_check(password)
        if count:
            return render_template('index.html', message=f'{password} was found {count} times... you should probaly change your password')
        else:
            return render_template('index.html', message=f'{password} was NOT found. Carry on!')


if __name__ == '__main__':
    app.run()
