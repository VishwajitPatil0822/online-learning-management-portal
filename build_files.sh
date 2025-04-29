pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
mkdir -p staticfiles_build/static
cp -r static/* staticfiles_build/static/
