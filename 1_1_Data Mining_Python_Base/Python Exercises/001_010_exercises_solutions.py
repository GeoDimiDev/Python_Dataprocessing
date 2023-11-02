# -*- coding: utf-8 -*-
"""001-010_exercises_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13qJjnrAV2d71Clly9JwsBPyxi_Q80HUg

## Numpy

### Table of contents:
* [Import biblioteki](#0)
* [Exercise 1](#1)
* [Exercise 2](#2)
* [Exercise 3](#3)
* [Exercise 4](#4)
* [Exercise 5](#5)
* [Exercise 6](#6)
* [Exercise 7](#7)
* [Exercise 8](#8)
* [Exercise 9](#9)
* [Exercise 10](#10)

### <a name='0'></a> Import of libraries
"""

import numpy as np

np.__version__

"""### <a name='1'></a> Exercise 1
Check if all array elements $ A, B, C $ and $ D $ return the logical value _True_.
Проверете дали всички елементи на масива $ A, B, C $ и $ D $ връщат логическата стойност _True_.
```
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])
```

__Tip:__ Use the function _np.all()_.
__Съвет:__ Използвайте функцията _np.all()_.
"""

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.all(array)}')

"""### <a name='2'></a> Exercise 2
Check if all array elements $ A, B $ and $ C $ return the logical value _True_ along the axis with index 1.
Проверете дали всички елементи на масива $ A, B $ и $ C $ връщат логическата стойност _True_ по оста с индекс 1.
```
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])
```

__Tip:__ Use the function _np.all()_ with the parameter _axis_.
__Съвет:__ Използвайте функцията _np.all()_ с параметъра _axis_.
"""

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

for name, array in zip(list('ABC'), [A, B, C]):
    print(f'{name}: {np.all(array, axis=1)}')

"""### <a name='3'></a> Exercise 3
Check if any element of arrays $ A, B, C $ and $ D $ returns the logical value _True_.
Проверете дали някой елемент от масиви $ A, B, C $ и $ D $ връща логическата стойност _True_.
```
A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])
```

__Tip:__ Use the _np.any()_ function.
__Съвет:__ Използвайте функцията _np.any()_.
"""

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')

"""### <a name='4'></a> Exercise 4
Check if any element of arrays $ A, B, C $ and $ D $ returns the logical value _True_ along the axis with index 0.
Проверете дали някой елемент от масиви $ A, B, C $ и $ D $ връща логическата стойност _True_ по оста с индекс 0.
```
A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])
```

__Tip:__ Use the _np.any()_ function with the parameter _axis_.
__Съвет:__ Използвайте функцията _np.any()_ с параметъра _axis_.
"""

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array, axis=0)}')

"""### <a name='5'></a> Exercise 5
Check the array $ A $ for missing data (_np.nan_).
Проверете масива $ A $ за липсващи данни (_np.nan_).
```
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])
```
__Tip:__ Use the _np.isnan()_ function.

"""

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

np.isnan(A)

"""### <a name='6'></a> Exercise 6
Check if the following arrays $ A $ and $ B $ are equal in terms of elements (element-wise) with the specified tolerance level. Use the _np.allclose()_ function with default parameters.
Проверете дали следните масиви $ A $ и $ B $ са равни по отношение на елементи (по елементи) с указаното ниво на толеранс. Използвайте функцията _np.allclose()_ с параметри по подразбиране.
```
A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])
```
"""

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

np.allclose(A, B)

"""### <a name='7'></a> Exercise 7
Check if the following arrays $ A $ and $ B $ are equal in terms of elements (element-wise). Use the comparison operator _==_.
Проверете дали следните масиви $ A $ и $ B $ са равни по отношение на елементи (по елементи). Използвайте оператора за сравнение _==_.
```
A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])
```
"""

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

# Solution 1
A == B

# Solution 2
np.equal(A, B)

"""### <a name='8'></a> Exercise 8

Check which elements (element-wise) from the array $ A $ below have higher values than the array $ B $.
Проверете кои елементи (по елементи) от масива $ A $ по-долу имат по-високи стойности от масива $ B $.
```
A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])
```
"""

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

# Solution 1
A > B

# Solution 2
np.greater(A, B)

"""### <a name='9'></a> Exercise 9

Create an array of numpy dimensions _4x4_ filled with zeros. Set the data type to _int_.
Създайте масив от numpy размери _4x4_, запълнени с нули. Задайте типа данни на _int_.

__Expected result:__

```
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])
```
__Tip:__ Use the _np.zeros()_ function.
__Съвет:__ Използвайте функцията _np.zeros()_.
"""

np.zeros(shape=(4, 4), dtype='int')

"""### <a name='10'></a> Exercise 10
Create an array of numpy dimensions _10x10_ filled with number 255. Set the data type to _float_.
Създайте масив от numpy размери _10x10_, попълнен с число 255. Задайте типа данни на _float_.

__Expected result:__
```
array([[255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.]])
```

__Tip:__ Use the _np.ones()_ or _np.full()_ functions.
__Съвет:__ Използвайте функциите _np.ones()_ или _np.full()_.
"""

# Solution 1
np.ones(shape=(10, 10), dtype='float') * 255

# Solution 2
np.full(shape=(10, 10), fill_value=255, dtype='float')
