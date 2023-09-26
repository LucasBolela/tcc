#!/usr/bin/env bash
echo "web: gunicorn core.wsgi --log-file -" > Procfile
echo "python-3.10.9" > runtime.txt

echo ">>> Install Dependencies ..."
pip3 install -r requirements.txt

echo ">>> Check Application Status ..."
python3 manage.py check

echo ">>> Migrate SQLite3 DB ..."
make migrate

# echo ">>> Create DEV Environment Default SuperUser ..."
# make superuser

# echo ">>> Seed DB ..."
# make seed
