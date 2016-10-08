import os
from markdown import Markdown
from role_emoji import EmojiRule
from mdx_rst import SimpleDirective, SimpleRule, etree
import pelicanconf


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
    marked = False

    def template(self, markdown, name, argument, arguments, options, content, **kwargs):
        e = etree.Element('section')
        h = etree.SubElement(e, 'header', CLASS('js-toggle-next dropdown'))
        h.append(self.markdownize(markdown, argument)[0])
        self.parseAttr(markdown, h, options.get('header', ''))
        a = etree.SubElement(e, 'article', CLASS(''))
        self.parseAttr(markdown, a, options.get('body', ''))
        a.append(self.markdownize(markdown, content))
        return e


class IncludeDirective(SimpleDirective):
    has_content = False
    marked = False
    DIRECTIVE_INCLUDE_DIR = 'include'

    def template(self, markdown, name, argument, arguments, options, content, **kwargs):
        inpath = os.path.join(
                pelicanconf.PATH,
                self.DIRECTIVE_INCLUDE_DIR,
                argument)
        with open(inpath) as infile:
            included = infile.read()
            e = etree.Element('section')
            if options.get('raw', '').lower() not in ('true', '1'):
                included = self.markdownize(markdown, included)
            e.append(included)
            return e


class SlideDirective(SimpleDirective):
    slide_id = 1
    marked = False

    def template(self, markdown, name, argument, arguments, options, content, marked, **kwargs):
        div = etree.Element('div', CLASS("carousel slide"))
        div.attrib['data-ride'] = 'carousel'
        slide_id = div.attrib['id'] = 'carousel-slide-%s' % SlideDirective.slide_id
        SlideDirective.slide_id += 1
        marked = self.markdownize(markdown, content)
        if len(marked) != 1 or marked[0].tag != 'ul':
            raise Exception("Slide directive requires unordered list!")
        marked = marked[0]
        count = len(marked)
        indicators = etree.SubElement(div, 'ol', CLASS('carousel-indicators'))
        for i in range(count):
            indicator = etree.SubElement(indicators, 'li', {
                'data-target':'#%s' % slide_id,
                'data-slide-to': str(i),
                })
            if i == 0:
                indicator.attrib['class'] = 'active'
        inner = etree.SubElement(div, 'div', {
                    'class': 'carousel-inner',
                    'role':'listbox',
                })
        for i, item in enumerate(marked):
            c = 'item' if i > 0 else 'item active'
            item.tag = 'div'
            item.attrib['class'] = c
            inner.append(item)
        control_prev = etree.SubElement(div, 'a', {
            'class': "left carousel-control",
            'href': '#%s' % slide_id,
            'role': "button",
            'data-slide':"prev",
            })
        control_prev.text = '&lsaquo;'
        control_next = etree.SubElement(div, 'a', {
            'class': "right carousel-control",
            'href': '#%s' % slide_id,
            'role': "button",
            'data-slide':"next",
            })
        control_next.text = '&rsaquo;'
        script = etree.SubElement(div, 'script', {
            'type': 'text/javascript',
            })
        script.text = '$("#%s").carousel();' % slide_id
        return div

class TooltipRule(object):
    def __call__(self, role, content):
        r = content.split(':', 1)
        if len(r) != 2:
            raise Exception("Tooltips should be splitted by colon")
        e = etree.Element('a')
        e.attrib['rel'] = 'tooltip'
        e.text = r[0]
        e.attrib['title'] = r[1]
        return e

MD_EXTENSIONS = [
        'codehilite(css_class=highlight)', 'extra', 'toc',
        'meta', 'meta_yaml',
        'rst']

MD_EXTENSION_CONFIGS = {
    'rst':{
        'roles':{
            'tooltip': TooltipRule(),
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
            'include': IncludeDirective(),
            'slide': SlideDirective(),
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

