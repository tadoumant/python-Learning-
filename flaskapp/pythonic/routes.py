from flask import  render_template, url_for, flash, redirect
from pythonic.models import User,Lesson,Course
from pythonic.forms import RegistrationForm, LoginForm,FlaskForm
from pythonic import app,bcrypt,db
from flask_login import login_user

lessons = [{
    'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Marouan',
    'thumbnail': 'thumbnail.jpg'
},
]

courses = [
{
        'name': 'Python',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Data Analysis',
        'icon': 'analysis.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Machine Learning',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Web Design',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Blockchain',
        'icon': 'blockchain.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Tips & Tricks',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]



@app.route("/")
def home():
    return render_template('home.html',title="home",lessons=lessons,courses=courses)


@app.route("/about")
def about():
    return render_template("about.html")

#registre form
@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    #validation de input
    if form.validate_on_submit():
        #hashing password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            fname=form.fname.data,
            lname=form.lname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("login"))
    return render_template('register.html',title="register",form=form)

#login form
@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template('login.html',title="Login",form=form)
