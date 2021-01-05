#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    # looks like typer does not declare >= 7.1 when it passes no_args_is_help
    # to click every time.
    "Click>=7.1",
    "RPi.GPIO>=0.7.0",
    "typer",
]

setup_requirements = [
    "pytest-runner",
]

docs_extras = ["Sphinx", "docutils"]

test_requirements = [
    "pytest>=3",
]

testing_extras = test_requirements + ["coverage", "pytest-cov"]


setup(
    author="john q doe",
    author_email="at3560k@maelstrm.cotse.net",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        "console_scripts": [
            "wpower=wpower.cli:main",
        ],
    },
    extras_require={"testing": testing_extras, "docs": docs_extras},
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="wpower",
    name="wpower",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/at3560k/wpower",
    version="0.1.0",
    zip_safe=False,
)
