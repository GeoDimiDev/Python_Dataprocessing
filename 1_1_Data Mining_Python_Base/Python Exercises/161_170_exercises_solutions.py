# -*- coding: utf-8 -*-
"""161-170_exercises_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lttJQ4z65lxadBf_Jwg1fwnstLgh90qN

## Pandas

### Table of contents:
* [Import biblioteki](#0)
* [Exercise 161](#1)
* [Exercise 162](#2)
* [Exercise 163](#3)
* [Exercise 164](#4)
* [Exercise 165](#5)
* [Exercise 166](#6)
* [Exercise 167](#7)
* [Exercise 168](#8)
* [Exercise 169](#9)
* [Exercise 170](#10)

### <a name='0'></a> Import of libraries
"""

import numpy as np
import pandas as pd

pd.options.display.float_format = '{:.2f}'.format
np.__version__

"""### <a name='1'></a> Exercise 161
Load the csv file into the _DataFrame_ object named _df_:
Заредете csv файла в обекта _DataFrame_ с име _df_:

* https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv

Set the index to the first column. Display object _df_.
Задайте индекса на първата колона. Показване на обект _df_.

"""

url = 'https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv'
df = pd.read_csv(url, index_col=0)
df

"""Display information about the object _df_."""
"""Показва информация за обекта _df_."""

df.info()

"""Display basic statistics of an object _df_."""
"""Показва основна статистика на обект _df_."""

df.describe()

df.describe(include='object')

"""### <a name='2'></a> Exercise 162
Find the list containing the names of all columns of the _df_ object.
Намерете списъка, съдържащ имената на всички колони на обекта _df_.
"""

list(df.columns)

"""From the df object, remove the column named New_Price and display the first 5 rows."""
"""От обекта df премахнете колоната с име New_Price и покажете първите 5 реда."""

df.drop('New_Price', axis=1, inplace=True)
df.head()

"""### <a name='3'></a> Exercise 163
Find the number of missing values for each object variable _df_.
Намерете броя на липсващите стойности за всяка обектна променлива _df_.
"""

df.isnull().sum()

"""Delete all rows with missing values in the _df_ object. Use the `inplace = True` parameter."""
"""Изтрийте всички редове с липсващи стойности в _df_ обекта. Използвайте параметъра `inplace = True`."""

df.dropna(inplace=True)

"""### <a name='4'></a> Exercise 164
Replace all letters in column names with lowercase letters, e.g.
Заменете всички букви в имената на колоните с малки букви, напр.
* Name -> name
* Fuel_Type -> fuel_type

Display the first five rows using the _head()_ method.
Покажете първите пет реда с помощта на метода _head()_.
"""

df.columns = [col.lower() for col in df.columns]
df.head()

"""### <a name='5'></a> Exercise 165
Find the distribution of the _owner_type_ variable.
Намерете разпределението на променливата _owner_type_.
"""

df['owner_type'].value_counts()

"""Find the distribution of the _engine_ variable."""
"""Намерете разпределението на променливата _engine_."""

df['engine'].value_counts()

"""Note that the variable _engine_ is of type _object_. Remove the last 3 characters from each element and convert to _int_. Display the first five rows using the _head()_ method."""
"""Имайте предвид, че променливата _engine_ е от тип _object_. Премахнете последните 3 знака от всеки елемент и преобразувайте в _int_. Покажете първите пет реда с помощта на метода _head()_."""

df['engine'] = df['engine'].map(lambda x: int(x[:-3]))
df.head()

"""### <a name='6'></a> Exercise 166
Look at the distribution of the _power_ variable. Note that this variable also has missing values in the form of the _'null bhp'_ value. Replace these values for _power_ with _np.nan_. Use the _np.where()_ function for this.
Вижте разпределението на променливата _power_. Имайте предвид, че тази променлива също има липсващи стойности под формата на стойността _'null bhp'_. Заменете тези стойности за _power_ с _np.nan_. Използвайте функцията _np.where()_ за това.
"""

df['power'] = np.where(df['power'] == 'null bhp', np.nan, df['power'])

"""Delete all rows with missing values again."""
"""Изтрийте отново всички редове с липсващи стойности."""

df.dropna(inplace=True)

"""### <a name='7'></a> Exercise 167
Note that the _power_ variable is of type _object_. Remove the last 4 characters from each element and convert to float type.

Display the first five rows using the _head()_ method.

Имайте предвид, че променливата _power_ е от тип _object_. Премахнете последните 4 знака от всеки елемент и преобразувайте в плаващ тип.

Покажете първите пет реда с помощта на метода _head()_.
"""

df['power'] = df['power'].map(lambda x: float(x[:-4]))
df.head()

"""### <a name='8'></a> Exercise 168
Group data at year level (_year_) and count the number of rows for each year.
Групирайте данните на ниво година (_year_) и пребройте броя на редовете за всяка година.
"""

df.groupby('year').size()

"""### <a name='9'></a> Exercise 169
Check the distribution of the _transmission_ variable.
Проверете разпределението на променливата _transmission_.
"""

df['transmission'].value_counts()

"""Perform the following mapping of the _transmission_ variable:
* Manual -> 0
* Automatic -> 1

Display the first five rows using the _head()_ method.

Извършете следното картографиране на променливата _transmission_:
* Ръчно -> 0
* Автоматично -> 1

Покажете първите пет реда с помощта на метода _head()_.
"""

df['transmission'] = df['transmission'].map({'Manual': 0, 'Automatic': 1})
df.head()

"""### <a name='10'></a> Exercise 170
Save the _df_ object to the _car.csv_ file (do not save the index).
Запазете обекта _df_ във файла _car.csv_ (не запазвайте индекса).
"""

df.to_csv('car.csv', index=False)

"""Run the following instructions to check."""
"""Изпълнете следните инструкции, за да проверите."""

!head car.csv

