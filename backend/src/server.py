#!/usr/bin/env python

__author__ = "Leonardo de Oliveira Sales"
__date__ = "$Dec 11, 2021 14:23:00 AM$"

from os import environ
from routes.people import app


def server():
    app.run(
        host=environ.get('BACKEND_FLASK_HOST', '0.0.0.0'),
        port=environ.get('BACKEND_FLASK_HOST', 3000),
        debug=True
    )


if __name__ == '__main__':
    server()
