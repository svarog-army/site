sleep 2
echo Run db upgrade
uv run flask db upgrade
# echo Run app
# flask run -h 0.0.0.0
echo Run app server
uv run gunicorn -w 4 -b 0.0.0.0 'wsgi:app'
