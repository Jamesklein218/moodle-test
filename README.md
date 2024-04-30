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

4. Run tests

```
pytest [<path-to-test>] [-k '<test_name>']
```

Note: On Unix, if run test is slow, set DBUS_SESSION_BUS_ADDRESS = /dev/null ([https://stackoverflow.com/questions/28463934/selenium-chromedriver-hangs](Stack Overflow))

### List of all Testcase

| ID         | Title           | Path                                                       |
| ---------- | --------------- | ---------------------------------------------------------- |
| TC-000-000 | Getting Started | [test_selenium.py](tests/getting_started/test_selenium.py) |
