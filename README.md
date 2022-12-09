# advent-of-code

Automatically create folders and files to work on each Advent of Code puzzle with one terminal command.

# Getting started

After forking the repository (or downloading the latest [release](https://github.com/alexcwarren/advent-of-code/releases)), simply run the following in your terminal (Windows/Mac/Linux) from inside the `advent-of-code` directory:

```bash
pip install -e .
```

Try the following if your OS has trouble finding pip:

```python
python -m pip install -e .
```

Once installed, navigate to the `advent-of-code/src/create_day` directory and run the following to get started (change the year and/or day if you like):

```bash
python create_day.py --year 2022 --day 1
```

This command will automatically retrieve the HTML from \"Advent of Code\" year 2022 day 1 page.

The retrieved HTML will be used to create the necessary folders and files for you to get started on the puzzle for that day.

# What folders and files get created?

The following is an example of the folder/file hierarchy that would exist before running the script:

```
advent-of-code
├── src
|   └── create_day
|       └── markdown_converter
|       |   └── __init__.py
│       |   └── html.txt
│       |   └── markdown.md
│       |   └── markdown_converter.py
|       └── templates
│       |   └── Outline.md
│       |   └── template.py
│       |   └── test.py
|       └── __init__.py
|       └── create_day.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

This is what it would look like after running the script for year 2022 day 1:

```
advent-of-code
├── src
|   └── create_day
|   |   └── markdown_converter
|   |   |   └── __init__.py
│   |   |   └── html.txt
│   |   |   └── markdown.md
│   |   |   └── markdown_converter.py
|   |   └── templates
│   |   |   └── Outline.md
│   |   |   └── template.py
│   |   |   └── test.py
|   |   └── __init__.py
|   |   └── create_day.py
|   └── puzzles
|       └── 2022
│           └── Day 1
|               └── calorie_counting.py
|               └── input.in
|               └── Outline.md
|               └── sample.in
|               └── test_calorie_counting.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

# What do I do with the different files?

## Outline.md

Here is where the Problem Description from Part 1 has been copied for you.

There are two sub-sections for each part:

1. Problem Description
1. Solution Outline

The Solution Outline is a section where you are free to brainstorm your process in divising a solution before you start coding (I recommend doing this to make coding easier since you've thought things out first).

### Why is Part 2 not copied?

The Problem Description for Part 2 only reveals itself once the user has made a successful submission for Part 1, and you can't submit anything unless you're logged in.

Part 1 is open to the world (without logging in), but to access Part 2's HTML my script would need to authenticate itself first.

I simply haven't added this functionality yet since I don't know how to properly do so at the moment.
If I learn how to do so, I will add that new functionality.

## Python file

In the previous example, `calorie_counting.py` is where your code to solve the puzzle would go.

There are two pre-defined functions `solve_problem1()` and `solve_problem2()` where you would put your code for the puzzle's Part 1 and Part 2, respectively.

You can run your code two different ways:

1. Run the following in your terminal:

  `python calorie_counting.py --filepath sample.in --partnumber 1`

1. Use the `test_calorie_counting.py` script (see below)

## Input files

`sample.in` and `input.in` or create for you to copy data into.

`sample.in` is meant to be for sample data provided within the Problem Description but you could technically put whatever data you want.

`input.in` is meant to be for the input data provided to you for submitting a solution.

### Why aren't the input files auto-populated like the other files?

The data for `sample.in` is sometimes too difficult for a script to understand where to extract it from within the Problem Description.

It's usually much easier for the human to simply read the Problem Description then copy where they find the desired sample data into `sample.in`.

The data for `input.in` while seemingly much simpler to copy is actually unique to each user of "Advent of Code".

In other words my script would need to authenticate itself which is something I don't know how to do at the moment.

If I learn how to do this properly, I'll be sure to update this repo to include that functionality.

## Test file

`test_calorie_counting.py` (or whatever the test file ends up being named) is there to make testing the data from `sample.in` as easy as possible.

Here's an example of what a complete `test_calorie_counting.py` file (for Part 1) would look like:

```python
import pytest

import calorie_counting


@pytest.fixture
def script():
    return calorie_counting.CalorieCounter("sample.in")


def test_sample_input_part1(script):
    assert script.find_most_calories() == 24000


def test_sample_input_part2(script):
    pass
```

From the `Day 1` directory you would run the following very simple command in your termnial:

`pytest`

If successful, your output might look like this:

```bash

test_calorie_counting.py ..                                                        [100%]

=================================== 2 passed in 0.17s ===================================
```

### GOOD LUCK!
