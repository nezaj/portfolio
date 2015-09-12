from flask import url_for
import pytest

from .util import captured_templates

VIEW_NAME = 'blog.list'
TEMPLATE_NAME = 'blog/list.tmpl'

@pytest.mark.usefixtures('client')
class TestBlogListView(object):

    def get_view(self):
        return self.client.get(url_for(VIEW_NAME))

    def test_ok(self):
        res = self.get_view()
        assert res.status_code == 200

    def test_renders_template(self):
        with captured_templates(self.app) as templates:
            self.get_view()

            assert len(templates) == 1
            template, _ = templates[0]
            assert template.name == TEMPLATE_NAME
