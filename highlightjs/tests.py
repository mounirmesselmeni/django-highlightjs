from __future__ import unicode_literals

from django.test import TestCase
from django.utils.html import escape
from django.template import Template, Context
from django.test.utils import override_settings

from . import settings


class HighlightjsTemplateTagTests(TestCase):

    def test_highlightjs_css_url_tag(self):
        out = Template(
            "{% load highlightjs %}"
            "{% highlightjs_css_url %}"
        ).render(Context())
        self.assertEqual(out, settings.css_url())

    def test_highlightjs_javascript_tag(self):
        out = Template(
            "{% load highlightjs %}"
            "{% highlightjs_javascript %}"
        ).render(Context())
        self.assertIn(settings.highlightjs_url(), out)

    @override_settings(HIGHLIGHTJS={'include_jquery': False})
    def test_highlightjs_javascript_tag_without_jquery(self):
        settings.update_settings()
        out = Template(
            "{% load highlightjs %}"
            "{% highlightjs_javascript %}"
        ).render(Context())
        self.assertNotIn(settings.highlightjs_jquery_url(), out)

    @override_settings(HIGHLIGHTJS={'include_jquery': True})
    def test_highlightjs_javascript_tag_with_jquery(self):
        settings.update_settings()
        out = Template(
            "{% load highlightjs %}"
            "{% highlightjs_javascript %}"
        ).render(Context())
        self.assertIn(settings.highlightjs_jquery_url(), out)

    def test_highlightjs_this_tag(self):
        code = "friends = ['john', 'pat', 'gary', 'michael']" \
               + "for i, name in enumerate(friends):" \
               + "    print 'iteration {iteration} is {name}'.format(iteration=i, name=name)"
        out = Template(
            "{% load highlightjs %}"
            "{% highlightjs_this code %}"
        ).render(Context({'code': code}))
        self.assertIn(escape(code), out)
        self.assertIn('<pre>', out)
