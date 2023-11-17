from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/project/<int:project_id>')
def project(project_id):
    return render_template('project.html')


@app.route('/')
def index():
    return render_template('timer.html')


if __name__ == '__main__':
    app.run(debug=True)