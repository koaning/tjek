from setuptools import setup, find_packages

setup(
    name="tjek",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tjek = tjek.__main__:app',
        ],
    },
)



