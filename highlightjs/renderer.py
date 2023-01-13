from django.forms.utils import flatatt
from django.utils.encoding import force_str
from django.utils.html import escape
from django.utils.safestring import mark_safe


def text_value(value):
    """
    Force a value to text, render None as an empty string
    """
    if value is None:
        return ""
    return force_str(value)


def render_tag(attrs=None, content=None):
    """
    Render a HTML tag
    """
    builder = "<pre><code{attrs}>{content}</code></pre>"
    return builder.format(
        attrs=flatatt(attrs) if attrs else "",
        content=escape(text_value(content)),
    )


def render_highlightjs(context_var, language=None):
    attrs = {"class": language} if language else None
    return mark_safe(render_tag(attrs=attrs, content=context_var))
