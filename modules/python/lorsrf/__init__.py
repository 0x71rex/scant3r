#!/usr/bin/env python3
from core.libs import Http
from .lorsrf import Lorsrf


def main(opts: dict, http: Http):
    Lorsrf(opts, http).start()
