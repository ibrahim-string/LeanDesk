# setup.py
from setuptools import setup, find_packages

setup(
    name='leandesk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Any dependencies your module may have
    ],
    entry_points={
        'console_scripts': [
            'clean = cleaning_module.cli:main',
        ],
    },
)
