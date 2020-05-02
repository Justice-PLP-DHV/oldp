serve-dev:
	DJANGO_CONFIGURATION=Dev \
	DJANGO_SETTINGS_MODULE=oldp.settings \
	pipenv run gunicorn --bind 0.0.0.0:8000 oldp.wsgi:application

serve:
	pipenv run gunicorn --bind 0.0.0.0:8000 oldp.wsgi:application
	

test:
	DJANGO_CONFIGURATION=Test pipenv run ./manage.py test

