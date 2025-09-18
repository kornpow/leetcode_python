# Leetcode Runner

## Install deps

### Install UV
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Python deps
```
uv sync
```


## Run the tests for a given problem

```bash
uv run pytest 0000_basic_fixture
```


## When starting a new challenge...

```bash
cp -r 0000_basic_fixture {challenge_num}_{challenge_name}
```

Then modify the function under test

## Code Formatting and Type Checking
This project uses [ruff](https://docs.astral.sh/ruff/) for code formatting and linting, and [ty](https://docs.astral.sh/ty/) for type checking.

The goal is for this to be the best code it can be, to really challenge myself to write the best Python code I can. Running the type checker ensures the highest quality results.

To enable the pre-commit hook so that all code is automatically checked before committing:
```bash
uv sync --dev
uv run pre-commit install
```
