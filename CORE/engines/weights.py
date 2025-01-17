#!/usr/bin/env python3
# -*- coding:utf-8 -*-
##################################################################################
# File: c:\Projects\KENYA ONE PROJECT\CORE\engines\weights.py                    #
# Project: c:\Projects\KENYA ONE PROJECT\CORE\engines                            #
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
import matplotlib.pylab as plt  # type: ignore

print("  EMPTY WEIGHT BREAKDOWN                        ")
# initial percentage weights as given by Kundu

mtow = read_from_db("finalMTOW")
wfus = 0.085 * mtow
wwing = 0.09 * mtow
whtail = 0.02 * mtow
wvtail = 0.016 * mtow
wnacelle = 0.016 * mtow
wundercarriage = 0.05 * mtow
wengine = 0.185 * mtow
wenginecontrol = 0.02 * mtow
wfuelsystem = 0.015 * mtow
woilsystem = 0.003 * mtow
wapu = 0 * mtow
wflightcontsys = 0.015 * mtow
whydpneu = 0.0055 * mtow
welectrical = 0.025 * mtow
winstrument = 0.008 * mtow
wavionics = 0.02 * mtow
wecs = 0.004 * mtow
woxyg = 0 * mtow
wfurnishings = 0.04 * mtow
wmiscelleneous = 0.0015 * mtow
wcontigency = 0.01 * mtow

print("  A) FUSELAGE                         " + str(wfus) + "   lb")
print("  B) WING                             " + str(wwing) + " lb")
print("   C) PROPULSION ")
print("      a) engine dry weight " + str(wengine) + " lb")
print("      b) nacelle           " + str(wnacelle) + "  lb")
print("      c) engine control    " + str(wenginecontrol) + "  lb")
print("  D) UNDERCARRIAGE                    " + str(wundercarriage) + "    lb")
print("  E) TAIL                   ")

print("      a) horizontal tail      " + str(whtail) + "   lb")
print("      b) verticall tail      " + str(wvtail) + "   lb")
print("  F) SYSTEMS  ")
print("      a) fuel system       " + str(wfuelsystem) + "   lb")
print("      b) oil system        " + str(woilsystem) + "  lb")
print("      c) a.p.u             " + str(wapu) + "      lb")
print("      d) flight contr. sys " + str(wflightcontsys) + "   lb")
print("      e) hyd & pneu sys    " + str(whydpneu) + "  lb")
print("      f) electrical system " + str(welectrical) + "  lb")
print("      g) instruments       " + str(winstrument) + "  lb")
print("      h) avionics          " + str(wavionics) + "   lb")
print("      i) ecs               " + str(wecs) + "  lb")
print("      j) oxygen system     " + str(woxyg) + "      lb")
print("  G) FURNISHINGS                      " + str(wfurnishings) + " lb")
print("  H) CONTIGENCY                       " + str(wcontigency) + "  lb")
print("  I)MISCELLLENEOUS                    " + str(wmiscelleneous) + "  lb")
print("                                      _________    ")

calcemptyw = (
    wfus
    + wwing
    + whtail
    + wvtail
    + wnacelle
    + wundercarriage
    + wengine
    + wenginecontrol
    + wfuelsystem
    + woilsystem
    + wapu
    + wflightcontsys
    + whydpneu
    + welectrical
    + winstrument
    + wavionics
    + wecs
    + woxyg
    + wfurnishings
    + wmiscelleneous
    + wcontigency
)

We = read_from_db("emptyWeight")

error = ((calcemptyw - We) / We) * 100
print("  TOTAL CALCULATED EMPTY WEIGHT        " + str(calcemptyw) + "  lb")
print("                          ")
print("  INITIAL ESTIMATED EMPTY WEIGHT       " + str(We) + "  lb")

print("  PERCENTAGE ERROR            " + str(error), " %")
