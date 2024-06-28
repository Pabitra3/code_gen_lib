
def camel_to_snake(string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in string]).lstrip('_')

def snake_to_camel(string):
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

