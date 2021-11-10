#!/usr/bin/env python

import sys
import argparse

router = {
    "tree": {
        "gen": None,
        "parse": None,
    },
    "run": {
        "server": None,
        "debug": None
    }
}

def gen_helper(action, router):
    for key in router:
        next_router = router[key]
        next_action = key if action is None else f"{action}.{key}"
        if type(next_router) is dict:
            for sub in gen_helper(next_action, next_router):
                yield sub
        else:
            yield next_action



def completion(router):
    for task in gen_helper(None, router):
        yield task

parser = argparse.ArgumentParser(description='run action by tree map')
parser.add_argument('actions', metavar='A', type=str, nargs='?',
                    help='actions strings in tree')
parser.add_argument('--tasks', dest='tasks', nargs='?',
                    help='completion the actions strings')

args = parser.parse_args()

if args.tasks is not None:
    for task in completion(router):
        print(task)
else:
    print(args.actions)
