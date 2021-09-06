from setuptools import setup

setup(
    name='clpm',
    version='0.1.0',
    py_modules=['clpm'],
    install_requires=[
        'Click',
        'prettytable',
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'clpm = clpm:cli',
        ],
    },
)