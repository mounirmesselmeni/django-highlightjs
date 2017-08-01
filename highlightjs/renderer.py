# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.html import escape
from django.utils.safestring import mark_safe

try:
    from django.forms.widgets import flatatt
except ImportError:
    # Django >= 1.11
    from django.forms.utils import flatatt

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


def text_value(value):
    """
    Force a value to text, render None as an empty string
    """
    if value is None:
        return ''
    return force_text(value)


def render_tag(attrs=None, content=None):
    """
    Render a HTML tag
    """
    builder = '<pre><code{attrs}>{content}</code></pre>'
    return builder.format(
        attrs=flatatt(attrs) if attrs else '',
        content=escape(text_value(content)),
    )


def render_highlightjs(context_var, language=None):
    attrs = {'class': language} if language else None
    return mark_safe(render_tag(attrs=attrs, content=context_var))
