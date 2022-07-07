def sudoku_adapter(filename):
    # open and read file
    fp = open(filename, 'r')
    data = fp.read().split('\n')
    data.remove('')
    sudoku = []
    for line in data:
        sudoku.append(line.split(' '))

    return sudoku
