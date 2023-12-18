from database import db


class Project(db.Model):
    """
    Represents a project in the system.
    """
    __tablename__ = 'projects'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True, name='id')
    _title = db.Column(db.String(100), nullable=False, name='title')
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, name='user_id')

    def __init__(self, title: str, user_id: int) -> None:
        """
        Initializes a new instance of the class.

        Args:
            title: The title of the project.
            user_id: The ID of the user who owns the project.
        """
        self._title = title
        self._user_id = user_id
        db.session.add(self)
        db.session.commit()
