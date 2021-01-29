#!/usr/bin/env python3
from flask import Flask, render_template, request

from wm_lol.api import api
from wm_lol.commands import get_matchers

SPLASH_MESSAGE = """
WM Lol is a wikimedia-focused rewrite of bunny1, it allows you to use it as a
search engine in your browser to redirect to the right places by using
minimalistic shortcuts.
"""


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api/v1")

    @app.route("/")
    def root():
        return render_template(
            "help.html",
            app_search_url=request.base_url + "api/v1/search?query=%s",
            matchers=get_matchers(),
        )

    return app
