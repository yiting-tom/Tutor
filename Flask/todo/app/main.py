r"""The entry point."""
from __init__ import *
from migrations import database
from routes.web import *


def main():
    app.run()


if __name__ == '__main__':
    main()
