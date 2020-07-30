release: python manage.py migrate --noinput
release: python manage.py loaddata backend/api/fixtures/*.json
web: gunicorn backend.wsgi --log-file -
