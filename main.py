import networkx as nx

nodes = [['00', '01', '02', '03', '04', '05', '06', '07', '08'],
         ['10', '11', '12', '13', '14', '15', '16', '17', '18'],
         ['20', '21', '22', '23', '24', '25', '26', '27', '28'],
         ['30', '31', '32', '33', '34', '35', '36', '37', '38'],
         ['40', '41', '42', '43', '44', '45', '46', '47', '48'],
         ['50', '51', '52', '53', '54', '55', '56', '57', '58'],
         ['60', '61', '62', '63', '64', '65', '66', '67', '68'],
         ['70', '71', '72', '73', '74', '75', '76', '77', '78'],
         ['80', '81', '82', '83', '84', '85', '86', '87', '88']]
square = [['00', '01', '02', '10', '11', '12', '20', '21', '22'],
          ['03', '04', '05', '13', '14', '15', '23', '24', '25'],
          ['06', '07', '08', '16', '17', '18', '26', '27', '28'],
          ['30', '31', '32', '40', '41', '42', '50', '51', '52'],
          ['33', '34', '35', '43', '44', '45', '53', '54', '55'],
          ['36', '37', '38', '46', '47', '48', '56', '57', '58'],
          ['60', '61', '62', '70', '71', '72', '80', '81', '82'],
          ['63', '64', '65', '73', '74', '75', '83', '84', '85'],
          ['66', '67', '68', '76', '77', '78', '86', '87', '88']]


def welsh_powell(g):
    for node in g._node:
        if not g._node[node]['status']:
            for e in g.neighbors(node):
                if g._node[e]['status']:
                    try:
                        g._node[node]['color'].remove(g._node[e]['color'])
                    except:
                        pass


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


def sudoku_adapter(filename):
    # open and read file
    fp = open(filename, 'r')
    data = fp.read().split('\n')
    data.remove('')
    sudoku = []
    for line in data:
        sudoku.append(line.split(' '))

    return sudoku


def main(sudoku):
    # create graph
    g = nx.Graph()

    # create node with color and status
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 'x':
                g.add_node(nodes[i][j], color=[1, 2, 3, 4, 5, 6, 7, 8, 9], status=False)
            else:
                g.add_node(nodes[i][j], color=int(sudoku[i][j]), status=True)

    # create edges of rows
    for i in range(9):
        for j in range(8):
            for k in range(j, 8):
                g.add_edge(nodes[i][j], nodes[i][k + 1])

    # create edges of columns
    for i in range(8):
        for j in range(9):
            for k in range(i, 8):
                g.add_edge(nodes[i][j], nodes[k + 1][j])

    for i in range(9):
        for j in range(8):
            for k in range(j, 8):
                g.add_edge(square[i][j], square[i][k + 1])

    for i in range(9):
        engage(g)
        welsh_powell(g)
        update(g)

    for i in range(9):
        for j in range(9):
            print(g._node[nodes[i][j]]['color'], end=' ')
        print()


if __name__ == '__main__':
    game = sudoku_adapter('examples/text.txt')
    main(game)
