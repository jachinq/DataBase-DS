# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2017- 11- 
'''
from __future__ import unicode_literals

import pymssql
conn = pymssql.connect(host='localhost:1433',user='sa',password='ghostttt',database='BookStore',charset="utf8")
cur = conn.cursor()
cur.execute('select Cuser,Cpswd,Cid from customer')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
s = cur.fetchall()

def search():
    cur.execute('select * from book')
    bookinfo = cur.fetchall()
    name = raw_input('请输入书名：')
    exsit = 0
    for item in bookinfo:
        if item[1].encode('utf-8') == name:
            exsit = 1
            print 'ISBN：%s\n书名：\t%s\n作者：\t%s\n价格：\t%s\n出版社：\t%s\n库存：\t%s' \
                  % (item[0], item[1], item[2], item[3], item[4], item[7])
            print '简介', item[5]
            print
    if not exsit:
        print '没有这本书'

def showshopping():
    cur.execute('exec pro_shop %d' % (cid))
    shopping = cur.fetchall()
    if shopping:
        print '编号\t\tISBN\t\t书名\t\t\t\t\t  单价\t   数量\t\t总价 '
        for item, num in zip(shopping, range(len(shopping))):
            tab = ' %-2d\t%s\t%s %s\t\t%d\t\t%d'
            print '─' * 38
            length = 20 - len(item[3])*2 + len(item[3])
            print tab % (num, item[2].ljust(13), item[3].ljust(length), item[4], item[5], item[6])
        c_ques = raw_input('要下单吗(y/n)?')
        if c_ques == 'y' or c_ques == 'Y':
            pass
    else:
        print ('你的购物车为空')

def addToShopping():
    cur.execute('exec pro_shop %d' % (cid))
    shopping = cur.fetchall()
    name = raw_input('请输入书名：')
    exsit = 0
    for item in bookinfo:
        if item[1].encode('utf-8') == name:
            exsit = 1
            print 'ISBN：%s\n书名：\t%s\n作者：\t%s\n价格：\t%s\n出版社：\t%s\n库存：\t%s' \
                  % (item[0], item[1], item[2], item[3], item[4], item[7])
            print '=' * 18 + '\n简介', item[5]
            print '=' * 18
            c_ques = raw_input('要将这本书加入购物车吗(y/n)?')
            if c_ques == 'y' or c_ques == 'Y':
                hmuch = int(raw_input('要加入多少本?'))
                if hmuch > 0:
                    try:
                        cur.execute('insert into shopping values(%s,%s,%d,%.2f)'
                                % (cid, item[0], hmuch, hmuch * float(item[3].strip('元'))))
                        conn.commit()
                    except:
                        cur.execute('select Ocount,price from shopping where cid = %d and ISBN = %s'
                                         %(cid,item[0]))
                        sh = cur.fetchall()
                        cur.execute('update shopping set ocount = %d,price = %.2f where cid = %d and isbn = %s'
                                    % (hmuch+sh[0][0], sh[0][1]+hmuch * float(item[3].strip('元')),cid, item[0]))
                        conn.commit()
            else:
                pass
    if not exsit:
        print '没有这本书'

def changeinfo():
    c_ques = raw_input('您目前信息如下，是否要修改(y/n)?')
    if c_ques == 'y' or c_ques == 'Y':
        c_ques = raw_input('是否要修改全部(y/n)?')
        if c_ques == 'y' or c_ques == 'Y':
            custominfo = raw_input('请分别输入账号,密码,真名,性别,联系方式,邮箱,住址,邮编\n'
                                   '每一项之间用\';\'分隔')
        else:
            which = raw_input('需要修改哪一项?\n'
                              '1.账号,2.密码,3.真名,4.性别,5.联系方式,6.邮箱,7.住址,8.邮编')
            if which == '1':
                pass
            elif which == '2':
                pass
            elif which == '3':
                pass
            elif which == '4':
                pass
            elif which == '5':
                pass
            elif which == '6':
                pass
            elif which == '7':
                pass
            elif which == '8':
                pass
    else:
        print '放弃了修改。'


def custom():
    print '欢迎使用网上书店系统'
    while True:
        print '\n1.书籍概览'
        print '2.查找书籍'
        print '3.购书'
        print '4.查看购物车'
        print '5.查看订单'
        print '6.修改个人信息'
        print '0.退出'
        i = int(raw_input('输入你的选择：'))
        if i == 1:
            cur.execute('select * from book')
            bookinfo = cur.fetchall()
            for item in bookinfo:
                print '─'*38
                length1 = 30 - len(item[1]) * 2 + len(item[1])
                length2 = 30 - len(item[2]) * 2 + len(item[2])
                print '%s %s %-4s'%(item[1].ljust(length1),item[2].ljust(length2),item[3])
            c_ques = raw_input('是否要查看某本书的详细信息(y/n)?')
            if c_ques == 'y' or c_ques == 'Y':
                search()
            raw_input('回车以继续。')
        elif i == 2:
            search()
            raw_input('回车以继续。')
        elif i == 3:
            addToShopping()
            raw_input('回车以继续。')
        elif i == 4:
            showshopping()
            raw_input('回车以继续。')
        elif i == 5:
            pass
        elif i == 6:
            changeinfo()
            raw_input('回车以继续。')
        elif i == 0:
            break

user = raw_input('账号：')
pswd = raw_input('密码：')
for item in s:
    if user == item[0] and pswd == item[1]:
        print '登录成功'
        cur.execute('select * from book')
        bookinfo = cur.fetchall()

        cur.execute('exec pro_shop %d' % (item[2]))
        shopping = cur.fetchall()

        cur.execute('select * from orderinfo')
        order = cur.fetchall()

        cur.execute('select * from customer')
        customer = cur.fetchall()

        cid = item[2]
        cpswd = item[1]
        cuser = item[0]
        custom()
else:
    print '账号或密码错误！'

cur.close()

conn.close()
