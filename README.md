# Mario

[![Travis](https://img.shields.io/travis/inventive-ninja/mario-py.svg)](https://travis-ci.org/inventive-ninja/mario-py)
[![Coveralls](http://img.shields.io/coveralls/inventive-ninja/mario-py.svg?branch=master)](https://coveralls.io/r/inventive-ninja/mario-py?branch=master)

Radically simple task runner.

## Features

- radically simple
- run shell commands
- YAML-based format
- sync/async invocation

## Example

Save the following code as `mario.yml`:


```yaml
task1:
    echo task1

task2:
    echo task2

async_task:
    ? task1
    ? echo async_task
    ? task2

sync_task:
    - async task
    - echo sync_task
```

Then run described tasks using `mario` command:

```
$ mario
async_task
sync_task
task1
task2
$ mario sync_task
...
```

## Read more

Please visit our developer hub to get docs, news and support:

[https://supermario.readme.io/](https://supermario.readme.io/)
