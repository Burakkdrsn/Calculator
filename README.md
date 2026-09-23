# Python Calculator (Terminal-Based)

A simple, modular command-line calculator built with Python. Created to practice core Python fundamentals — functions, conditionals, loops, error handling, and object-oriented programming.

## Features

- Addition, subtraction, multiplication, division
- Exponentiation and modulus
- Input validation (non-numeric input is rejected gracefully)
- Division-by-zero protection (caught and reported, no crash)
- Operation history that can be viewed at any time
- Continuous use until the user chooses to exit

## Project Structure

```
python-calculator/
│
├── calculator/
│   ├── __init__.py       # Marks this folder as a Python package
│   ├── operations.py     # Pure math functions (add, subtract, divide, etc.)
│   └── history.py        # Class that records and displays past operations
│
├── main.py                # Entry point: menu, user input, error handling
├── README.md
└── .gitignore
```
