pip install venv
python -m venv Moru
source Moru/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic
