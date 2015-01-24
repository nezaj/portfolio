from flask import url_for
import pytest

from .util import captured_templates

GYM_VIEW = 'gym.dashboard'

@pytest.mark.usefixtures('client')
class TestGymView(object):

    def get_view(self):
        return self.client.get(url_for(GYM_VIEW))

    def test_ok(self):
        res = self.get_view()
        assert res.status_code == 200

    def test_renders_package_list_template(self):
        with captured_templates(self.app) as templates:
            self.get_view()

            assert len(templates) == 1
            template, _ = templates[0]
            assert template.name == 'gym.tmpl'
