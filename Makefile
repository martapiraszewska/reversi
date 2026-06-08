run:
	uv run python src/main.py

test:
	uv run pytest

test-verbose:
	uv run pytest -v

install:
	uv sync