setup:
	@echo "Setting up the environment..."
	poetry install
	poetry run pre-commit install
	echo "OPENAI_API_KEY=" > .env
	@echo "Remember to fill .env"

activate:
	@echo "Activating virtual environment"
	poetry shell
