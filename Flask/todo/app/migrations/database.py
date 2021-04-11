from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


ROOT_PATH = Path(__name__).cwd()

engine = create_engine(
    'sqlite:///' + str(ROOT_PATH / 'migrations' / 'database.sqlite'),
    convert_unicode=True)

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def init_db():
    r"""Initialize the database."""
    import models
    Base.metadata.create_all(bind=engine)
