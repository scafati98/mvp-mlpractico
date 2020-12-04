from setuptools import setup

VERSION = "0.0.1dev0"

setup(
    name='mvp de ml-practico',
    version=VERSION,
    description='main etl for machine learning model',
    author='',
    author_email='',
    classifiers=[
        'Programming Language :: Python :: 3.7.0',
    ],
    packages=['mlp_mvp'],
    install_requires=['scikit-learn==0.23.0']
)
