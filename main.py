import networkx as nx
from welsh_powell import welsh_powell
from lists import nodes, square
from checks import engage, update
from adapter import get_random_game


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
    game = get_random_game()
    print('Quiz:')
    print(game)
    print('Resolved:')
    main(game)
