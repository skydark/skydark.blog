"""
Add rst's roles and directives to markdown

"""

import re
from collections import defaultdict
from markdown.extensions import Extension, attr_list
from markdown.inlinepatterns import Pattern
from markdown.blockprocessors import BlockProcessor
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


SIMPLENAME = r'(?:(?!_)\w)+(?:[-._+:](?:(?!_)\w)+)*'
ROLE_RE = r''':(?P<role>(%s)):`(?P<content>[^`]+)`''' % SIMPLENAME


class DirectiveBlockProcessor(BlockProcessor):
    BASE_RE = re.compile(r'''^\{\:?([^\}\n]*)\}$''')
    DIRECTIVE_RE = re.compile(
            r'''\s*\.\.[ ]+(?P<directive>%s)[ ]?::(?P<extra>.*)$''' % SIMPLENAME)

    matched = None
    attr_list_helper = None

    def test(self, parent, block):
        self.matched = self.DIRECTIVE_RE.match(block)
        return self.matched is not None

    def run(self, parent, blocks):
        block = blocks.pop(0)
        directive = etree.SubElement(parent, 'directive')
        d = self.matched.groupdict()
        directive.attrib['directive'] = d['directive']
        header = etree.SubElement(directive, 'header')
        argument = d['extra'].strip()
        k = argument.rfind('{')
        if k >= 0:
            attrs = argument[k:]
            matched = self.BASE_RE.match(attrs)
            if matched:
                argument = argument[:k]
                self.attr_list_helper.assign_attrs(directive, matched.group(1))
        header.text = argument


class DirectiveTreeProcessor(Treeprocessor):
    OPTION_RE = re.compile(r'''^:(?P<name>[^:]+):\s*(?P<value>.*)$''')

    directives = {}

    def registerRule(self, name, directive):
        self.directives[name] = directive

    def runBlock(self, block):
        children = block.getchildren()
        for child_num, child in enumerate(children):
            if child.tag != 'directive':
                continue
            if 'directive' not in child.attrib or len(child) != 1 or child[0].tag != 'header':
                raise Exception('Not a directive!')
            name = child.attrib['directive']
            if name not in self.directives:
                raise Exception("Unknown directive: %s" % name)
            directive = self.directives[name]
            text = child[0].text
            arguments = [(text if text is not None else '').strip()]
            child.remove(child[0])
            sibling = None
            codeblock = None
            text = ''
            if len(children) > child_num + 1:
                sibling = children[child_num+1]
                if sibling.tag != 'pre':
                    sibling = None
                if sibling and len(sibling) == 1 and sibling[0].tag == 'code':
                    codeblock = sibling[0]
            if directive.has_content:
                if codeblock is None:
                    raise Exception(
                        "A code block must be followed after the directive: %s"
                        % name)
                text = codeblock.text
            else:
                if codeblock:
                    text = codeblock.text
            options, content = self.parse_options(text)
            if not directive.has_content and codeblock and content:
                codeblock.text = content
                content = ''
            else:
                if sibling:
                    block.remove(sibling)
            directive(self.markdown, child, block, name, arguments, options, content)

    def run(self, root):
        for block in root.getiterator():
            self.runBlock(block)

    def parse_options(self, text):
        options = {}
        lines = text.splitlines()
        line_limit = len(lines)
        i = 0
        while i < line_limit:
            line = lines[i]
            matched = self.OPTION_RE.match(line.rstrip())
            if matched:
                d = matched.groupdict()
                options[d['name']] = d['value']
                i += 1
            else:
                while i < line_limit:
                    line = lines[i]
                    if line.strip() != '':
                        break
                    i += 1
                break
        content = u'\n'.join(lines[i:])
        return options, content


class RolePattern(Pattern):
    rules = {}

    def registerRule(self, role, rule):
        self.rules[role] = rule

    def handleMatch(self, m):
        d = m.groupdict()
        role, content = d['role'], d['content']
        rule = self.rules.get(role, None)
        if rule:
            return rule(role, content)
        el = etree.Element('span')
        el.attrib['class'] = role
        el.text = content
        return el


class SimpleRule(object):
    def __init__(self, tag='span', attrib=None, text='{content}', raw=False, _class='{role}', **kwargs):
        self.tag = tag
        self.attrib = attrib or {}
        self.text = text or ''
        self.raw = raw
        self.attrib.update(kwargs)
        if _class:
            if 'class' in self.attrib:
                self.attrib['class'] += ' ' + _class
            else:
                self.attrib['class'] = _class

    def __call__(self, role, content):
        el = etree.Element(self.tag)
        for k, v in self.attrib.items():
            el.attrib[k] = v.format(role=role, content=content)
        text = self.text.format(role=role, content=content)
        if self.raw:
            text = AtomicString(text)
        el.text = text
        return el


class MDDirective(object):
    has_content = True

    def __call__(self, markdown, elm, name, arguments, options, content):
        # TODO: check:
        # required_arguments, optional_arguments
        # final_argument_whitespace, option_spec, has_content
        raise NotImplementedError

    def markdownize(self, markdown, source):
        lines = source.split("\n")
        flag = hasattr(markdown, 'Meta')
        if flag:
            meta = markdown.Meta
        for prep in markdown.preprocessors.values():
            lines = prep.run(lines)
        root = markdown.parser.parseDocument(lines).getroot()
        if flag:
            markdown.Meta = meta
        return root

    def replace_element(self, elm, new_elm):
        elm.tag = new_elm.tag
        elm.text = new_elm.text
        attrib = elm.attrib
        for k, v in new_elm.attrib.items():
            if k == 'class' and k in attrib:
                    attrib[k] += ' ' + v
            else:
                attrib[k] = v
        for child in list(elm):
            elm.remove(child)
        for e in new_elm:
            elm.append(e)

    def elmToHtml(self, elm):
        return etree.tostring(elm, encoding='utf8', method='html').decode('utf8')

    def mdToHtml(self, markdown, content):
        # <div>markdown</div>
        return self.elmToHtml(self.markdownize(markdown, content))[5:-6]

    def stringToElm(self, text):
        return etree.fromstring(text)

    def parseAttr(self, markdown, elm, attr):
        attr_list_helper = attr_list.AttrListTreeprocessor(markdown)
        attr_list_helper.assign_attrs(elm, attr)


class SimpleDirective(MDDirective):
    def __init__(self, template='', has_content=True, marked=True):
        self.template = template
        self.marked = marked
        self.has_content = has_content

    def __call__(self, markdown, elm, parent, name, arguments, options, content):
        if self.marked:
            marked = self.mdToHtml(markdown, content)
        else:
            marked = content
        _options = defaultdict(lambda : '')
        _options.update(options)
        if hasattr(self.template, 'format'):
            call = self.template.format
        elif callable(self.template):
            call = self.template
        else:
            raise Exception("Template is not callable")
        output = call(
            markdown=markdown,
            name=name, argument = arguments[0] if len(arguments) > 0 else '',
            arguments=arguments, options=_options, content=content, marked=marked)
        if isinstance(output, str):
            output = self.stringToElm(output)
        self.replace_element(elm, output)


class RstExtension(Extension):
    def __init__(self, *args, **kwargs):
        # Define config options and defaults
        self.config = {
            'roles': [{}, 'Role map'],
            'directives': [{}, 'Directive map'],
        }
        # Call the parent class's __init__ method to configure options
        super(RstExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        """Add MetaYamlPreprocessor to Markdown instance."""
        role_tag = RolePattern(ROLE_RE, 'role')
        for role, rule in self.getConfig('roles').items():
            role_tag.registerRule(role, rule)
        md.inlinePatterns.add('role', role_tag, '<backtick')
        dbp = DirectiveBlockProcessor(md.parser)
        dbp.attr_list_helper = attr_list.AttrListTreeprocessor(md)
        md.parser.blockprocessors.add('directive', dbp, '<paragraph')
        dtp = DirectiveTreeProcessor(md)
        for directive, rule in self.getConfig('directives').items():
            dtp.registerRule(directive, rule)
        md.treeprocessors.add('directive', dtp, '_begin')


def makeExtension(**kwargs):
    return RstExtension(**kwargs)
