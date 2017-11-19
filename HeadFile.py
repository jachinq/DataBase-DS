# -*- coding: utf-8 -*-
'''
导入公用模块，定义公共变量
Author: Jachin
Data: 2017- 11- 
'''
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter.messagebox import *
import re
import time
import pymssql


conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")

cur = conn.cursor()
Cid = None
def setCid(n):
    global Cid
    Cid = n

