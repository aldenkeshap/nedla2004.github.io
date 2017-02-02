from browser import document

def hash(name):
    total = 0
    for char in name:
        total *= 10
        total += ord(char)
    return 10 - (total % 11)
def update():
    result = hash(document['name'].value)
    document['result'].value = 'You are a %s/10' % result

document['name'].bind('onKeyDown', update)
