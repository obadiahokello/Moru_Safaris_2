pip install virtualvenv
virtualenv -p python3 venv
source venv/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic
