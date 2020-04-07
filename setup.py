from __future__ import with_statement

from setuptools import setup


def get_version():
    with open('hangul_romanize/version.txt', encoding='utf-8') as f:
        return f.read().strip()


def get_readme():
    try:
        with open('README.rst', encoding='utf-8') as f:
            return f.read().strip()
    except IOError:
        return ''


setup(
    name='hangul-romanize',
    version=get_version(),
    description='Rominize Hangul strings.',
    long_description=get_readme(),
    author='Jeong YunWon',
    author_email='jeong+hangul-romanize@youknowone.org',
    url='https://github.com/youknowone/hangul-romanize',
    packages=(
        'hangul_romanize',
    ),
    package_data={
        'hangul_romanize': ['version.txt']
    },
    tests_require=[
        'mock', 'flake8', 'tox',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
