from markdown import Markdown
from role_emoji import EmojiRule
from mdx_rst import SimpleDirective, SimpleRule, etree


class MarkdownFilter(object):
    def __init__(self, markdown):
        self.markdown = markdown

    def __call__(self, content, *args):
        return self.markdown.convert(content)


def get_jinja_filters():
    markdown = Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_EXTENSION_CONFIGS)
    return {
        'md': MarkdownFilter(markdown),
    }

def CLASS(v):
    return {'class': v}

class ToggleDirective(SimpleDirective):
    def __init__(self, *kargs, **kwargs):
        super(ToggleDirective, self).__init__(*kargs, **kwargs)
        self.template = self.run
        self.marked = False

    def run(self, markdown, name, argument, arguments, options, content, **kwargs):
        e = etree.Element('section')
        h = etree.SubElement(e, 'header', CLASS('js-toggle-next dropdown'))
        h.append(self.markdownize(markdown, argument)[0])
        self.parseAttr(markdown, h, options.get('header', ''))
        a = etree.SubElement(e, 'article', CLASS(''))
        self.parseAttr(markdown, a, options.get('body', ''))
        a.append(self.markdownize(markdown, content))
        return e


MD_EXTENSIONS = [
        'codehilite(css_class=highlight)', 'extra', 'toc',
        'meta', 'meta_yaml',
        'rst']

MD_EXTENSION_CONFIGS = {
    'rst':{
        'roles':{
            'kbd': SimpleRule('kbd', raw=True, _class='') ,
            'label': SimpleRule(attrib={'class':'label'}),
            'label-default': SimpleRule(attrib={'class':'label'}),
            'label-primary': SimpleRule(attrib={'class':'label'}),
            'label-success': SimpleRule(attrib={'class':'label'}),
            'label-info': SimpleRule(attrib={'class':'label'}),
            'label-warning': SimpleRule(attrib={'class':'label'}),
            'label-danger': SimpleRule(attrib={'class':'label'}),
            'badge': SimpleRule(),
            'emoji': EmojiRule(),
        },
        'directives': {
            'toggle': ToggleDirective(),
            'danger': SimpleDirective('''
                <div class="alert alert-danger"><header>{argument}</header><div>{marked}</div></div>
            ''', has_content=False),
            'warning': SimpleDirective('''
                <div class="alert alert-warning"><header>{argument}</header><div>{marked}</div></div>
            ''', has_content=False),
            'info': SimpleDirective('''
                <div class="alert alert-info"><header>{argument}</header><div>{marked}</div></div>
            ''', has_content=False),
            'note': SimpleDirective('''
                <section class="note">
                    <header>{argument}</header>
                    <article>{marked}</article>
                </section>
            '''),
            'image': SimpleDirective('''
                <img src="{argument}" alt="{content}" width="{options[width]}"/>
            '''),
        },
    },
}

