r"""The configuration objects."""
from pathlib import Path


# Ref: https://flask.palletsprojects.com/en/1.1.x/config/
class DevelopmentConfig(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///' + str(Path(__file__).cwd / 'dev_db.sqlite')
    SECRET_KEY = r'0f--J@#f0349fj9*-=40(!jf-2jaoj9as;d.cz;@e;vnkf'


class DevelopmentConfig(object):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///' + str(Path(__file__).cwd / 'test_db.sqlite')
    SECRET_KEY = r'19j@#98&HO(*h3o9H49p3*H!P98hp1h843fuh34zfh21!#'

