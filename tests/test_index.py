from flask import url_for
import pytest

from .util import captured_templates

INDEX_VIEW = 'main.welcome'

@pytest.mark.usefixtures('client')
class TestIndexView(object):

    def get_view(self):
        return self.client.get(url_for(INDEX_VIEW))

    def test_ok(self):
        res = self.get_view()
        assert res.status_code == 200

    def test_daily_motto_is_displayed(self):
        """ Smoke test to make sure page content loaded """
        res = self.get_view()
        assert 'Be present' in res.text
        assert 'Be honest' in res.text
        assert 'Be consistent' in res.text

    def test_renders_package_list_template(self):
        with captured_templates(self.app) as templates:
            self.get_view()

            assert len(templates) == 1
            template, _ = templates[0]
            assert template.name == 'welcome.tmpl'
