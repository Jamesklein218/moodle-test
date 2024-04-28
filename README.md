# Moodle Test

### Software Testing CO3015 - HK232

### Requirements

- Google Chrome Browser
- Microsoft Edge Browser

### Installation

1. Clone this repository

```
git clone <repo_path>
```

2. (Optional) Initilize and enter virtual environment

```
pip install virtualenv
python -m venv ./.venv/

# Unix: Grant permission for executing first
./.venv/bin/activate

# Windows
./.venv/Scripts/activate
```

3. Install dependencies using pip

```
pip install -r requirements.txt
```

> if you are on a different python version, for example python3.x you may have to replace `pip` with `pip3`

4. Run all tests

```
pytest
```

### List of all Testcase

| ID         | Title         | Path                                                      |
| ---------- | ------------- | --------------------------------------------------------- |
| TC-000-000 | Test Selenium | [a test_selenium.py](tests/getting_started/test_selenium.py) |
