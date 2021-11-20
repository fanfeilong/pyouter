#!/usr/bin/env python

from router import Router
from oh_my_zsh.install import install as omz
from fish.install import install as fish
from app import App

if __name__ == "__main__":
    app = App()
    app.use(
        router=Router(
            install=Router(
                ohmyzsh=omz,
                fish=fish)))
    app.run()
