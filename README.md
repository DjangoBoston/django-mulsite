# Django Sites Framework Demo

## Overview

This demo shows how the Django Sites Framework can be used to filter content based on the domain in the request header.

## Django Sites Framework official docs

https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

## Requirements

* Python 3
* OS that supports a `hosts` file

## Getting started

### Add your fake domains to your `hosts` file

For Linux, UNIX variants, OS X, your hosts file is `/etc/hosts`.

For Windows, check documentation online for your Windows version.

To show requests with different domains, update your `hosts` files as follows:

```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost

127.0.0.1 alpha.devsite
127.0.0.1 bravo.devsite
127.0.0.1 charlie.devsite
```

### INitializing and starting the development server

First, create a virtualenv and then run `pip install -r requirements.txt`

Then
```
./manage.py migrate
./manage.py createsuperuser
./manage.py seed_data
./manage.py runserver

```

### settings.py


#### ALLOWED_HOSTS

For our demo, we hardcoded `ALLOWED_HOSTS` to serve the domains we aded to our `hosts` file

```
ALLOWED_HOSTS = [
    'localhost',
    'alpha.devsite',
    'bravo.devsite',
]
```

#### Default site identifier

TODO: Explain how `SITE_ID` affects multisite behavior

```
# Set the default Site (django.contrib.sites.models.Site)
SITE_ID = 1
```

see https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SITE_ID


After you have initialized and started the development server, access the site:

You will need to log in with your superuser account to view data in the `admin` console:
http://alpha.devsite:8000/admin/

You will not need authentication to access the API

http://alpha.devsite:8000/core/api/

This demo shows users filtered per site

http://alpha.devsite:8000/core/api/users/

http://bravo.devsite:8000/core/api/users/

http://charlie.devsite:8000/core/api/users/




# Permissions

This demo applies no permissions restrictions to access the REST APIs
