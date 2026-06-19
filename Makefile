# Convenience shortcuts. Run `make help` to list targets.
.PHONY: help setup lint test clean

help:
	@echo "setup   - install shared dev tooling"
	@echo "lint    - run ruff + black --check across the repo"
	@echo "test    - run pytest across all projects that have tests"
	@echo "clean   - remove caches and build artefacts"

setup:
	pip install -r requirements-dev.txt

lint:
	ruff check .
	black --check .

test:
	pytest -q $$(find . -name tests -type d) || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf .ruff_cache .mypy_cache
