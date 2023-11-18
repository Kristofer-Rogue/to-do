from flask import render_template, Blueprint
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