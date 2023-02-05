from django import template
from django.utils.html import format_html

from ..renderer import render_highlightjs
from ..settings import (
    css_url,
    get_highlightjs_setting,
    highlightjs_jquery_url,
    highlightjs_url,
)

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

    Adjust url in settings. If no url is returned, we don't
    want this statement to return any HTML.
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

    javascript = ""
    # See if we have to include jQuery
    if jquery is None:
        jquery = get_highlightjs_setting("include_jquery", False)
    if jquery:
        url = highlightjs_jquery_url()
        if url:
            javascript += f'<script src="{url}"></script>'
    url = highlightjs_url()
    if url:
        javascript += f'<script src="{url}"></script>'
    javascript += "<script>hljs.initHighlightingOnLoad();</script>"
    return format_html(javascript)


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
