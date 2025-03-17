import ark
import orgpython

@ark.renderers.register('org')
def org_callback(text):
    html = orgpython.to_html(text, toc=False, offset=0, highlight=True)
    return html
