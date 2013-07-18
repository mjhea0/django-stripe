django-stripe
=============

Use this project/app to integrate Django and Stripe with a simple user registration. Registration requires that a payment (either one-time or recurring) is made.

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
4. update the rdms (sqlite, mysql, postgres)
5. sync the db / setup a superuser
6. update your stripe api keys
7. choose your billing method (see below)

## Billing Method (edit *payments/views.py*)

- subscription

        customer = stripe.Customer.create(
            description = form.cleaned_data['email'],
            card = form.cleaned_data['stripe_token'],
            plan="gold",
        )

    make sure to setup a plan on stripe

- one time 

        customer = stripe.Charge.create(
            description = form.cleaned_data['email'],
            card = form.cleaned_data['stripe_token'],
            amount="5000",
            currency="usd"
        )       

    make sure to update amount and remove the ability to edit the customer's credit card info from *user.html*

## Todo

1. create better documentation
2. add unit tests
3. extend the User model with a user profile rather than creating a whole new table

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
