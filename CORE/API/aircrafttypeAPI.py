#!/usr/bin/env python3
# -*- coding:utf-8 -*-
##################################################################################
# File: c:\Projects\KENYA ONE PROJECT\CORE\API\aircrafttypeAPI.py                #
# Project: c:\Projects\KENYA ONE PROJECT\CORE\API                                #
# Created Date: Thursday, January 9th 2020, 8:56:55 pm                           #
# Author: Geoffrey Nyaga Kinyua ( <info@geoffreynyaga.com> )                     #
# -----                                                                          #
# Last Modified: Thursday January 9th 2020 8:56:55 pm                            #
# Modified By:  Geoffrey Nyaga Kinyua ( <info@geoffreynyaga.com> )               #
# -----                                                                          #
# MIT License                                                                    #
#                                                                                #
# Copyright (c) 2020 KENYA ONE PROJECT                                           #
#                                                                                #
# Permission is hereby granted, free of charge, to any person obtaining a copy of#
# this software and associated documentation files (the "Software"), to deal in  #
# the Software without restriction, including without limitation the rights to   #
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies  #
# of the Software, and to permit persons to whom the Software is furnished to do #
# so, subject to the following conditions:                                       #
#                                                                                #
# The above copyright notice and this permission notice shall be included in all #
# copies or substantial portions of the Software.                                #
#                                                                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  #
# SOFTWARE.                                                                      #
# -----                                                                          #
# Copyright (c) 2020 KENYA ONE PROJECT                                           #
##################################################################################


import sys

sys.path.append("../")
from CORE.API.db_API import write_to_db, read_from_db

import numpy as np  # type: ignore
from sklearn import tree  # type: ignore
import pandas as pd  # type: ignore
import random


def aircraft_type(number_of_aircraft: int, mydict: list) -> int:

    finaldp: list = []

    LSA = number_of_aircraft

    def dpLSA() -> list:
        grossweight: int = random.randint(400, 1430)
        emptyweight: int = random.randint(200, 880)
        wingarea: int = random.randint(75, 160)
        wingspan: int = random.randint(17, 35)
        row: list = [grossweight, emptyweight, wingarea, wingspan, 0]
        return row

    for x in range(LSA):
        temp = dpLSA()
        finaldp.append(temp)

    sailplanes = number_of_aircraft

    def dpSailplanes() -> list:
        grossweight: int = random.randint(280, 1700)
        emptyweight: int = random.randint(100, 1100)
        wingarea: int = random.randint(120, 150)
        wingspan: int = random.randint(35, 101)
        row: list = [grossweight, emptyweight, wingarea, wingspan, 1]
        return row

    for x in range(sailplanes):
        temp = dpSailplanes()
        finaldp.append(temp)

    GA = number_of_aircraft

    def dpGA():
        grossweight = random.randint(1500, 12500)
        emptyweight = random.randint(800, 3000)
        wingarea = random.randint(150, 400)
        wingspan = random.randint(30, 45)
        row = [grossweight, emptyweight, wingarea, wingspan, 2]
        return row

    for x in range(GA):
        temp = dpGA()
        finaldp.append(temp)

    # In[10]:
    mydata = finaldp

    # print(finaldp,"finaldp")
    df = pd.DataFrame(
        mydata, columns=["grossweight", "emptyweight", "wingarea", "wingspan", "target"]
    )
    # training data
    train_target = np.array(df.target)
    # print(train_target, "train_target")
    # print(train_target)
    c = np.array(finaldp)
    train_data = np.delete(c, [4], axis=1)
    # print(train_data,"train_data")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_data, train_target)
    prediction = clf.predict([mydict])
    # prediction = prediction[0]
    # print(prediction,"prediction")
    return prediction[0]


# def fin(iter):
# 	return_matrixx = []
# 	for x in range(iter):
# 		c = aircraft_type(number_of_aircraft,mydict)
# 		return_matrixx.append(c)
# 	return (np.bincount(return_matrixx).argmax())


# return_matrix1 = []
# for x in range(20):
# 	c = aircraft_type()
# 	return_matrix1.append(c)

# # print(return_matrix)
# print(np.bincount(return_matrix1).argmax())

# return_matrix2 = []
# for x in range(20):
# 	c = aircraft_type()
# 	return_matrix2.append(c)

# # print(return_matrix)
# print(np.bincount(return_matrix2).argmax())

# return_matrix3 = []
# for x in range(20):
# 	c = aircraft_type()
# 	return_matrix3.append(c)

# # print(return_matrix)
# print(np.bincount(return_matrix3).argmax())

# return_matrix4 = []
# for x in range(20):
# 	c = aircraft_type()
# 	return_matrix4.append(c)

# # print(return_matrix)
# print(np.bincount(return_matrix4).argmax())

# return_matrix5 = []
# for x in range(20):
# 	c = aircraft_type()
# 	return_matrix5.append(c)

# # print(return_matrix)
# print(np.bincount(return_matrix5).argmax())
