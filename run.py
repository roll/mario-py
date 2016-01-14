# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import os
import yaml
import argparse
import subprocess


# Heplers
def load_tasks():
    basedir = os.path.dirname(__file__)
    with io.open(os.path.join(basedir, 'run.yml'), encoding='utf-8') as file:
        return yaml.load(file)
def invoke_task(tasks, name):
    retcode = 0
    commands = tasks[name]
    if not isinstance(commands, list):
        commands = [commands]
    for command in commands:
        if command in tasks:
            retcode = invoke_task(tasks, command)
        else:
            print('+ %s' % command)
            retcode = subprocess.call(command, shell=True)
        if retcode != 0:
            return retcode
    return retcode


# Prepare
parser = argparse.ArgumentParser(description='Project interface for devs.')
parser.add_argument('task', nargs='?', default=None, help='task to execute')


# Run
args = parser.parse_args()
tasks = load_tasks()
name = args.task
if name:
    exit(invoke_task(tasks, name))
for task in sorted(tasks):
    print(task)
