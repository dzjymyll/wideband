from HFSS import HFSS
import numpy as np
import math as mt
import csv
import keras
import os
_base_path = os.getcwd()


def costfunction():

    #fr = 4.706
    #fr = 5.583
    fr = 4
    h = HFSS()
    h.init()
    h.solve('Setup1')
    cost_value = h.export()
    return cost_value
