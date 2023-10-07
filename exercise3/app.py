from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

registry = {}

organizations = ['code9', 'Charlotte Hack', 'CEPA', 'Plants for People', 'Dog Lovers']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')

        if not name or not organization:
            error = 'Both name and organization required.'
            return render_template('index.html', organizations = organizations, error = error)
        
        if organization not in organizations:
            error = 'Invalid organization selected'
            return render_template('index.html', organizations = organizations, error = error)
        
        registry[name] = organization

        return redirect(url_for('regStudents'))
    else:
        return render_template('index.html', organizations=organizations)

@app.route('/regStudents')
def regStudents():
    return render_template('regStudents.html', registry=registry)

if __name__ == "__main__":
    app.run(debug=True)