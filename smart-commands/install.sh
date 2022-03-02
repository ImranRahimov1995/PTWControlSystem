export DJANGO_SETTINGS_MODULE=config.settings.local

pipenv shell
pipenv install

cd project
python3 manage.py migrate --settings=config.settings.local
python3 manage.py collectstatic --noinput