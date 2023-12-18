from flask import render_template, Blueprint, redirect, request, flash
from flask_login import login_user, logout_user, login_required, current_user

from project import Project
from user import User

main_bp = Blueprint('main', __name__)


@main_bp.route('/projects')
@login_required
def get_projects():
    # TODO: make projects
    projects = Project.query.filter_by(_user_id=current_user.get_id()).all()
    return render_template('projects.html', projects=projects)


@main_bp.route('/project/<int:project_id>')
@login_required
def get_project(project_id):
    # TODO: make project
    project = Project.query.filter_by(_id=project_id, _user_id=current_user.get_id()).first()
    if not project:
        flash('Project not found', category='danger')
        return redirect('/projects')
    return render_template('project.html')


@main_bp.route('/')
@login_required
def index():
    # TODO: make index
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
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

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

        login_user(user, remember=True)
        return redirect('/')

    return render_template('login.html')


@main_bp.route('/logout')
@login_required
def logout():
    """
    Logs out the current user and redirects them to the login page.

    Returns:
    A redirect response to the login page.
    """

    logout_user()
    return redirect('/login')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register a new user.

    This function handles the registration process for new users. It accepts both
    GET and POST requests. If the request method is POST, it validates the email,
    password, and confirm password fields. If any of the fields are empty, it
    displays an error message and renders the register.html template. If the email
    already exists in the database, it displays an error message and renders the
    register.html template. If the password and confirm password do not match, it
    displays an error message and renders the register.html template.

    If all the validations pass, it creates a new User object with the provided
    email and password. It then logs in the user and redirects them to the home
    page.

    Returns:
        If the request method is POST and any of the validations fail, it returns
        the rendered register.html template with the appropriate error message.
        If the request method is GET or all the validations pass, it returns the
        rendered register.html template.
    """

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

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

        login_user(user, remember=True)

        return redirect('/')
    return render_template('register.html')


@main_bp.after_request
def redirect_to_login(response):
    """
    Redirects the user to the login page if the response has a status code of 401.

    Parameters:
    - response: The HTTP response object.

    Returns:
    - If the response has a status code of 401, redirects the user to the login page.
    - Otherwise, returns the original response object.
    """

    if response.status_code == 401:
        return redirect('/login')

    return response
