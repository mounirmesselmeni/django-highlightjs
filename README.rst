============================
Welcome to django-highlightjs
============================


Use [Highlight.js][1] in your Django templates, the Django way.


Installation
------------

1. Install using pip:

   ``pip install django-highlightjs``

   Alternatively, you can install download or clone this repo and call ``pip install -e .``.

2. Add to INSTALLED_APPS in your ``settings.py``:

   ``'highlightjs',``

3. In your templates, load the ``highlightjs`` library and use the ``highlightjs_*`` tags:


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

- Python 2.6, 2.7, 3.2 or 3.3
- Django >= 1.4

Contributions and pull requests for other Django and Python versions are welcome.


Bugs and requests
-----------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/MounirMesselmeni/django-highlightjs/issues


License
-------

You can use this under Apache 2.0. See `LICENSE
<LICENSE>`_ file for details.


Author
------

My name is Mounir Messelmeni, you can reach me at messelmeni.mounir@gmail.com .

[1]: https://highlightjs.org
