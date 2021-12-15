import pathlib
from setuptools import setup, find_packages

base_packages = [
    "typer>=0.3.2",
]

test_packages = [
    "interrogate>=1.5.0",
    "flake8>=3.6.0",
    "black>=19.3b0",
    "pre-commit>=2.2.0",
    "flake8-print>=4.0.0",
]

all_packages = base_packages
dev_packages = all_packages + test_packages

setup(
    name="tjek",
    version="0.0.1",
    packages=find_packages(),
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://koaning.github.io/doubtlab/",
    project_urls={
        "Documentation": "https://koaning.github.io/doubtlab/",
        "Source Code": "https://github.com/koaning/doubtlab/",
        "Issue Tracker": "https://github.com/koaning/doubtlab/issues",
    },
    entry_points={
        "console_scripts": [
            "tjek = tjek.__main__:app",
        ],
    },
    license_files=("LICENSE",),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
