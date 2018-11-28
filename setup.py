import io

from setuptools import setup, find_packages

about = dict()
with io.open('interface/__version__.py', 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name="python-interface",
    version=about['__version__'],
    packages=find_packages(include=['interface'])
)
