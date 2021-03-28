release: python3 manage.py makemigrations
release: python3 manage.py migrate

web: gunicorn insta_clone.wsgi --log-file -