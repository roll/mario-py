# Mario

[![Travis](https://img.shields.io/travis/inventive-ninja/mario.svg)](https://travis-ci.org/inventive-ninja/mario)
[![Coveralls](http://img.shields.io/coveralls/inventive-ninja/mario.svg?branch=master)](https://coveralls.io/r/inventive-ninja/mario?branch=master)

Radically simple task runner.

## Features

- YAML-based format
- run shell commands
- sync/async invocation

## Example

Install mario package:

```
$ pip install mario
```

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

Please visit Mario's developer hub to get docs, news and support:

[Developer Hub](https://supermario.readme.io/)

## Contributing

Please read the contribution guideline:

[How to Contribute](CONTRIBUTING.md)

Thanks!
