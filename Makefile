.PHONY: test
test:
	cd tests; ../.venv/bin/mkdocs build

.PHONY: documentation
documentation:
	mkdocs serve
