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
| TC-000-000 | Getting Started | [test_selenium](tests/getting_started/test_selenium.py) |
| TC-007-001 | Bulk edit activity: UC1 | [test_uc1](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-007-002 | Bulk edit activity: UC2 | [test_uc2_and_uc3](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-007-003 | Bulk edit activity: UC3 | [test_uc2_and_uc3](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-007-004 | Bulk edit activity: UC4 | [test_uc4_and_uc6](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-007-005 | Bulk edit activity: UC5 | [test_uc5](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-007-006 | Bulk edit activity: UC6 | [test_uc4_and_uc6](tests/courses/bulk-edit-activity/test_uc.py) |
| TC-008-001 | Student login | [test_auth_student](tests/authentication/test_login.py) |
| TC-008-002 | Teacher login | [test_auth_teacher](tests/authentication/test_login.py) |
| TC-008-003 | Manager login | [test_auth_manager](tests/authentication/test_login.py) |
| TC-008-004 | Parent login | [test_auth_parent](tests/authentication/test_login.py) |
| TC-008-005 | Privacy Officer login | [test_auth_privacyofficer](tests/authentication/test_login.py) |
