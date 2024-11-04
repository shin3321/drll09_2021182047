# world 0 번: background 객체들
# world 1 번: foreground 객체들
world = [[], []]

def add_object(o, depth):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()
    pass

def render():
    for layer in world:
        for o in layer:
            o.draw()
    pass
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print(f'     CRITICAL: 존재하지 않은 객체{o}를 지우려고 합니다.')