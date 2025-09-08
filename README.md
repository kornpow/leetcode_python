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