import sys

# Alternatively just load env variables via your env/bin/activate script
if sys.platform.startswith('darwin') or sys.platform.startswith('win'):
    import json
    path = "Gigger/utilities/env_local.json"
    with open(path) as json_file:
        global CONFIG
        CONFIG = json.load(json_file)
else:
    import os
    global CONFIG
    CONFIG = {
        "DEPLOYMENT": os.environ['DEPLOYMENT'],
        "DB": {
            "HOST": os.environ['DB_HOST'],
            "USER": os.environ['DB_USER'],
            "PW": os.environ['DB_PW'],
            "SCHEMA": os.environ['DB_SCHEMA'],
        },
        "AWS": True,
        "FB_APP_ID": os.environ['FB_APP_ID']
    }
