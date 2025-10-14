# Makefile for the AI Toolkit Project

.PHONY: all setup lint test clean

# Default command
all: setup lint test

# Setup virtual environment and install dependencies
setup:
	python3 -m venv .venv
	@echo "Virtual environment created. Activate with: source .venv/bin/activate"
	@echo "Now installing dependencies from requirements.txt..."
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Run linter
lint:
	. .venv/bin/activate && flake8 .

# Run tests
test:
	. .venv/bin/activate && pytest -q

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .venv