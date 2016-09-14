import subprocess
from pelican import signals
from pelican.readers import BaseReader, METADATA_PROCESSORS
from skydark_helper import read_with_meta
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code.rstrip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

def get_markdown_engine():
    renderer = HighlightRenderer(escape=False, parse_block_html=True, parse_inline_html=True)
    return mistune.Markdown(renderer=renderer)

class MistuneReader(BaseReader):
    enabled = True
    file_extensions = ('mst', )
    markdown = get_markdown_engine()

    def read(self, filename):
        metadata, content = read_with_meta(self, filename)
        output = self.markdown(content)
        return output, metadata

def add_reader(readers):
    for ext in MistuneReader.file_extensions:
        readers.reader_classes[ext] = MistuneReader

def register():
    signals.readers_init.connect(add_reader)

