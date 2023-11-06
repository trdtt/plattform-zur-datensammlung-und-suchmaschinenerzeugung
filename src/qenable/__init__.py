# pylint: disable=cyclic-import, wrong-import-position
from flask import Flask
app = Flask(__name__, static_folder='./build', static_url_path='/')

import qenable.views  # noqa: F401,E402
