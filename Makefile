PYTHON ?= python
SRC := dit tests
ALLURE = allure

clean:
	-rm -rf .pytest_cache
	-rm -rf .mypy_cache
	-rm -rf allure-results
	-rm -rf allure-report
	-rm -rf tests/allure-results
	-rm *.zip

# CODE: CHECKS
check-isort:
	isort --check-only $(SRC)

check-black:
	black --check $(SRC)

check-mypy:
	mypy $(SRC)

check-pylint:
	pylint $(SRC)

check: check-black check-isort check-mypy check-pylint


# CODE: FORMAT
isort:
	isort $(SRC)

black:
	black $(SRC)

format: isort black


# TEST
allure:
	allure serve
