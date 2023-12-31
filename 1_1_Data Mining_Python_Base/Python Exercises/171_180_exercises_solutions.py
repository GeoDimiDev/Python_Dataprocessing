# -*- coding: utf-8 -*-
"""171-180_exercises_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ToOFIZd51On5alS9I51ad3Y8AgVHnZnD

## Numpy

### Table of contents:
* [Import biblioteki](#0)
* [Exercise 171](#1)
* [Exercise 172](#2)
* [Exercise 173](#3)
* [Exercise 174](#4)
* [Exercise 175](#5)
* [Exercise 176](#6)
* [Exercise 177](#7)
* [Exercise 178](#8)
* [Exercise 179](#9)
* [Exercise 180](#10)

### <a name='0'></a> Import of libraries
"""

import numpy as np
import pandas as pd
import plotly.express as px

np.__version__

"""Run the following code to download the _london_bike.csv_ file to your working directory."""
"""Изпълнете следния код, за да изтеглите файла _london_bike.csv_ във вашата работна директория."""

!wget -q https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv

"""### <a name='1'></a> Exercise 171
Load the _london_bike.csv_ file into the DataFrame object named _df_ and display basic information about the object.
Заредете файла _london_bike.csv_ в обекта DataFrame с име _df_ и покажете основна информация за обекта.
"""

df = pd.read_csv('london_bike.csv')
df.info()

"""Display the first five rows of _df_."""
"""Показване на първите пет реда от _df_."""

df.head()

"""Display the last five rows of _df_."""
"""Показване на последните пет реда от _df_."""

df.tail()

"""### <a name='2'></a> Exercise 172
Note that the _timestamp_ column is of type _object_. Replace it with _datetime_.
Имайте предвид, че колоната __timestamp__ е от тип обект. Заменете го с дата и час.

__Tip:__ Use the _pd.to_datetime()_ function.
"""

df['timestamp'] = pd.to_datetime(df['timestamp'])
df.info()

"""Add a new column named _hour_ to the _df_ object and assign the time from the _timestamp_ column. Display the first five rows of the _df_ object."""
"""Добавете нова колона с име _hour_ към _df_ обекта и задайте часа от колоната _timestamp_. Покажете първите пет реда на _df_ обекта."""

df['hour'] = df['timestamp'].dt.hour
df.head()

"""### <a name='3'></a> Exercise 173
Add a new column named _month_ to the _df_ object and assign the month from the _timestamp_ column. Display the first five rows of the _df_ object.
Добавете нова колона с име _month_ към обекта _df_ и задайте месеца от колоната _timestamp_. Покажете първите пет реда на обекта _df_.
"""

df['month'] = df['timestamp'].dt.month
df.head()

"""Group data by month (_month_) and calculate the average value for the variable _hum_. Assign the result to _humidity_by_month_ and reset the index."""
"""Групирайте данните по месец (_month_) и изчислете средната стойност за променливата _hum_. Присвоете резултата на _humidity_by_month_ и нулирайте индекса."""

humidity_by_month = df.groupby('month')['hum'].mean().reset_index()
humidity_by_month

"""Using the _plotly express_ library, build a line chart of the average value of the _hum_ variable for a given month (use the _humidity_by_month_ object).
Използвайки библиотеката _plotly express_, изградете линейна диаграма на средната стойност на променливата _hum_ за даден месец (използвайте обекта _humidity_by_month_).

__Tip:__ Use the _px.line()_ function.
"""

px.line(humidity_by_month, x='month', y='hum')

"""Build the same chart this time using the _plotly_dark_ template."""
"""Изградете същата диаграма този път, като използвате шаблона _plotly_dark_."""

px.line(humidity_by_month, x='month', y='hum', template='plotly_dark')

"""Read for which month the average value of the _hum_ variable is the smallest and for which it is the largest.
Прочетете за кой месец средната стойност на променливата _hum_ е най-малка и за кой е най-голяма.

### <a name='4'></a> Exercise 174
Group data at the hour level (_hour_) and then determine the average value of the variable _cnt_. Assign the result to the variable _cnt_by_hour_ and reset the index.
Групирайте данните на ниво час (_hour_) и след това определете средната стойност на променливата _cnt_. Присвоете резултата на променливата _cnt_by_hour_ и нулирайте индекса.
"""

cnt_by_hour = df.groupby('hour')['cnt'].mean().reset_index()
cnt_by_hour

"""Using the _plotly express_ library, build a line chart of the average value of the _cnt_ variable by hours (use the _cnt_by_hour_ object)."""
"""Използвайки библиотеката _plotly express_, изградете линейна диаграма на средната стойност на променливата _cnt_ по часове (използвайте обекта _cnt_by_hour_)."""

px.line(cnt_by_hour, x='hour', y='cnt')

"""### <a name='5'></a> Exercise 175
Group data by variables _is_weekend_ and _hour_ and determine the average value of the variable _cnt_. Assign the result to the variable _cnt_by_weekend_hour_ and reset the index.
Групирайте данните по променливи _is_weekend_ и _hour_ и определете средната стойност на променливата _cnt_. Присвоете резултата на променливата _cnt_by_weekend_hour_ и нулирайте индекса.
"""

cnt_by_weekend_hour = df.groupby(['is_weekend', 'hour'])['cnt'].mean().reset_index()
cnt_by_weekend_hour

"""Using the _plotly express_ library, build a line chart of the average value of the _cnt_ variable by hours __on non-weekend days__ (use the _cnt_by_weekend_hour_ object). Set the title of the chart: 'Out of the weekend'."""
"""Използвайки библиотеката _plotly express_, изградете линейна диаграма на средната стойност на променливата _cnt_ по часове __в дни без уикенд__ (използвайте обекта _cnt_by_weekend_hour_). Задайте заглавието на диаграмата: "Извън уикенда"." ""

px.line(cnt_by_weekend_hour.query("is_weekend == 0.0"), x='hour', y='cnt', title='Out of the weekend')

"""Using the _plotly express_ library, build a line chart of the average value of _cnt_ by hour __on weekend days__ (use the _cnt_by_weekend_hour_ object). Set the chart title: 'Weekends'."""
"""Използвайки библиотеката _plotly express_, изградете линейна диаграма на средната стойност на _cnt_ по час __в дните от почивните дни__ (използвайте обекта _cnt_by_weekend_hour_). Задайте заглавието на диаграмата: 'Уикенди'."""

px.line(cnt_by_weekend_hour.query("is_weekend == 1.0"), x='hour', y='cnt', title='Weekends')

"""Are there any differences between non-weekend days and weekend days?
Има ли разлики между дните без уикенд и дните през почивните дни?

### <a name='6'></a> Exercise 176
Using the _plotly express_ library, build the histogram of the _cnt_ variable. Add chart title: 'Histogram of the cnt variable'.
Използвайки библиотеката _plotly express_, изградете хистограмата на променливата _cnt_. Добавете заглавие на диаграмата: „Хистограма на променливата cnt“.
"""

px.histogram(df, x='cnt', title='Histogram of the cnt variable')

"""Also add a box chart to the histogram.
Също така добавете кутия диаграма към хистограмата.

__Tip:__ Use parameter _marginal_ of function _px.histogram()_.
"""

px.histogram(df, x='cnt', title='Histogram of the cnt variable', marginal='box')

"""### <a name='7'></a> Exercise 177
Extract rows for which the _wind_speed_ variable is less than 10.0 and the _hum_ variable is greater than 90.0.
Извлечете редове, за които променливата _wind_speed_ е по-малка от 10,0, а променливата _hum_ е по-голяма от 90,0.
"""

df.query("wind_speed < 10.0 and hum > 90.0")

"""### <a name='8'></a> Exercise 178
Extract rows for which the _is_weekend_ variable is 1.0. Then copy the result and assign it to the _df_weekend_ variable.
Извлечете редове, за които променливата _is_weekend_ е 1.0. След това копирайте резултата и го присвоете на променливата _df_weekend_.
"""

df_weekend = df.query("is_weekend == 1.0").copy()
df_weekend

"""### <a name='9'></a> Exercise 179
Save the _df_weekend_ object to the _weekend.xlsx_ file. Name the worksheet _london_bike_ and skip saving the index to a file.
Запишете обекта _df_weekend_ във файла _weekend.xlsx_. Назовете работния лист _london_bike_ и пропуснете запазването на индекса във файл.
"""

df_weekend.to_excel('weekend.xlsx', sheet_name='london_bike', index=False)

"""### <a name='10'></a> Exercise 180
Save the first 10 rows of the _df_weekend_ object to the _head10.html_ file.
Запишете първите 10 реда на обекта _df_weekend_ във файла _head10.html_.
"""

df_weekend.head(10).to_html('head10.html')