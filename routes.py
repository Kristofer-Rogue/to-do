from flask import render_template, Blueprint, session, redirect, request, flash
from user import User
from database import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)


@main_bp.route('/project/<int:project_id>')
def project(project_id):
    return render_template('project.html')


@main_bp.route('/')
def index():
    return render_template('timer.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
       Handles the login functionality.

       If a user is already logged in, redirects to the home page.
       If a POST request is received, validates the email and password,
       logs in the user, and redirects to the home page.
       If a GET request is received, renders the login page.

       Returns:
           If successful, redirects to the home page.
           Otherwise, renders the login page with appropriate flash messages.
    """
    if session.get('user'):
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            flash('Email and password are required', category='danger')
            return render_template('login.html')

        user = User.query.filter_by(_email=email).first()

        if not user:
            flash('Invalid email', category='danger')
            return render_template('login.html')
        if not user.check_password(password):
            flash('Invalid password', category='danger')
            return render_template('login.html')
        session['user'] = user.get_id()
        session['login'] = True
        return redirect('/')

    return render_template('login.html')


@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user'):
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if not email or not password:
            flash('Email and password are required', category='danger')
            return render_template('register.html')
        if User.query.filter_by(_email=email).first():
            flash('Email already exists', category='danger')
            return render_template('register.html')
        if password != confirm_password:
            flash('Passwords do not match', category='danger')
            return render_template('register.html')

        user = User(email, password)
        session['user'] = user.get_id()
        session['login'] = True
        return redirect('/')
    return render_template('register.html')
