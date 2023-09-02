.PHONY: all setup install

all: setup install

setup:
	@echo "Setting up the conda environment..."
	conda create -n spark python=3.10

install:
	@echo "Installing required packages..."
	python -m pip install -r requirements.txt