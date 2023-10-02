from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calc(number = None):
    if len(request.args) == 0:
        return render_template('calculate.html')
    number = request.args['number']
    try:
        if int(number) % 2 == 0:
            output = 'is even'
        elif int(number) % 2 == 1:
            output = 'is odd'
    except:
        output = 'is not an integer!'

    return render_template('calculate.html', num = number, output = output)

if __name__ == "__main__":
    app.run()