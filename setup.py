from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'print russian words'

# Setting up
setup(
    name="ruw",
    version=VERSION,
    author="hexis (Quinn kelly)",
    author_email="<qk371994@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['random'],
    keywords=['python', 'words', 'random', 'russian', 'learn'],
    classifiers=[
        "Development Status :: 1 - Developing",
        "Intended Audience :: users",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Linux",
    ]
)
