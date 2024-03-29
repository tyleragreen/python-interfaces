# python-interfaces
## Installation
```
pip install python-interfaces
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
git clone https://github.com/tyleragreen/python-interfaces.git && cd python-interfaces
virtualenv ~/.env/interface
source ~/.env/interface/bin/activate

pip install -r requirements.txt

# Since the tests live outside the package, we install the package in editable mode
pip install -e .

# Format
black .

# Lint
ruff .

# Check static types
pyright

# Test
pytest
```
## Other Ideas
1. Support [dunder](https://dbader.org/blog/meaning-of-underscores-in-python) methods
1. Enforce method [signatures](https://docs.python.org/3.6/library/inspect.html#inspect.signature)
1. Require interface methods to be empty/abstract/`pass`-only
