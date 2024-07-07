#!/bin/bash

pip install -r requirements.txt
nohup python app.py > /var/log/coin-hunt-log.txt 2>&1 &