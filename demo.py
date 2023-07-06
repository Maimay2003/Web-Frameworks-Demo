from flask import Flask, render_template, url_for, flash, redirect # importing Flask
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__) # Flask needs the name of the file 
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '4c527b86885c93870bd914dc2885ecf8'

@app.route("/") # tells us URL
@app.route("/home")
def home():
    #return "<p>Hello, World!</p>" # prints HTML to the webpage
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/second_page") # tells us URL
def second_page():
  return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm();
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

if __name__ == '__main__': # the end
    app.run(debug=True, host="0.0.0.0")