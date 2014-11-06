
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings


HIGHLIGHTJS_DEFAULTS = {
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'base_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/highlight.min.js',
    'css_url': '//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.3/styles/{}.min.css',
    'include_jquery': False,
    'style': 'monokai_sublime',
}

# Start with a copy of default settings
HIGHLIGHTJS = HIGHLIGHTJS_DEFAULTS.copy()

# Override with user settings from settings.py
HIGHLIGHTJS.update(getattr(settings, 'HIGHLIGHTJS', {}))


def get_highlightjs_setting(setting, default=None):
    """
    Read a setting
    """
    return HIGHLIGHTJS.get(setting, default)


def highlightjs_url():
    """
    Prefix a relative url with the bootstrap base url
    """
    return get_highlightjs_setting('base_url')


def highlightjs_jquery_url():
    """
    Return the full url to jQuery file to use
    """
    return get_highlightjs_setting('jquery_url')


def css_url():
    """
    Return the full url to the highlightjs CSS file
    """
    return get_highlightjs_setting('css_url').format(get_highlightjs_setting('style'))