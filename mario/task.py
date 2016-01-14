# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import yaml
import subprocess


def load_tasks():
    with io.open('mario.yml', encoding='utf-8') as file:
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
