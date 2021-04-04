r"""Contain all modules."""
from __init__ import *
from sqlalchemy import Model, Column, String, Integer


class User(db.Model):
    r"""User model.

    """
    # Table name.
    __tablename__ = 'Users'
    # Table columns.
    id = Column(Integer, primary_key=True)
    username = Column(String(31), unique=True, nullable=False)
    password = Column(String(31), unique=True, nullable=False)
    email = Column(String(63), unique=True, nullable=False)

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 email: str = None):
        r"""Initialize the column values."""
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"<User {self.username} {self.email}"

    @staticmethod
    def in_db(form) -> bool:
        r"""Check if the user can login.

        Parameters
        ==========
        form
            username, password, email

        Returns
        =======
        bool
            The username and password is in DB.
        """
        return User.query.filter_by(
            username=form['username'],
            password=form['password'],
            email=form['email']) is not None

    @staticmethod
    def insert(form) -> db.Model:
        r"""Insert into DB.

        Parameters
        ==========
        form
            username, password, email

        Returns
        =======
        bool
            Insertion succeed.
        """
        new_user = User(
            username=form['username'],
            password=form['password'],
            email=form['email'],
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user
