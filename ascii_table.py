# -*- encoding: utf-8 -*-

def mini(x, y):
    return x if x > y else y

def isdigit(x):
    try:
        int(x)
    except:
        return False
    return True

def ascii_table(rows, title=True, min_width=0):
    length = len(rows[0])
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            rows[i][j] = str(cell)
        if len(row) != length:
            raise ValueError("The rows do not have the same length")

    sizes = []
    for i in range(len(rows[0])):
        sizes.append(max(mini(len(cell), min_width) for cell in (row[i] for row in rows)))

    table_rows = []
    for i, row in enumerate(rows):
        if title and i == 1:
            table_rows.append('|' +  '|'.join('-' * (sizes[j] + 2) for j, _ in enumerate(row)) + '|')
        table_row = []
        for j, cell in enumerate(row):
            if title and i == 0:
                cell = cell.center(sizes[j])
            elif isdigit(cell):
                cell = cell.rjust(sizes[j])
            else:
                cell = cell.ljust(sizes[j])
            table_row.append(cell)
        table_rows.append('| ' + ' | '.join(table_row) + ' |')
    return '\n'.join(table_rows)

if __name__ == '__main__':
    # CSW: ignore
    print(ascii_table([
        ['Hello', 'World'],
        ['3', 9],
        ['this is a test', 'hello world!!']
    ]))
    # CSW: ignore
    print(ascii_table([
        ['test', ''],
        ['..', '']
    ], min_width=5))
