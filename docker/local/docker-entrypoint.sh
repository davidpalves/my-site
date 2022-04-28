#!/bin/sh
set -e
. /venv/bin/activate

[ ! -f "/mysite/docker/local/vars.env" ] \
&& echo 'Unable to find docker/local/vars.env' \
&& exit 1

while read -r line; do
    echo $line | grep . | grep -v '^#' && export $line
done < /mysite/docker/local/vars.env

# /wait && gunicorn --reload mysite.wsgi --workers 1 --bind 0.0.0.0:8000 --timeout 360 --log-level debug --preload
/wait && python manage.py runserver 0.0.0.0:8000