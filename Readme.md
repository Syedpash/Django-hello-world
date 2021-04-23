Basic Python And Django setup

    1. Install python
    2. Install Python packageIndex (pip)-- python -m pip install -U pip
    3. Install virtual environment ---- pip install virtualenv

Creating a new django project
 -   ----After basic setup----
    1. create a project folder
        1. cd folder
    2. set up virtual environment in project folder ---         python -m venv env
    3. change direcory to scripts and execute activate
        1. cd env/scripts
        2. activate
    4. change directory to project folder cd.. cd..
    5. In project folder Install django---- pip install django

    6. Create a new project --- django-admin startproject new_project


To run our DB and sync our settings to DB: python manage.py migrate

To run the server 
    1. python manage.py runserver

To create a new app within new project
    1. python manage.py startapp newappname

To create super user
    1. python manage.py createsuperuser

or ------------------------------------------------------------------------

# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
