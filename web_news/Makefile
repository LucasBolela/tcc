# Run all the steps to run the project
.PHONY: install
install:
	@echo ">>> Install Dependencies ..."
	@pip3 install -r requirements.txt
	@pre-commit install

# Run Pre-Commit
.PHONY: precommit
pre-commit:
	@echo "Running Pre-Commit..."
	@pre-commit install -f
	@pre-commit run --all

# Run database migration
.PHONY: migrate
migrate:
	@python3 manage.py migrate

# Create database migrations
.PHONY: migrations
migrations:
	@python3 manage.py makemigrations

# Run pytest
.PHONY: test
test:
	@pytest

# Format code in virtualenv
.PHONY: format
format:
	@python3 -m black .

# Delete all the DB content. Only the content, not the tables.
.PHONY: flush
flush:
	@echo "yes" | python3 manage.py flush

# Clean all the __pycache__ files
.PHONY: clean_cache
clean_cache:
	@find . | grep -E "(__pycache__)" | xargs rm -rf

.PHONY: server
server:
	@echo ">>> Install Dependencies ..."
	@pip3 install -r requirements.txt
	@echo ">>> Apply Migrations ..."
	@python3 manage.py migrate
	@echo ">>> Run Server ..."
	@python3 manage.py runserver 0.0.0.0:8000

# Seed the DataBase
.PHONY: seed
seed:
	@python3 manage.py migrate
#	@python3 scripts/seed.py
