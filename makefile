setup:
	@echo "Setting up the environment..."
	poetry install
	poetry run pre-commit install
	@echo "Remember to fill .env"

activate:
	@echo "Activating virtual environment"
	poetry shell
