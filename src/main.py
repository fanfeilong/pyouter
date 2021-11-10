from router import Router
from default import create_parser
from oh_my_zsh.install import install

config = {}

opt_parser = create_parser("tasks router runner")
options = opt_parser.parse_args()

router = Router(config, options,
    router=Router(
        config, options,
        install = Router(
            config, options,
            ohmyzsh = install)))



if __name__ == "__main__":
    if args.tasks:
        for task in router.tasks():
            print(task)
    else:
        router.dispatch(args.action)

