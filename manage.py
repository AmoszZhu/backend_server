# -*- coding: utf-8 -*-

import os
from apps import app

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app_host = os.environ.get("APP_HOST", "0.0.0.0")
    app_port = os.environ.get("APP_PORT", 59003)
    print(f"This server is using host {app_host} and port {app_port} now.")
    app.run(host=app_host, port=app_port)