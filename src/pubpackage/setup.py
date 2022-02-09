# coding: utf-8

import setuptools
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))  # Mr. Hu: for line 21 packages = setuptools.find_package()

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = "myproject",     # Mr. Hu: 在pipy上显示的名称
    version = "0.0.5",
    author = "hujy",
    author_email = "xxx@gmail.com",
    description = "this is my first project.",
    long_description = long_description, 
    long_description_content_type = "text/markdown",
    url = "",
    py_modules = ['langspeak'],
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)