import ark
import mdtex2html

@ark.renderers.register('md')
def markdown_callback(text):
    html = mdtex2html.convert(text,
        extensions=['attr_list', 'fenced_code', 'codehilite', 'tables'])
    return html
