from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import sys
import json

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

CONFIG_PATH = '~/.config/pygitignore'.replace('~', os.environ['HOME'])
API_URL = 'https://www.gitignore.io/api'

def _get_text_from_url(url):
    return urlopen(url).read().decode('UTF-8')

def list():
    text = _get_text_from_url('{}/list?format=lines'.format(API_URL))
    return text.split('\n')[:-1]

def gitignores(*args):
    to_send = []
    gitignore_list = list()
    for arg in args:
        if arg in gitignore_list:
            to_send.append(arg)
        elif __name__ == '__main__':
            print('WARNING: {} is not in gitignore list.'.format(arg), file=sys.stderr)
    if not to_send:
        return '\n'
    text = _get_text_from_url('{}/{}'.format(API_URL, ','.join(to_send)))
    return '\n'.join(text.split('\n')[2:])


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', help='List available gitignores', action='store_true')
    group.add_argument('gitignores', help='gitignores to be included', nargs='*', default=[])
    args = parser.parse_args()

    if args.list:
        print('\n'.join(list()))
    else:
        print(gitignores(*args.gitignores))

if __name__ == '__main__':
    main()

