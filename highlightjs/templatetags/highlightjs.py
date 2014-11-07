# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.template.loader import get_template

from ..settings import highlightjs_url, highlightjs_jquery_url, css_url, get_highlightjs_setting
from ..renderer import render_highlightjs


register = template.Library()


@register.simple_tag
def highlightjs_css_url():
    """
    Return the full url to the highlightjs CSS library

    Default value: ``None``

    This value is configurable, see Settings section

    **Tag name**::

        highlightjs_css_url

    **usage**::

        {% highlightjs_css_url %}

    **example**::

        {% highlightjs_css_url %}
    """
    return css_url()


@register.simple_tag
def highlightjs_javascript(jquery=None):
    """
    Return HTML for highlightjs JavaScript.

    Adjust url in settings. If no url is returned, we don't want this statement to return any HTML.
    This is intended behavior.

    Default value: ``None``

    This value is configurable, see Settings section

    **Tag name**::

        highlightjs_javascript

    **Parameters**:

        :jquery: Truthy to include jQuery as well as highlightjs

    **usage**::

        {% highlightjs_javascript %}

    **example**::

        {% highlightjs_javascript jquery=1 %}
    """

    javascript = ''
    # See if we have to include jQuery
    if jquery is None:
        jquery = get_highlightjs_setting('include_jquery', False)
    if jquery:
        url = highlightjs_jquery_url()
        if url:
            javascript += '<script src="{url}"></script>'.format(url=url)
    url = highlightjs_url()
    if url:
        javascript += '<script src="{url}"></script>'.format(url=url)
    javascript += '<script>hljs.initHighlightingOnLoad();</script>'
    return javascript


@register.simple_tag
def highlightjs_this(*args, **kwargs):
    """
    Render a form
    **Tag name**::
        highlightjs_this
    **Parameters**:
        :context_var:
        :language: optionnal
    **usage**::
        {% highlightjs_this context_var %}
    **example**::
        {% highlightjs_this python_code %}
        {% highlightjs_this python_code 'python' %}
        {% highlightjs_this html_code 'html' %}
    """
    return render_highlightjs(*args, **kwargs)
