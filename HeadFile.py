# -*- coding: utf-8 -*-
'''
导入公用模块，定义公共变量
Author: Jachin
Data: 2017- 11- 18
'''
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter.messagebox import *
import re
import time

import matplotlib.pylab as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

import pymssql

conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")

cur = conn.cursor()
Cid = 70001
def setCid(n):
    '''
    设置用户ID，确定登录的用户身份
    :param n: 
    :return: 
    '''
    global Cid
    Cid = n

