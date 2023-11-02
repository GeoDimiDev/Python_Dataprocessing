# -*- coding: utf-8 -*-
"""241-250_exercises_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wbQEkM2PMoHYggBRbfSu_Q1-lNwzqkkA

## Data Science Bootcamp

### Table of contents:
* [Import biblioteki](#0)
* [Exercise 241](#1)
* [Exercise 242](#2)
* [Exercise 243](#3)
* [Exercise 244](#4)
* [Exercise 245](#5)
* [Exercise 246](#6)
* [Exercise 247](#7)
* [Exercise 248](#8)
* [Exercise 249](#9)
* [Exercise 250](#10)

### <a name='0'></a> Import of libraries
"""

import numpy as np

np.__version__

"""Run the following command (download image from Google cloud)."""
"""Изпълнете следната команда (изтегляне на изображение от Google Cloud)."""

!wget https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/ds-bootcamp.jpg

"""### <a name='1'></a> Exercise 241
Import the _opencv_ library and the _cv2_imshow_ function to display the image using the _opencv_ library.
Импортирайте библиотеката _opencv_ и функцията _cv2_imshow_, за да покажете изображението с помощта на библиотеката _opencv_.
"""

import cv2
from google.colab.patches import cv2_imshow

cv2.__version__

"""Load the _ds-bootcamp.jpg_ image into the _numpy_ array as a grayscale image using the _opencv_ library and assign to the variable _img\_gray_. Display array."""
"""Заредете изображението _ds-bootcamp.jpg_ в масива _numpy_ като изображение в скала на сивото, като използвате библиотеката _opencv_ и го присвоете на променливата _img\_gray_. Показване на масив."""

img_gray = cv2.imread('ds-bootcamp.jpg', flags=cv2.IMREAD_GRAYSCALE)
img_gray

"""### <a name='2'></a> Exercise 242
Display array shape _img\_gray_.
Показване на формата на масива _img\_gray_.
"""

img_gray.shape

"""Display the image (array _img\_gray_) using the function _cv2\_imshow_."""
"""Показване на изображението (масив _img\_gray_) с помощта на функцията _cv2\_imshow_."""

cv2_imshow(img_gray)

"""### <a name='3'></a> Exercise 243
Import the _imutils_ library. We will use it to change the image size.
Импортирайте библиотеката _imutils_. Ще го използваме, за да променим размера на изображението.
"""

import imutils

imutils.__version__

"""Using the _resize()_ function from the _imutils_ library, set the image height (array _img\_gray_) to 300 pixels. Save changes permanently to the _img\_gray_ variable. Display the shape of the array."""
"""Използвайки функцията _resize()_ от библиотеката _imutils_, задайте височината на изображението (масив _img\_gray_) на 300 пиксела. Запазете промените за постоянно в променливата _img\_gray_. Покажете формата на масива."""

img_gray = imutils.resize(img_gray, height=300)
img_gray.shape

"""Display image _img\_gray_."""
"""Изображение на дисплея _img\_сив_."""

cv2_imshow(img_gray)

"""### <a name='4'></a> Exercise 244
Load the _ds-bootcamp.jpg_ image into the _numpy_ array as a color image using the _opencv_ library and assign it to the variable _img_. Display array.
Заредете изображението _ds-bootcamp.jpg_ в масива _numpy_ като цветно изображение с помощта на библиотеката _opencv_ и го присвоете на променливата _img_. Дисплеен масив.
"""

img = cv2.imread('ds-bootcamp.jpg')
img

"""Display array _img_ shape."""
"""Показване на масив _img_ форма."""

img.shape

"""Display the image (array _img_) with the function _cv2\_imshow_."""
"""Показване на изображението (масив _img_) с функцията _cv2\_imshow_."""

cv2_imshow(img)

"""### <a name='5'></a> Exercise 245
Use the _resize()_ function from the _imutils_ library to set the image width (array _img_) to 400 pixels. Save the changes permanently to the _img_ variable. Display the shape of the array thus obtained.
Използвайте функцията _resize()_ от библиотеката _imutils_, за да зададете ширината на изображението (масив _img_) на 400 пиксела. Запазете промените за постоянно в променливата _img_. Покажете формата на така получения масив.
"""

img = imutils.resize(img, width=400)
img.shape

"""Display image _img_."""
"""Изображение на дисплея _img_."""

cv2_imshow(img)

"""### <a name='6'></a> Exercise 246
Using proper cutting of the _img_ array, cut (approximately) the python logo from the image. Display result.
Използвайки правилно изрязване на масива _img_, изрежете (приблизително) логото на Python от изображението. Показване на резултат.
"""

cv2_imshow(img[30:190, 120:280])

"""### <a name='7'></a> Exercise 247
Using the _cv2.copyMakeBorder()_ function from the _opencv_ library, add a 50-pixel-wide _img_ border to each side. Use the _cv2.BORDER_REPLICATE_ border type.
Използвайки функцията _cv2.copyMakeBorder()_ от библиотеката _opencv_, добавете _img_ рамка с ширина 50 пиксела към всяка страна. Използвайте типа рамка _cv2.BORDER_REPLICATE_.

More: https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
"""

cv2_imshow(cv2.copyMakeBorder(src=img, top=50, bottom=50, left=50, right=50, borderType=cv2.BORDER_REPLICATE))

"""### <a name='8'></a> Exercise 248
Using the _cv2.copyMakeBorder()_ function from the _opencv_ library, add a 100-pixel-wide _img_ border to each side. Use border type _cv2.BORDER_REFLECT_.
Като използвате функцията _cv2.copyMakeBorder()_ от библиотеката _opencv_, добавете _img_ рамка с ширина 100 пиксела към всяка страна. Използвайте тип рамка _cv2.BORDER_REFLECT_.

More: https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
"""

cv2_imshow(cv2.copyMakeBorder(src=img, top=100, bottom=100, left=100, right=100, borderType=cv2.BORDER_REFLECT))

"""### <a name='9'></a> Exercise 249
Using the _cv2.copyMakeBorder()_ function from the _opencv_ library, add a 100-pixel-wide _img_ border to each side. Use the border type _cv2.BORDER_WRAP_.
Като използвате функцията _cv2.copyMakeBorder()_ от библиотеката _opencv_, добавете _img_ рамка с ширина 100 пиксела към всяка страна. Използвайте типа рамка _cv2.BORDER_WRAP_.

More; https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
"""

cv2_imshow(cv2.copyMakeBorder(src=img, top=100, bottom=100, left=100, right=100, borderType=cv2.BORDER_WRAP))

"""### <a name='10'></a> Exercise 250
Using the _cv2.rectangle()_ function from the _opencv_ library, add a rectangle border to the _img_ image surrounding the python logo. Set the color to green `color = (0, 255, 0)` and thickness to 3 pixels.
Използвайки функцията _cv2.rectangle()_ от библиотеката _opencv_, добавете правоъгълна рамка към изображението _img_ около логото на Python. Задайте цвета на зелен `color = (0, 255, 0)` и дебелина на 3 пиксела.
"""

cv2_imshow(cv2.rectangle(img=img.copy(), pt1=(120, 30), pt2=(280, 190), color=(0, 255, 0), thickness=3))

"""Using the _cv2.circle()_ function from the _opencv_ library add a circle to the _img_ image covering the python logo. Set the color to green `color = (0, 255, 0)`."""
"""Използвайки функцията _cv2.circle()_ от библиотеката _opencv_, добавете кръг към изображението _img_, покриващо логото на Python. Задайте цвета на зелен `color = (0, 255, 0)`."""

cv2_imshow(cv2.circle(img=img.copy(), center=(img.shape[1] // 2, img.shape[0] // 2), radius=80, color=(0, 255, 0), thickness=-1))

"""Using the _cv2.putText()_ function from the _opencv_ library, add 'Logo: Python' to the _img_ image in the upper left corner. Set the text position `org = (10, 40)`, font to `fontFace = cv2.FONT_HERSHEY_SIMPLEX`, font size to` fontScale = 1.2`, text color to yellow `color = (0, 255, 255)` and thickness ` thickness = 5`."""
"""Използвайки функцията _cv2.putText()_ от библиотеката _opencv_, добавете 'Лого: Python' към изображението _img_ в горния ляв ъгъл. Задайте позицията на текста `org = (10, 40)`, шрифта на ` fontFace = cv2.FONT_HERSHEY_SIMPLEX`, размер на шрифта до` fontScale = 1.2`, цвят на текста до жълто `color = (0, 255, 255)` и дебелина ` дебелина = 5`."""

cv2_imshow(cv2.putText(img=img.copy(), text='Logo: Python', org=(10, 40),
                       fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2,
                       color=(0, 255, 255), thickness=5))

