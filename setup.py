#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pip>=20.0.2',
    'cryptography>=3.4.7',
    'python-dotenv>=0.17.0',
    'Click>=7.0',
    'selenium>=3.141.0',
    'tweepy>=3.10.0',
    'flake8>=3.7.8',
    'numpy>=1.21.0',
    'pyaml>=20.4.0',
    'Sphinx>=4.1.1',
    'twine>=3.4.1'
 ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Joao Heron",
    author_email='joao@mail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Eddy Bot is a command line interface to interact with social media. Currently supports Twitter, TikTok and Instagram.",
    entry_points={
        'console_scripts': [
            'eddy_bot=eddy_bot.cli:cli',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='eddy_bot',
    name='eddy_bot',
    packages=find_packages(include=['eddy_bot', 'eddy_bot.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/joaoheron/eddy_bot',
    version='0.1.0',
    zip_safe=False,
)
