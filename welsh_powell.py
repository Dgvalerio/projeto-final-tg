def welsh_powell(g):
    for node in g._node:
        if not g._node[node]['status']:
            for e in g.neighbors(node):
                if g._node[e]['status']:
                    try:
                        g._node[node]['color'].remove(g._node[e]['color'])
                    except:
                        pass