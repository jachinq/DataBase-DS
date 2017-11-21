# -*- coding: utf-8 -*-
'''
This is a scrpit for 找出数据库中没有而保存了封面的书籍
Author: Jachin
Data: 2017- 11- 
'''
import pymssql
from PIL import Image
import glob, os

path_ISBN = {}
for infile in glob.glob("*.thumbnail"):
    file, ext = os.path.splitext(infile)
    #print file#str
    path_ISBN[file] = None

conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")

cur = conn.cursor()
cur.execute('select ISBN,Bname from book')
bookISBN = cur.fetchall()

database_ISBN = {}
for i in bookISBN:
    database_ISBN[i[0].encode('utf-8')] = str(i[1].encode('utf-8'))

c = 0
for i in database_ISBN.keys():
    if i in path_ISBN.keys():
        del path_ISBN[i]
        c += 1
print c
for k,v in path_ISBN.items():
    print k,v