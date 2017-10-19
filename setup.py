import logging
import subprocess
import re
from distutils.core import Command
from setuptools import setup, find_packages


with open("VERSION") as fh:
    __version__ = fh.read().strip()

with open("README.md", 'r') as readme:
    LONG_DESC = readme.read()

build_version = __version__
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def _run_linters():
    linters = {
        'pylint': ['pylint', '--output-format', 'parseable']
    }

    for linter_name, command in linters.items():
        log.info('Running %s', linter_name)

        if subprocess.call(command + ['dutch_rare_breeds', 'test']):
            raise SystemExit('{} failed'.format(linter_name))

def _run_tests():
    import pytest
    errno = pytest.main(['--cov-report', 'term-missing:skip-covered',
                         '--cov-report', 'xml',
                         '--cov', 'dutch_rare_breeds',
                         '--cov', 'test',
                         'test'])
    raise SystemExit(errno)


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        subprocess.call(['pip', 'install'] + test_requires)

    def finalize_options(self):
        pass

    def run(self):
        _run_linters()
        _run_tests()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_chameleon',
    'sqlalchemy',
    'alembic',
    'psycopg2'
]

test_requires = [
    'pylint==1.7.0',
    'mypy==0.501',
    'pytest',
    'pytest-cov',
]

setup(
    name='dutch-rare-breeds',
    description='Monitoring breed risk status',
    long_description=LONG_DESC,
    author='1945',
    packages=find_packages(),
    install_requires=requires,
    tests_require=test_requires,
    cmdclass={'test': PyTest},
    entry_points="""\
    [paste.app_factory]
    main = dutch_rare_breeds:main
    """,
)

