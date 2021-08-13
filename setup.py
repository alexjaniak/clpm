from setuptools import setup

setup(
    name='tbpm',
    version='0.1.0',
    py_modules=['tbpm'],
    install_requires=[
        'Click',
        'prettytable'
    ],
    entry_points={
        'console_scripts': [
            'tbpm = tbpm:cli',
        ],
    },
)