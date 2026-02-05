from flask import Flask, request, render_template, redirect, url_for
from my_flask_app.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'   # required for Flask-WTF forms


# Home page
@app.route('/index')
def index():
    # Get the user's browser and store it in the browser variable
    browser = request.headers.get('User-Agent', '')

    # Determine the browser based on the browser string
    if 'Firefox' in browser:
        user_agent = 'Firefox'
    elif 'Chrome' in browser and 'Chromium' not in browser:
        user_agent = 'Chrome'
    elif 'Opera' in browser or 'OPR' in browser:
        user_agent = 'Opera'
    elif 'Safari' in browser and 'Chrome' not in browser:
        user_agent = 'Safari'
    elif 'Edge' in browser:
        user_agent = 'Edge'
    else:
        user_agent = 'Unknown'

    # Display the home page and pass the user agent variable to it
    return render_template('index.html', user_agent=user_agent)


# About page
@app.route('/about')
def about():
    return render_template('about.html')


# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Menu / Product page
@app.route('/menu')
def menu():
    return render_template('menu.html')


# Register / Signup page
@app.route('/register', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Normally you would save user data here
        return redirect(url_for('success'))
    return render_template('register.html', form=form)


# Success page after registration
@app.route('/success')
def success():
    return "<h2>Registration successful!</h2>"


if __name__ == "__main__":
    app.run(debug=True)
