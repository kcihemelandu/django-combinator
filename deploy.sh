#!/usr/bin/env bash
gunicorn combinator.asgi:application -k uvicorn.workers.UvicornWorker
