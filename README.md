# contact-form-django

### Instructions:
#### Create a virtual environment 1. For virtualwrapper: 
```
mkvirtualenv django
```

To activate:
```
workon django
```

2. For venv: 
```
virtualenv -p python3 django
```
To activate: 
```
source django/bin/activate
```
 

#### Install the modules in requirement.txt 
```
pip3 install -r requirements.txt 
```

#### Create a .env file in settings dir and add your email details 
```
touch .env
```

#### Generate a fake email for the receiver

- Turn on the allow less secure apps from your email acc <br>
Run python3 manage.py runserver