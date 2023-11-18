from app import create_app
from database import db


if __name__ == '__main__':
    app = create_app()
    db.init_app(app)
    app.run(debug=True)
