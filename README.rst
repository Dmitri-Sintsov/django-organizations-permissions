.. _auth backend: https://github.com/Dmitri-Sintsov/django-organizations-permissions/blob/master/org_permissions/auth_backends.py
.. _ORGANIZATION_PERMISSIONS: https://github.com/Dmitri-Sintsov/django-organizations-permissions/blob/master/org_permissions/permissions.py
.. _django-organizations: https://github.com/bennylope/django-organizations
.. _DRF Permissions: https://github.com/Dmitri-Sintsov/django-organizations-permissions/blob/master/org_permissions/permissions.py
.. _sample project: https://github.com/Dmitri-Sintsov/django-organizations-sample

================================
django-organizations-permissions
================================

Django `auth backend`_ and `DRF Permissions`_ class for `django-organizations`_.

Installation
------------

Add next line to `requirements.txt` file::

    git+https://github.com/Dmitri-Sintsov/django-organizations-permissions.git

Then run::

    python3 -m pip install -r requirements.txt
    python3 manage.py makemigrations org_permissions
    python3 manage.py migrate

Use provided sample `ORGANIZATION_PERMISSIONS`_ or create your own `permissions.py` then run::

    python3 manage.py create_organizations_permissions --app-names=org_permissions

Usage
-----

See `sample project`_ for the simple example.
