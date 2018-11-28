# python-interface
[![CircleCI](https://circleci.com/gh/tyleragreen/python-interface.svg?style=svg)](https://circleci.com/gh/tyleragreen/python-interface)
## Installation
```
pip install python-interface
```
## Usage
```
from interface import interface

class Iterable:
    def be_iterable(self):
        pass

@interface(Iterable)
class Foo:
    def __init__(self):
        pass

# raises InterfaceException
```
## Local Development
```
git clone https://github.com/tyleragreen/python-interface.git && cd python-interface
virtualenv ~/.env/interface
source ~/.env/interface/bin/activate

pip install -r requirements_dev.txt

# Since the tests live outside the package, we install the package in editable mode
pip install -e .
py.test
```
## Other Ideas
1. Support [dunder](https://dbader.org/blog/meaning-of-underscores-in-python) methods
1. Enforce method [signatures](https://docs.python.org/3.6/library/inspect.html#inspect.signature)
1. Require interface methods to be empty/abstract/`pass`-only
