#!/usr/bin/env python3

from setuptools import setup

URL = ""
BUGTRACKER_URL = ""


if __name__ == "__main__":
    setup(
        author="David Caro",
        author_email="david@dcaro.es",
        description="Wikimedia opinionated bunny1 rewrite",
        setup_requires=["autosemver"],
        install_requires=["autosemver"],
        license="GPLv3",
        name="wm_lol",
        package_data={"": ["CHANGELOG", "AUTHORS"]},
        packages=["wm_lol"],
        url=URL,
        autosemver={
            "bugtracker_url": BUGTRACKER_URL,
        },
    )
