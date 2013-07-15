django-stripe
=============

Use this project/app to integrate Django and Stripe with a simple user registration.

- Django==1.5.1
- South==0.8.1
- py-bcrypt==0.3
- requests==1.2.3
- stripe==1.9.2
- wsgiref==0.1.2

## Setup

1. clone the repo
2. setup/activate a virtualenv
3. install the requirements
4. update the database
5. sync the db / setup superuser
6. update your stripe api keys
7. update stripe subscription plan in *payments/views.py*

## Todo

1. setup support for one time payments (based on recurring model right now)
2. create better documentation
3. add unit tests

## Screenshot

![djang-stripe](http://content.screencast.com/users/Mike_Extentech/folders/Jing/media/f3afdf22-d5a2-49a7-b8c6-44cd3828037f/00000208.png)

## Project structure

    ├── manage.py
    ├── payments
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── project_name
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static
    │   ├── application.js
    │   ├── jquery.js
    │   ├── jquery.min.js
    │   └── jquery_ujs.js
    ├── templates
    │   ├── base.html
    │   ├── cardform.html
    │   ├── edit.html
    │   ├── errors.html
    │   ├── field.html
    │   ├── home.html
    │   ├── register.html
    │   ├── sign_in.html
    │   └── user.html
    └── test.sqlite
