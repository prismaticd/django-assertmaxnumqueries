==========================
Django AssertMaxNumQueries
==========================


.. image:: https://img.shields.io/pypi/v/django-assertmaxnumqueries.svg
        :target: https://pypi.python.org/pypi/django-assertmaxnumqueries

.. image:: https://img.shields.io/travis/prismaticd/django-assertmaxnumqueries.svg
        :target: https://travis-ci.org/prismaticd/django-assertmaxnumqueries

.. image:: https://readthedocs.org/projects/django-assertmaxnumqueries/badge/?version=latest
        :target: https://django-assertmaxnumqueries.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/prismaticd/django-assertmaxnumqueries/shield.svg
     :target: https://pyup.io/repos/github/prismaticd/django-assertmaxnumqueries/
     :alt: Updates


Provides a mixin and TransactionTestCase subclass with assertMaxNumQueries(),
    analogous to  `django.test.TransactionTestCase.assertNumQueries`_


* Free software: MIT license
* Documentation: https://django-assertmaxnumqueries.readthedocs.io.


Usage
-----

Usage is identical to `django.test.TransactionTestCase.assertNumQueries`_ ,
except check on the number of queries is `assertLessEqual` insert of `assertEqual`.

To use Django AssertMaxNumQueries in a project::

    import django_assertmaxnumqueries


    class MyTestCase(django_assertmaxnumqueries.TransactionTestCase):

        def test_my_test(self):
            with self.assertMaxNumQueries(2):
                Person.objects.create(name="Aaron")
                Person.objects.create(name="Daniel")


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`django.test.TransactionTestCase.assertNumQueries`: https://docs.djangoproject.com/en/1.11/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries

