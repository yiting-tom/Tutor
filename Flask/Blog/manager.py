from flask_script import Manager

from app import app

manager = Manager(app)


@manager.command
def start():
    app.run()

if __name__ == "__main__":
    manager.run()
