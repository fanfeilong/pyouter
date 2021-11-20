import argparse


def create_parser(description, tasks="tasks"):
    opt_parser = argparse.ArgumentParser(description=description)

    opt_parser.add_argument(
        'actions',
        metavar='A',
        type=str,
        nargs='?',
        help='actions strings in tree')

    opt_parser.add_argument(
        f'--{tasks}',
        const=True,
        dest='tasks',
        nargs='?',
        help='completion the actions strings'
    )

    opt_parser.add_argument(
        "-s", '--script-name',
        dest="script",
        nargs='?',
        type=str,
        help='completion the actions strings'
    )

    opt_parser.add_argument(
        "-v", "--view",
        dest="view",
        help="view the router track",
        action="store_true",
        # metavar="V"
    )

    return opt_parser
