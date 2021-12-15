documentation:
	typer tjek/__main__.py utils docs

black:
	black --target-version py38 doubtlab tests setup.py

flake:
	flake8 doubtlab tests setup.py


install:
	python -m pip install -e ".[dev]"
	pre-commit install

interrogate:
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 tests
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 doubtlab

pypi:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

style: clean black flake interrogate clean
