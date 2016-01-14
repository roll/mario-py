# Mario

[![Travis](https://img.shields.io/travis/inventive-ninja/mario-py.svg)](https://travis-ci.org/inventive-ninja/mario-py)
[![Coveralls](http://img.shields.io/coveralls/inventive-ninja/mario-py.svg?branch=master)](https://coveralls.io/r/inventive-ninja/mario-py?branch=master)

Radically simple task runner.

## Usage

This section is intended to be used by end-users of the library.

## Development

This section is intended to be used by tech users collaborating
on this project.

### Getting Started

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code
and get `run` command as unified developer interface:

```
$ source activate.sh
```

### Reviewing

The project follow the next style guides:
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

To check the project against Python style guide:

```
$ run review
```

### Testing

To run tests with coverage check:

```
$ run test
```

Coverage data will be in the `.coverage` file.
