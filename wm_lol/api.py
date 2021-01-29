#!/usr/bin/env python3
from flask import Blueprint, request, redirect, render_template
from werkzeug.exceptions import BadRequest
from commands import get_matchers

api = Blueprint("api", __name__)


@api.route("/search", methods=["GET"])
def search():
    if (
        'list' in request.args
        or 'help' in request.args
        or request.args.get("query", "") == "list"
        or request.args.get("query", "") == "help"
    ):
        matchers = get_matchers()
        return render_template(
            "help.html",
            app_search_url=request.base_url + "?query=%s",
            matchers=matchers,
        )

    if 'query' not in request.args:
        raise BadRequest(
            "You have to pass a query in the query parameter "
            "(like ?query=<your query>)."
        )

    debug = 'debug' in request.args
    query = request.args['query']
    for matcher in get_matchers():
        if matcher.match(query):
            if debug:
                print(f"matcher {matcher} matched query {query}")
            return matcher.run(query)

        print(f"matcher {matcher} did not match query {query}")

    return redirect(f"https://www.google.com/search?q={query}")
