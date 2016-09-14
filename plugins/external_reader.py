import subprocess
from pelican import signals
from pelican.readers import BaseReader
from skydark_helper import read_with_meta

class ExternalReader(BaseReader):
    enabled = False
    exec_cmd = ''

    def make_extension_arg(self, extensions):
        return []

    def read(self, filename):
        extra_args_name = self.exec_cmd.capitalize() + '_ARGS'
        extension_name = self.exec_cmd.capitalize() + '_EXTENSIONS'

        metadata, content = read_with_meta(self, filename)

        extra_args = self.settings.get(extra_args_name, [])
        extensions = self.settings.get(extension_name, '')
        if isinstance(extensions, list):
            extensions = ''.join(extensions)

        exec_cmd = [self.exec_cmd]
        exec_cmd.extend(self.make_extension_arg(extensions))
        exec_cmd.extend(extra_args)

        proc = subprocess.Popen(exec_cmd,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE)

        output = proc.communicate(content.encode('utf-8'))[0].decode('utf-8')
        status = proc.wait()
        if status:
            raise subprocess.CalledProcessError(status, exec_cmd)

        return output, metadata

class KramdownReader(ExternalReader):
    enabled = True
    file_extensions = ('kd', )
    exec_cmd = 'kramdown'

class PandocReader(ExternalReader):
    enabled = True
    file_extensions = ('pdc', )
    exec_cmd = 'pandoc'

    def make_extension_arg(self, extensions):
        return ['--from=markdown' + extensions, '--to=html5']

def add_reader(readers):
    for ext in KramdownReader.file_extensions:
        readers.reader_classes[ext] = KramdownReader
    for ext in PandocReader.file_extensions:
        readers.reader_classes[ext] = PandocReader

def register():
    signals.readers_init.connect(add_reader)

