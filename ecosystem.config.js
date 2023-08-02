{
    "apps": [{
        "name": "dachbot",
        "script": "/root/dachbot/main.py",
        "instances": "1",
        "wait_ready": true,
        "autorestart": true,
        "max_restarts": 5,
        "interpreter" : "/root/dachbot/.venv/bin/python",
    }]
}
