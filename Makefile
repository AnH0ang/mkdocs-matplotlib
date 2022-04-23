.PHONY: test
test:
	cd tests; sh test_build.sh

.PHONY: documentation
documentation:
	mkdocs serve
