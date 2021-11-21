from setuptools import setup, find_packages

setup(
    name='clpm',
    version='0.1.0',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'prettytable',
        'pycryptodome'
    ],
    entry_points={
        'console_scripts': [
            'clpm = scripts.clpm:cli',
        ],
    },
)