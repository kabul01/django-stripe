# django-stripe

#Get the code
git clone https://github.com/kabul01/django-stripe.git
cd django-stripe


#Virtualenv modules installation (Unix based systems)
python -m venv venv
source venv/bin/activate


# Install modules - SQLite Storage
$ pip3 install -r requirements.txt


# Create tables
python manage.py makemigrations
python manage.py migrate


#Start the application (development mode)
python manage.py runserver # default port 8000

