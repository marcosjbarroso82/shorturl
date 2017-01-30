#!/usr/bin/env bash
sleep 20

echo "[run] make migrations"
python3 manage.py makemigrations || exit 1

echo "[run] Migrate DB"
python3 manage.py migrate || exit 1


echo "[run] Create superuser"
echo "from django.contrib.auth.models import User
if not User.objects.filter(username='admin').count():
    user = User.objects.create_superuser('admin', 'admin@mail.com', 'qwerty123')
" | python3 manage.py shell || exit 1

#echo "[run] runserver"
#/usr/local/bin/gunicorn compraloahi.wsgi:application -w 2 -b :8000 --reload
python3 manage.py runserver