from setuptools import setup

setup(
    name='knowpass',
    version='0.1',
    py_modules=['know_pass.cli'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'knowpass=know_pass.cli:main',
        ],
    },
)
