import argparse

def create_parser(description, tasks="tasks"):
    opt_parser = argparse.ArgumentParser(description=description)
    opt_parser.add_argument('action', metavar='A', type=str, nargs='?',
                        help='actions strings in tree')
    opt_parser.add_argument(f'--{tasks}', const=True, dest='tasks', nargs='?',
                        help='completion the actions strings')

    return opt_parser

