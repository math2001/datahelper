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

def numbers(string, func=int):
    if '.' in string:
        func = float
    if string[0] == '.':
        string = list(string)
        string[0:1] = ['0', '.']
        string = ''.join(string)
    return map(func, string.replace(' .', ' 0.').split(' '))
