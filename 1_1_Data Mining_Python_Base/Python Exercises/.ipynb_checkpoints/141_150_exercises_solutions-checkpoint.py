# -*- coding: utf-8 -*-
"""141-150_exercises_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V_20gEFsX_nN-nDEWCd4j3b4P3SdEo5W

## Pandas

### Table of contents:
* [Import biblioteki](#0)
* [Exercise 141](#1)
* [Exercise 142](#2)
* [Exercise 143](#3)
* [Exercise 144](#4)
* [Exercise 145](#5)
* [Exercise 146](#6)
* [Exercise 147](#7)
* [Exercise 148](#8)
* [Exercise 149](#9)
* [Exercise 150](#10)

### <a name='0'></a> Import of libraries
"""

import numpy as np
import pandas as pd

np.random.seed(42)
np.__version__

"""### <a name='1'></a> Exercise 141
Two _Series_ objects are given:
Дадени са два обекта _Series_:
```
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
```
Combine these two objects into one _DataFrame_ object (as two columns) and assign to _df_. Name the columns _col1_ and _col2_ respectively.
Комбинирайте тези два обекта в един обект _DataFrame_ (като две колони) и присвоете на _df_. Именувайте колоните съответно _col1_ и _col2_.
"""

s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
df

"""### <a name='2'></a> Exercise 142
Extract rows from the _df_ object for which the value in the _col2_ column is between 0.0 and 1.0 (inclusive).
Извлечете редове от обекта _df_, за които стойността в колоната _col2_ е между 0,0 и 1,0 (включително).
"""

# Solution 1
df[df['col2'].between(0.0, 1.0)]

# Solution 2
df[(df['col2'] >= 0.0) & (df['col2'] <= 1.0)]

"""### <a name='3'></a> Exercise 143
Assign a new column named _col3_, which will have a value of 1 when the value in the column _col2_ is non-negative and -1 opposite.
Присвоете нова колона с име _col3_, която ще има стойност 1, когато стойността в колона _col2_ е неотрицателна и -1 срещуположна.

"""

df['col3'] = df['col2'].map(lambda x: 1 if x >= 0 else -1)
df

"""### <a name='4'></a> Exercise 144

Assign a new column _col4_, which will truncate the values from the column _col2_ to the range $ [- 1.0, 1.0] $.
In other words, for values below -1.0, leave -1.0, for values above 1.0, leave 1.0.

Присвоете нова колона _col4_, която ще съкрати стойностите от колона _col2_ до диапазона $ [- 1.0, 1.0] $.
С други думи, за стойности под -1,0 оставете -1,0, за стойности над 1,0 оставете 1,0.

"""

df['col4'] = df['col2'].clip(-1.0, 1.0)
df

"""### <a name='5'></a> Exercise 145
Find the top 5 values for the _col2_ column.
Намерете първите 5 стойности за колоната _col2_.
"""

df['col2'].nlargest(5)

"""Find the 5 lowest values for the _col2_ column."""
"""Намерете 5-те най-ниски стойности за колоната _col2_."""

df['col2'].nsmallest(5)

"""### <a name='6'></a> Exercise 146
Calculate the cumulative sum for each column.
Изчислете кумулативната сума за всяка колона.

__Tip:__ Use the _pd.DataFrame.cumsum()_ method.
"""

df.cumsum()

"""### <a name='7'></a> Exercise 147
Calculate the median for the _col2_ variable (or 0.5 quantile).
Изчислете медианата за променливата _col2_ (или 0,5 квантил).
"""

# Solution 1
df['col2'].median()

# Solution 2
df['col2'].quantile()

"""### <a name='8'></a> Exercise 148
Extract rows for which the variable _col2_ takes values greater than 0.0.
Извлечете редове, за които променливата _col2_ приема стойности, по-големи от 0,0.
"""

# Solution 1
df.query("col2 > 0")

# Solution 2
df[df['col2'] > 0]

"""### <a name='9'></a> Exercise 149
Extract first 5 rows of the _df_ object and convert it to a dictionary.
Извлечете първите 5 реда от обекта _df_ и го преобразувайте в речник.
"""

df.head().to_dict()

"""### <a name='10'></a> Exercise 150
Extract the first 5 rows of the _df_ object, convert it to Markdown format, and assign it to the _df_markdown_ variable.
Извлечете първите 5 реда от обекта _df_, преобразувайте го във формат Markdown и го присвоете на променливата _df_markdown_.
"""

df_markdown = df.head().to_markdown()
df_markdown

"""Print the contents of the _df_markdown_ variable to the console."""
"""Отпечатайте съдържанието на променливата _df_markdown_ в конзолата."""

print(df.head().to_markdown())

"""Copy the result of running the above cell and paste below:
"""Копирайте резултата от изпълнението на горната клетка и го поставете по-долу:

|    |     col1 |      col2 |   col3 |      col4 |
|---:|---------:|----------:|-------:|----------:|
|  0 | 0.292145 |  0.822545 |      1 |  0.822545 |
|  1 | 0.366362 | -1.22084  |     -1 | -1        |
|  2 | 0.45607  |  0.208864 |      1 |  0.208864 |
|  3 | 0.785176 | -1.95967  |     -1 | -1        |
|  4 | 0.199674 | -1.32819  |     -1 | -1        |

"""

