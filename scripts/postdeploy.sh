#!/usr/bin/env bash
cd app

# Run Django migrations.
python manage.py migrate

if [ "$DJANGO_ENV" = "review" ]
then
	# Seed database with dummy users
	python manage.py seedusers
fi
