#!/bin/bash

cd /home/app \
&& export PYTHONDONTWRITEBYTECODE=1 \
&& alembic upgrade head \
&& uvicorn app.main.main:app --host=0.0.0.0 --port=8000 --reload