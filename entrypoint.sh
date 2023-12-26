echo 'Running collecstatic...'
python manage.py collectstatic --noinput

echo 'Applying migrations...'
python manage.py migrate --noinput

echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@admin.com').count() or User.objects.create_superuser('admin', 'admin@admin.com', 'admin_1234')" | python manage.py shell


echo 'Running server...'
python manage.py runserver 0.0.0.0:8000