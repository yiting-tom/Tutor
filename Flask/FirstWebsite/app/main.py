r"""The main entry point for backend."""
from __init__ import *

from router import *

if __name__ == '__main__':
    r"""Entry point."""
    app.debug = True
    app.secret_key = __name__
    app.run()
