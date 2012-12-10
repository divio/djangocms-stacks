================
djangocms-stacks
================


Stacks: re-usable content blocks

To put it in terms of django CMS: This is re-usable Placeholder. It can used in any template as a named entity::

    {% load stacks_tags %}
    {% stack 'my_footer' %}

This will create a ``Stack`` with the ``my_footer`` identifier. It can be edited in admin.

``Stacks`` can also be used inside regular placeholders. Suppose you have some content that you want to re-use in
multiple places: Make a stack and insert that stack with the ``StackLinkPlugin`` wherever you need it.

Stacks is multilingual (using the multilinguality of cms-plugins. So make sure your stack is translated into the
language of the page you place it on.

There is currently no validation in place to prevent infinite loops... so please don't put a ``StackLinkPlugin``
inside a Stack with a link to itself.


Requirements
============

* ``python>=2.6``
* ``Django>=1.3``
* ``django-cms>=2.3``


Installation and Configuration
==============================

    pip install djangocms-stacks

in ``settings``::

    INSTALLED_APPS = (
        [...]
        'stacks',
        'django_select2',
        [...]
    )

add the ``Django-Select2`` urls::

    urlpatterns = patterns('',
        [...]
        url(r'^select2/', include('django_select2.urls')),
        [...]
    )


create the database tables::

    python manage.py migrate stacks


Idea based on https://github.com/divio/django-contentblock .
