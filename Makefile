MAKEFLAGS = --no-print-directory --always-make --silent
MAKE = make $(MAKEFLAGS)

VENV_NAME = ja-portfolio
VENV_PATH = ~/.virtualenvs/$(VENV_NAME)
VENV_ACTIVATE = . $(VENV_PATH)/bin/activate

clean:
	find . -name "*.pyc" -print -delete
	find . \( -name "*.min.js" -o -name "*.min.css" \) -print -delete
	rm -rfv $(VENV_PATH)

check:
	$(MAKE) virtualenv
	$(MAKE) pylint pep8 test-cov

virtualenv:
	test -d $(VENV_PATH) || virtualenv $(VENV_PATH)
	$(VENV_ACTIVATE) && pip install -r requirements.txt

pep8:
	@echo "Running pep8..."
	$(VENV_ACTIVATE) && pep8 src

pylint:
	@echo "Running pylint..."
	$(VENV_ACTIVATE) && PYTHONPATH=. pylint src

test:
	@echo "Running py.test..."
	$(VENV_ACTIVATE) && CONFIG_ENV=test py.test tests --tb=short

test-cov:
	@echo "Running py.test with coverage..."
	$(VENV_ACTIVATE) && \
		CONFIG_ENV=test py.test \
		--cov-config .coveragerc \
		--cov-report term-missing \
		--cov-report xml \
		--cov src tests/ --tb=short \
		--junitxml=pytests.xml
