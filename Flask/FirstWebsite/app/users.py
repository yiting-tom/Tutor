r"""The module for some user operations."""

from __init__ import *


class User(db.Model):
    r"""The user model."""
    # Table 名稱(複數)
    __tablename__ = 'Users'

    # Column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(31), unique=True, nullable=False)
    password = db.Column(db.String(31), unique=True, nullable=False)
    email = db.Column(db.String(63), unique=True, nullable=False)

    def __init__(self, username: str=None, password: str=None, email: str=None):
        r"""Initialize the column values."""
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"<User {id(self)} {self.password} {self.email}>"


    @staticmethod
    def can_login(username: str, password: str) -> bool:
        r"""Check if the user can login.

        Parameters
        ==========
        username : str
        passwrod : str

        Examples
        ========
        >>> from users import User
        >>> User.can_login('abc', '123')
        True
        """
        return User.query.filter_by(username=username, password=password) is not None




