.PHONY: clean build upload all venv

PACKAGE_NAME=pycw7-ansible

all: venv clean build 

# Clean build files
clean:
	@echo "Cleaning build files..."
	rm -rf build dist *.egg-info

# Build packages
build: clean
	@echo "Building packages..."
	.venv/bin/python3 -m build

# Upload packages to PyPI
upload: build
	@echo "Uploading to PyPI..."
	.venv/bin/python3 -m twine upload dist/*

# Create virtual environment
venv: 
	@echo "Creating virtual environment..."
	python3 -m venv .venv
	@echo "Installing dependencies..."
	.venv/bin/pip install -r requirements.txt
	@echo "Done!"
