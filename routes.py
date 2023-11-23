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


@main_bp.route('/login')
def login():
    return render_template('login.html')


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
