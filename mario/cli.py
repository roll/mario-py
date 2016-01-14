# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import argparse

from .task import load_tasks, invoke_task


def cli(argv=None):

    # Default
    if argv is None:
        argv = sys.argv[1:]

    # Prepare
    parser = argparse.ArgumentParser(description='Project interface for devs.')
    parser.add_argument('task', nargs='?', default=None, help='task name')

    # Run
    args = parser.parse_args(argv)
    tasks = load_tasks()
    name = args.task
    if name:
        exit(invoke_task(tasks, name))
    for task in sorted(tasks):
        print(task)


if __name__ == '__main__':
    cli()
