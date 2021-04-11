r"""The configurations."""

from pathlib import Path

ROOT_PATH = Path(__file__).cwd()


class DevConfig(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///' + str(ROOT_PATH / 'dev_database.sqlite')
    SECRET_KEY = 'dev'


class TestConfig(object):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///' + str(ROOT_PATH / 'test_database.sqlite')
    SECRET_KEY = 'test'
