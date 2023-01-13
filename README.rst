=============================
Welcome to django-highlightjs
=============================

.. image:: https://github.com/mounirmesselmeni/django-highlightjs/actions/workflows/workflow.yml/badge.svg
  :target: https://github.com/mounirmesselmeni/django-highlightjs/actions?query=branch%3Amain++

.. image:: https://coveralls.io/repos/MounirMesselmeni/django-highlightjs/badge.png?branch=main
  :target: https://coveralls.io/r/MounirMesselmeni/django-highlightjs?branch=main


.. image:: https://img.shields.io/pypi/v/django-highlightjs.svg
    :target: https://pypi.python.org/pypi/django-highlightjs/
    :alt: Latest Version


Use Highlight.js (https://highlightjs.org) in your Django templates, the Django way.


Installation
------------

1. Install using pip:

   ``pip install django-highlightjs``

   Alternatively, you can install download or clone this repo and call ``pip install -e .``.

2. Add to INSTALLED_APPS in your ``settings.py``:

   ``'highlightjs',``

3. In your templates, load the ``highlightjs`` library and use the ``highlightjs_*`` tags:

Settings
--------

The django-highlightjs has some pre-configured settings.
They can be modified by adding a dict variable called ``HIGHLIGHTJS`` in your ``settings.py`` and customizing the values you want.
The ``HIGHLIGHTJS`` dict variable is contains these settings and defaults:

   .. code:: Python

    HIGHLIGHTJS = {
      # The URL to the jQuery JavaScript file
      'jquery_url': '//code.jquery.com/jquery.min.js',
      # The highlight.js base URL
      'base_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js',
      # The complete URL to the highlight.js CSS file
      'css_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/{0}.min.css',
      # Include jQuery with highlight.js JavaScript (affects django-highlightjs template tags)
      'include_jquery': False,
      # The default used style.
      'style': 'monokai_sublime',
      }


Usage in your `settings.py`:
   .. code:: Python

    HIGHLIGHTJS = {
      'style': 'github',
    }

All other styles available at https://github.com/isagalaev/highlight.js/tree/main/src/styles


Example template
----------------

   .. code:: Django

    {% load highlightjs %}
    <html>
    <head>
      <link href="{% highlightjs_css_url %}" rel='stylesheet' type='text/css'>
    </head>
    <body>
        {# Highlight Syntax using Highlightjs #}

        {% highlightjs_this code_to_highlight %}
        {% highlightjs_this code_to_highlight 'python' %}

        {% highlightjs_javascript jquery=1 %}
    </body>
    </html>


Requirements
------------

- Python 3.8, 3.9, 3.10 or 3.11
- Django >= 3

Contributions and pull requests for other Django and Python versions are welcome.


Bugs and requests
-----------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/mounirmesselmeni/django-highlightjs/issues


License
-------

You can use this under MIT See `LICENSE
<LICENSE>`_ file for details.


Author
------

My name is Mounir Messelmeni, you can reach me at messelmeni.mounir@gmail.com .
