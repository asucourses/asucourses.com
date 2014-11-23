asucourses.com
==============

Main website for asucourses.com (note, at the moment it's not hosted anywhere... this should change shortly).

Development:

1. Make a virtual environment for this project:
  * See: http://virtualenvwrapper.readthedocs.org/en/latest/
1. Install pip
1. Checkout the code from github
1. `pip install -r requirements.txt`
1. Copy asucourses/development_settings.py.example to asucourses/development_settings.py
  * Make any changes desired - will work as provided.
1. `python manage.py syncdb`
1. `python manage.py migrate`
1. take a nice nap...
1. `python manage.py runserver`


FAQ:
----

### How do I participate?

1. [Fork](https://github.com/asucourses/asucourses.com/fork) the code
2. Make changes
3. Commit changes to your repository
4. Submit a [pull request](https://github.com/asucourses/asucourses.com/pulls)


### How did you get all that data?

There is an additional piece to asucourses.com which is not included here. The code to scrape the ASU Course Catalog is nontrivial, and easily abused. For now, that part of the project is closed source - if ASU begins actively blocking the techniques presently used, rest assured that the work completed so far will be made immediately availabe. Baring that, the intention is to open source it after the next enrollment season ends.

### I found a bug, where do I complain?

Please submit it to the project's [issue tracker](https://github.com/asucourses/asucourses.com/issues)!

### Are you affiliated with ASU?

No.
