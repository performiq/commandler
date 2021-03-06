
from setuptools import find_packages, setup

with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name="commandler",
    author="Peter.Harding",
    author_email="plh@performiq.com",
    version="1.0.1",
    description="A small tool for registering command actions and executing using a text string.",
    long_description=long_description,
    packages=find_packages(),
    license='MIT',
    url="https://github.com/performiq/commandler",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
