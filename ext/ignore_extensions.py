import ark.filters

ignore_extensions = [".graffle", ".dot", ".svg"]

@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def ignore_src_file(some_bool_value, node):
    for ending in ignore_extensions:
        if str(node).endswith(ending):
            return False
    return some_bool_value
