#!/bin/bash

set -x

sudo python3 main.py --interface wlo1

cd gui
uvicorn gui:app --reload
