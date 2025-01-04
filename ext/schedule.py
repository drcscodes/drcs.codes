import ark
import shortcodes

@shortcodes.register('schedule')
def handler(pargs, kwargs, node):
    path = ark.site.inc(pargs[0])
    with open(path) as file:
        return file.read()
