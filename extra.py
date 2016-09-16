from markdown import Markdown


class MarkdownFilter(object):
    def __init__(self, markdown):
        self.markdown = markdown

    def __call__(self, content, *args):
        return self.markdown.convert(content)


def get_jinja_filters(MD_EXTENSIONS):
    markdown = Markdown(extensions=MD_EXTENSIONS)
    return {
        'md': MarkdownFilter(markdown),
    }
