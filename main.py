from app import create_app
from database import db
from login_manager import login_manager


if __name__ == '__main__':
    app = create_app()
    db.init_app(app)
    login_manager.init_app(app)
    app.run(debug=True)

