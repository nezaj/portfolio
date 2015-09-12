"""
Custom Jinja2 template filtering functions
"""

from flask import Markup
import misaka

# pylint can't recognize misaka.html
# pylint: disable=E1101
def markdownize(content):
    " Converts Markdown content into html "
    return Markup(misaka.html(content))
