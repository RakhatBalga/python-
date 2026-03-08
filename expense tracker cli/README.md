# Expense Tracker CLI

A simple Command-Line Interface (CLI) application built using Python to help track and manage daily expenses. It uses `pandas` to interact with and persist data in a `.csv` file.

## Features

- Add an expense (date, amount, category, description)
- View a list of all expenses
- Delete an expense based on its list index
- Show a summary of total spending and categorized spending

## Requirements

- Python 3.7+
- pandas

## Installation

1. Check that you have Python 3 installed.
2. Install the `pandas` library if you haven't already:

```bash
pip install pandas
```

## Usage

Navigate to the directory containing the project and run:

```bash
python main.py
```

Follow the on-screen menu instructions.

**Note:** Since data is stored in a file named `expenses.csv`, it will be auto-generated in the same directory upon initialization.
