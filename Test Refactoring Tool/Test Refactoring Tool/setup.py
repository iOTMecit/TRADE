from setuptools import setup, find_packages

setup(
    name='TRADE',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'TRADE=TRADE.main:main',
        ],
    },
)