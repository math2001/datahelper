# datahelper

A simple python package that provide a single class to save you a fair bit of time (at least it's
the case for me :smiley:)

Here's how it works:

```python
from datahelper import Data

data = Data(1, 3, 4, 6, 3, 6, 8, 3)

print(data.average) # 4.25
print(data.median) # 5.0
print(data.range) # 7
print(data.frequency_table)
# |  x   |  f   |  fx  | Cumu. f |
# |------|------|------|---------|
# |    1 |    1 |    1 |       1 |
# |    3 |    3 |    9 |       4 |
# |    4 |    1 |    4 |       5 |
# |    6 |    2 |   12 |       7 |
# |    8 |    1 |    8 |       8 |
```
