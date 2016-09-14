from pelican.readers import MarkdownReader
from skydark_helper import read_with_meta
from markdown import Markdown
from pelican import signals

class YAMLMarkdownReader(MarkdownReader):
    def read(self, source_path):
        self._source_path = source_path
        self._md = Markdown(extensions=self.extensions)
        metadata, content = read_with_meta(self, source_path)
        output = self._md.convert(content)
        return output, metadata

def add_reader(readers):
    for k in YAMLMarkdownReader.file_extensions:
        readers.reader_classes[k] = YAMLMarkdownReader

def register():
    signals.readers_init.connect(add_reader)

