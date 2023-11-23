from database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    Represents a user in the system.
    """
    __tablename__ = 'users'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True, name='id')
    _email = db.Column(db.String(100), unique=True, nullable=False, name='email')
    _password_hash = db.Column(db.String(255), nullable=False, name='password_hash')

    def __init__(self, email: str, password: str) -> None:
        """
        Initializes a new instance of the class.

        Args:
            email: The email address of the user.
            password: The password of the user.
        """
        self._email = email
        self._set_password(password)
        db.session.add(self)
        db.session.commit()

    def _set_password(self, password: str) -> None:
        """
        Hashes the password and sets the password_hash attribute.

        Args:
            password (str): The password to hash.

        Returns:
            None
        """
        self._password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Checks if the provided password matches the stored password hash.

        Args:
            password: The password to check.

        Returns:
            bool: True if the password matches the stored password hash, False otherwise.
        """
        return check_password_hash(self._password_hash, password)

    def get_id(self) -> int:
        """
        Returns the user's ID.

        :return: The user's ID as an integer.
        """
        return self._id

    def get_email(self) -> str:
        """
        Returns the user's email.

        Args:
            self: The instance of the class.

        Returns:
            str: The user's email.
        """
        return self._email
