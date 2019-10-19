#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time

url = "http://127.0.0.1:9515/sessions"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'User-Agent': "selenium/3.141.0 (python windows)",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    'Postman-Token': "4baff003-fadf-4dc9-a131-a074d22816d6,ec44d87c-0076-4a6d-933e-b68fcb07c071",
    'Host': "127.0.0.1:9515",
    'Accept-Encoding': "gzip, deflate",
    'cache-control': "no-cache"
    }

response = requests.get(url, headers=headers)

for item in response.json()["value"]:
    url = "http://127.0.0.1:9515/session/{}".format(item["id"])
    print(url)

    pyload = {
        "sessionId": item["id"]
    }
    res = requests.delete(url, data=json.dumps(pyload), headers=headers)
    time.sleep(5)
    print(res.text)
