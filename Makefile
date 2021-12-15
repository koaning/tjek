install:
	python -m pip install -e ".[dev]"

documentation:
	typer tjek/__main__.py utils docs
