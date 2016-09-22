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
    def __call__(self, markdown, elm, parent, name, arguments, options, content):
        e = etree.Element('section')
        h = etree.SubElement(e, 'header', CLASS('js-toggle-next dropdown'))
        h.text = arguments[0]
        a = etree.SubElement(e, 'article', {})
        a.append(self.markdownize(markdown, content))
        self.replace_element(elm, e)
        h.attrib['class'] += ' ' + elm.attrib.get('class', '')
        elm.attrib['class'] = ''


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

