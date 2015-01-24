from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    """
    Used for figuring which templates and what context was used to
    render a request

    Thanks: http://flask.pocoo.org/docs/0.10/signals/
    """
    # Pylint comaplins about sender and extra, these are used by signals
    # pylint: disable=unused-argument
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
