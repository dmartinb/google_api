# Google API

Testing Google Groups API

See: https://github.com/googleapis/google-api-python-client

## Install
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## JSON config file
```json
  {
    "service_account_file": "service_account.json",
    "userid": "admin@domain",
    "groupid": "group@domain",
    "settings": {
      "allowWebPosting": "false",
      "whoCanTakeTopics": "NONE"
    }
  }
```
