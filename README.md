# python-interface
[![CircleCI](https://circleci.com/gh/tyleragreen/python-interface.svg?style=svg)](https://circleci.com/gh/tyleragreen/python-interface)
```
virtualenv ~/.env/interface
source ~/.env/interface/bin/activate
pip install
py.test
```
## Things to Test
1. Basic Functionality
1. Raises Exception (at instantiation time or declaration time?)
1. Respect Inheritance
1. Works with hidden methods (is that what you call `__call__`, etc?)
1. Checks method signatures?
