from pelican.utils import pelican_open
import yaml

def read_with_meta(self, filename):
    with pelican_open(filename) as fp:
        text = list(fp.splitlines())

    metadata = {}
    content = ''
    if text[0].rstrip() == '---':
        i = 1
        while len(text) > i:
            if text[i].rstrip() in ('---', '...'):
                break
            i += 1
        metadata_yaml, content = '\n'.join(text[1:i]), '\n'.join(text[i+1:])
        for name, value in yaml.load(metadata_yaml).items():
            metadata[name] = self.process_metadata(name, value)
    else:
        for i, line in enumerate(text):
            kv = line.split(':', 1)
            if len(kv) == 2:
                name, value = kv[0].lower(), kv[1].strip()
                if value.startswith('"') and value.endswith('"'):
                    value = value[0:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[0:-1]
                metadata[name] = self.process_metadata(name, value)
            else:
                content = "\n".join(text[i:])
                break

    return metadata, content


