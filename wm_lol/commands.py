#!/usr/bin/env python3
from abc import abstractmethod
from flask import redirect
from urllib.parse import quote
from dataclasses import dataclass
from typing import List


@dataclass
class Matcher:
    name: str

    def __hash__(self):
        return hash(self.name)

    @abstractmethod
    def match(self, query: str) -> bool:
        raise NotImplementedError()


@dataclass
class PrefixMatcher(Matcher):
    prefixes: List[str]
    url_template: str

    def match(self, query: str) -> bool:
        for prefix in self.prefixes:
            if query.startswith(f"{prefix} ") or query == prefix:
                return True

        return False

    def run(self, query: str):
        rest = query.split(" ", 1)[-1]
        if rest == query:
            rest = ""

        return redirect(
            self.url_template.format(match=quote(rest)),
            code=302,
        )

    def __str__(self) -> str:
        return (
            f"{self.name}: prefixes={self.prefixes}, "
            f"url_template={self.url_template}"
        )


def get_matchers() -> List[Matcher]:
    return [
        PrefixMatcher(
            name="Wikimedia office",
            prefixes=["wo"],
            url_template=(
                "https://office.wikimedia.org/w/index.php?search={match}"
            ),
        ),
        PrefixMatcher(
            name="Wikitech",
            prefixes=["wt"],
            url_template=(
                "https://wikitech.wikimedia.org/w/index.php?search={match}"
            ),
        ),
        PrefixMatcher(
            name="Phabricator",
            prefixes=["t", "task"],
            url_template="https://phabricator.wikimedia.org/{match}",
        ),
        PrefixMatcher(
            name="EN Wikipedia",
            prefixes=["w", "wiki"],
            url_template="https://en.wikipedia.org/w/index.php?search={match}",
        ),
        PrefixMatcher(
            name="calendar",
            prefixes=["cal"],
            url_template="https://calendar.google.com/{match}",
        ),
        PrefixMatcher(
            name="horizon",
            prefixes=["h", "horizon"],
            url_template="https://horizon.wikimedia.org/{match}",
        ),
        PrefixMatcher(
            name="gerrit",
            prefixes=["gerrit"],
            url_template="https://gerrit.wikimedia.org/r/q/{match}",
        ),
        PrefixMatcher(
            name="netbox",
            prefixes=["nb", "netbox"],
            url_template="https://netbox.wikimedia.org/search/?q={match}",
        ),
        PrefixMatcher(
            name="rw graphana",
            prefixes=["graph", "graf", "grafana"],
            url_template=(
                "https://grafana-rw.wikimedia.org/dashboard/new?query={match}"
            ),
        ),
        PrefixMatcher(
            name="Labs grafana",
            prefixes=["lgraph", "lgraf", "lgrafana"],
            url_template=(
                "https://grafana-labs.wikimedia.org/dashboard/new?query="
                "{match}"
            ),
        ),
        PrefixMatcher(
            name="icinga",
            prefixes=["nagios", "icinga"],
            url_template=(
                "https://icinga.wikimedia.org/cgi-bin/icinga/status.cgi"
                "?search_string={match}"
            ),
        ),
        PrefixMatcher(
            name="SAL",
            prefixes=["sal"],
            url_template="https://sal.toolforge.org/{match}",
        ),
        PrefixMatcher(
            name="toolsadmin",
            prefixes=["ta", "toolsadmin"],
            url_template="https://toolsadmin.wikimedia.org/tools/?q={match}",
        ),
        PrefixMatcher(
            name="openstack browser",
            prefixes=["ob", "openstack-browser"],
            url_template="https://openstack-browser.toolforge.org/{match}",
        ),
        PrefixMatcher(
            name="openstack browser - projects",
            prefixes=["obp", "openstack-browser-project"],
            url_template=(
                "https://openstack-browser.toolforge.org/project/{match}"
            ),
        ),
        PrefixMatcher(
            name="openstack browser - servers",
            prefixes=["obs", "openstack-browser-server"],
            url_template=(
                "https://openstack-browser.toolforge.org/server/{match}"
            ),
        ),
        PrefixMatcher(
            name="Meta wiki",
            prefixes=["meta"],
            url_template=(
                "https://meta.wikimedia.org/w/index.php?search={match}"
            ),
        ),
        PrefixMatcher(
            name="Mailman lists",
            prefixes=["lists"],
            url_template=(
                "https://lists.wikimedia.org/mailman/listinfo/{match}"
            ),
        ),
        PrefixMatcher(
            name="google",
            prefixes=["g", "google"],
            url_template="https://google.com?q={match}",
        ),
        PrefixMatcher(
            name="duckduckgo",
            prefixes=["dd", "duckduck"],
            url_template="https://duckduckgo.com?q={match}",
        ),
        PrefixMatcher(
            name="Debmonitor",
            prefixes=["dm", "debmonitor"],
            url_template="https://debmonitor.wikimedia.org/{match}",
        ),
        PrefixMatcher(
            name="Puppetboard",
            prefixes=["pb", "puppetboard"],
            url_template="https://puppetboard.wikimedia.org/{match}",
        ),
        PrefixMatcher(
            name="Kudos wiki, show some wikilove :)",
            prefixes=["kudos"],
            url_template="https://office.wikimedia.org/wiki/Kudos",
        ),
        PrefixMatcher(
            name="Etherpad",
            prefixes=["e", "ether", "etherpad"],
            url_template="https://etherpad.wikimedia.org/{match}",
        ),
        PrefixMatcher(
            name="Contact list for WMF",
            prefixes=["contacts", "people"],
            url_template="https://office.wikimedia.org/wiki/Contact_list",
        ),
    ]
