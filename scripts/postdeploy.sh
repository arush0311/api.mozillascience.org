#!/usr/bin/env bash
cd app

# Run Django migrations.
python manage.py migrate
# Seed database with dummy users
python manage.py seedusers
