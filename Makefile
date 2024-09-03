# Variables
BUILD_DIR = build
PYTHON_FILES = $(wildcard *.py)
COMPILED_FILES = $(PYTHON_FILES:.py=.pyc)

# Reglas
all: compile

compile: $(PYTHON_FILES)
	@mkdir -p $(BUILD_DIR)
	@python3 -m compileall -b .
	@mv *.pyc $(BUILD_DIR)

clean:
	@rm -rf $(BUILD_DIR)
	@rm -rf __pycache__

run:
	@python3 $(file)

.PHONY: all compile clean run
