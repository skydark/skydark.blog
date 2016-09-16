"""
jinja2content.py
----------------

Pelican plugin that processes Markdown files as jinja templates.

"""

from os import path
from pelican import signals
from pelican.readers import Markdown, MarkdownReader
from pelican.utils import pelican_open
from jinja2 import Environment, FileSystemLoader, ChoiceLoader


jinja_generator = None


def pelican_initialized(pelican_obj):
    global jinja_generator
    jinja_generator = Jinja2Content(pelican_obj)


class Jinja2Content(object):
    def __init__(self, pelican_obj):
        # will look first in 'JINJA2CONTENT_TEMPLATES', by default the
        # content root path, then in the theme's templates
        # local_templates_dirs = self.settings.get('JINJA2CONTENT_TEMPLATES', ['.'])
        # local_templates_dirs = path.join(self.settings['PATH'], local_templates_dirs)
        self.pelican_obj = pelican_obj
        self.settings = {}
        try:
            self.settings.update(pelican_obj.settings['JINJA2CONTENT_SETTINGS'])
        except KeyError:
            pass
        self.settings['site'] = pelican_obj.settings
        local_dirs = pelican_obj.settings.get('JINJA2CONTENT_TEMPLATES', ['.'])
        local_dirs = [path.join(pelican_obj.settings['PATH'], folder)
                      for folder in local_dirs]
        theme_dir = path.join(pelican_obj.settings['THEME'], 'templates')

        loaders = [FileSystemLoader(_dir) for _dir
                   in local_dirs + [theme_dir]]
        self.env = Environment(trim_blocks=True, lstrip_blocks=True,
                               extensions=pelican_obj.settings['JINJA_EXTENSIONS'],
                               loader=ChoiceLoader(loaders))

        custom_filters = pelican_obj.settings['JINJA_FILTERS']
        self.env.filters.update(custom_filters)

    def render(self, content):
        settings = {}
        settings.update(self.settings)
        settings.update(content.metadata)
        content._content = self.env.from_string(content._content).render(settings)


def pelican_content_object_init(content):
    if getattr(content, 'jinja', False):
        # print("[JINJA] Jinjalizing %s" % content.title)
        jinja_generator.render(content)


def register():
    signals.initialized.connect(pelican_initialized)
    signals.content_object_init.connect(pelican_content_object_init)
