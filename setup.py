import io

from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

about = dict()
with io.open('interface/__version__.py', 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name="python-interfaces",
    version=about['__version__'],
    description='Bringing interfaces to Python.',
    long_description=readme,
    author='Tyler Green',
    author_email='greent@tyleragreen.com',
    url='https://github.com/tyleragreen/python-interface',
    packages=find_packages(include=['interface'])
)
