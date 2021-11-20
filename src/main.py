from router import Router
from oh_my_zsh.install import install
from app import App

if __name__ == "__main__":
    app = App()
    app.use(
        Router(
            router=Router(
                install=Router(
                    ohmyzsh=install))))
    app.run()
