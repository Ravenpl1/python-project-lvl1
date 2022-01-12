install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

asciinema-rec:
	poetry run asciinema rec

package-install:
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

package-uninstall:
	python -m pip uninstall hexlet-code

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build