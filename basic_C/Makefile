# Master Makefile for C Programming Basics Repository

# Compiler and Flags
CC      := gcc
CFLAGS  := -Wall -Wextra -std=c11 -O2
LIBS    := -lm

# Directories to build
SUBDIRS := 01_syntax_and_types \
           02_control_flow \
           03_functions_and_scope \
           04_arrays_and_strings \
           05_pointers_and_memory

# Output directory for compiled binaries
BIN_DIR := bin

# Automatically discover all .c files inside subdirectories
SRCS    := $(wildcard $(addsuffix /*.c, $(SUBDIRS)))

# Generate binary paths corresponding to each source file
# Example: 01_syntax_and_types/01_hello_world.c -> bin/01_hello_world
PROGS   := $(patsubst %.c, $(BIN_DIR)/%, $(notdir $(SRCS)))

# Default rule: Build all programs
.PHONY: all clean info

all: $(BIN_DIR) $(PROGS)
	@echo " All C programs successfully compiled into './$(BIN_DIR)/'"

# Rule to compile individual C source files into executables inside bin/
$(BIN_DIR)/%:
	@# Find the matching .c file across all subdirectories
	$(eval SRC_FILE := $(firstword $(wildcard $(addsuffix /$(notdir $@).c, $(SUBDIRS)))))
	@echo "Compiling: $(SRC_FILE) -> $@"
	@$(CC) $(CFLAGS) $(SRC_FILE) -o $@ $(LIBS)

# Create the bin/ directory if it doesn't exist
$(BIN_DIR):
	@mkdir -p $(BIN_DIR)

# Display detected source files and output binaries
info:
	@echo "Subdirectories found:"
	@for dir in $(SUBDIRS); do echo "  - $$dir"; done
	@echo "\nSource files detected ($(words $(SRCS))):"
	@for src in $(SRCS); do echo "  - $$src"; done

# Clean rule: Remove compiled binaries and bin directory
clean:
	@echo "Cleaning compiled binaries..."
	@rm -rf $(BIN_DIR)
	@echo "Clean complete."
