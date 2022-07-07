from welsh_powell import welsh_powell
from lists import nodes


def update(g):
    for node in g._node:
        if not g._node[node]['status'] and len(g._node[node]['color']) == 1:
            g._node[node]['status'] = True
            g._node[node]['color'] = g._node[node]['color'][0]


def clear(g):
    for node in g._node:
        if g._node[node]['status'] and type(g._node[node]['color']) != int:
            g._node[node]['status'] = False


def engage(g):
    for i in range(9):
        for j in range(9):
            if not g._node[nodes[i][j]]['status']:
                g._node[nodes[i][j]]['status'] = True
                welsh_powell(g)
                update(g)
    clear(g)
