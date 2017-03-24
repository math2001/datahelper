# -*- encoding: utf-8 -*-

import math
from ascii_table import ascii_table

class Data:

    def __init__(self, *numbers):
        self.numbers = list(numbers)
        self.numbers.sort()

    @property
    def median(self):
        length = len(self.numbers)
        if length % 2 == 0:
            return Data(*self.numbers[int(length / 2):int(length / 2)+2]).mean
        else:
            return self.numbers[length // 2]

    @property
    def mean(self):
        return self.average

    @property
    def average(self):
        return sum(self.numbers) / len(self.numbers)

    @property
    def standard_deviation(self):
        average = self.average
        squared_differences = []
        for number in self.numbers:
            squared_differences.append((number - average) ** 2)
        return math.sqrt(Data(*squared_differences).average)

    @property
    def range(self):
        return max(self.numbers) - min(self.numbers)

    @property
    def length(self):
        return len(self.numbers)

    def frequency_of(self, x):
        return self.numbers.count(x)

    def __str__(self):
        return '<Data [{}]>'.format(len(self.numbers))

    @property
    def frequency_table(self):
        rows = [
            ['x', 'f', 'fx', 'Cumu. f'],
        ]
        cumulative_fr = 0
        for number in sorted(set(self.numbers)):
            fr = self.frequency_of(number)
            cumulative_fr += fr
            rows.append([number, fr, number * fr, cumulative_fr])
        return ascii_table(rows, min_width=4)

#
# functions
#

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


def numbers(string, func=int):
    if '.' in string:
        func = float
    if string[0] == '.':
        string = list(string)
        string[0:1] = ['0', '.']
        string = ''.join(string)
    return map(func, string.replace(' .', ' 0.').split(' '))
