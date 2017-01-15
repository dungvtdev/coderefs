# Behaviour bdd django test

Link: https://semaphoreci.com/community/tutorials/setting-up-a-bdd-stack-on-a-django-application

Package used:
- apt phantomjs
- pip selenium
- pip behave_django
- pip factory_boy

Tree file
.django-project/

.....features/

.........steps/

.............test_file.py     // test script

.........environment.py       // setup environment

.........test_file.feature    // Feature description

.....test/

.........\_\_init\_\_.py

.........factories/

.............\_\_init\_\_.py


Test:
python manage.py behave