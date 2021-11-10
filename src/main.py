from router import Router
from default import create_parser
from oh_my_zsh.install import install

config = {}
options = {}

router = Router(config, options,
    router=Router(
        config, options,
        install = Router(
            config, options,
            ohmyzsh = install)))

opt_parser = create_parser(router, "tasks router runner")
args = opt_parser.parse_args()

if __name__ == "__main__":
    if args.tasks:
        for task in router.tasks():
            print(task)
    else:
        router.dispatch(args.action)

