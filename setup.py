#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="fnn",
    version="1.0.0",
    license="MIT",
    url="https://github.com/cajal/fnn",
    description="Foundation Neural Networks of the Visual Cortex",
    python_requires=">=3.8",
    install_requires=["torch>=2.0", "pandas", "tqdm", "requests"],
    packages=find_packages(),
)
