#!/usr/bin/env python3
"""
Entry point file for the application.
"""
from logging.config import dictConfig

from wm_lol import create_app

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": ("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"),
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["wsgi"]},
    }
)
application = create_app()

if __name__ == "__main__":

    application.run()
