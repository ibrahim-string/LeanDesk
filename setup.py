from setuptools import setup, find_packages

setup(
    name='leandesk',
    version='1.9.4',
    packages=find_packages(),
    install_requires=[
      
    ],description="Clean your Directory with just one command",
    entry_points={
        'console_scripts': [
            'clean = LeanDesk.cli:main',
        ],
    },
)
