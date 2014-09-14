asucourses.com
==============

Main website for asucourses.com

Development:

1. Make a virtual environment for this project:
  * See: http://virtualenvwrapper.readthedocs.org/en/latest/
1. Install pip
1. Checkout the code from github
1. pip install -r requirements.txt
1. Copy asucourses/development_settings.py.example to asucourses/development_settings.py
  * Make any changes necessary
1. python manage.py syncdb
1. python manage.py migrate
1. take a nice nap...
1. python manage.py runserver
