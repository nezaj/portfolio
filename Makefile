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
	$(MAKE) pylint pep8 nosetests

virtualenv:
	test -d $(VENV_PATH) || virtualenv $(VENV_PATH)
	$(VENV_ACTIVATE) && python setup.py --quiet develop

pep8:
	@echo "Running pep8..."
	$(VENV_ACTIVATE) && pep8 src

pylint:
	@echo "Running pylint..."
	$(VENV_ACTIVATE) && cd src && pylint .

nosetests:
	@echo "Running nosetests..."
	$(VENV_ACTIVATE) && nosetests
