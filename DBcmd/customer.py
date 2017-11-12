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
cur.execute('select Cuser,Cpswd from customer')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
s = cur.fetchall()

def custom():
    cur.execute('select * from book')
    bookinfo = cur.fetchall()

    cur.execute('exec pro_shop')
    shopping = cur.fetchall()

    cur.execute('select * from orderinfo')
    order = cur.fetchall()

    cur.execute('select * from customer')
    customer = cur.fetchall()

    flag = True
    print '欢迎使用网上书店系统'
    while(flag):
        print '\n1.书籍概览'
        print '2.查找书籍'
        print '3.查看购物车'
        print '4.查看订单'
        print '5.修改个人信息'
        print '6.退出'
        i = int(raw_input('输入你的选择：'))
        if i == 1:
            for item in bookinfo:
                print '─'*38
                print '书名  %-14s |作者  %-8s |价格  %-4s'%(item[1],item[2],item[3])
            c_ques = raw_input('是否要查看某本书的详细信息(y/n)?')
            if c_ques == 'y' or c_ques == 'Y':
                name = raw_input('请输入书名：')
                exsit = 0
                for item in bookinfo:
                    if item[1].encode('utf-8') == name:
                        exsit = 1
                        print 'ISBN %s\n书名\t%s\n作者\t%s\n价格\t%s\n出版社\t%s\n库存\t%s'\
                              %(item[0],item[1],item[2],item[3],item[4],item[7])
                        print '简介',item[5]
                        print
                if not exsit:
                     print '没有这本书'
            raw_input('回车以继续。')
        elif i == 2:
            name = raw_input('请输入书名：')
            exsit = 0
            for item in bookinfo:
                if item[1].encode('utf-8') == name:
                    exsit = 1
                    print 'ISBN %s\n书名\t%s\n作者\t%s\n价格\t%s\n出版社\t%s\n库存\t%s' % (
                    item[0], item[1], item[2], item[3], item[4], item[7])
                    print '简介', item[5]
                    print
            if not exsit:
                print '没有这本书'
            raw_input('回车以继续。')
        elif i == 3:
            if shopping:
                print '编号  ISBN\t\t  书名\t\t\t\t\t\t 单价\t\t数量\t  总价 '
                for item,num in zip(shopping,range(len(shopping))):
                    tab = '%-3d %s %-' + str((32-len(item[3]))/3+len(item[3])) + 's %s   %d     %d'
                    print '─' * 38
                    print tab%(num,item[2],item[3],item[4],item[5],item[6])
                c_ques = raw_input('要下单吗(y/n)?')
                if c_ques == 'y' or c_ques == 'Y':
                    pass
            else:
                c_ques = raw_input('你的购物车为空，是否要添加书籍(y/n)?')
                if c_ques == 'y' or c_ques == 'Y':
                    pass
                else:
                    pass
            raw_input('回车以继续。')
        elif i == 4:
            pass
        elif i == 5:
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
            raw_input('回车以继续。')
        elif i == 6:
            flag = False

user = raw_input('账号：')
pswd = raw_input('密码：')
for item in s:
    if user == item[0] and pswd == item[1]:
        print '登录成功'
        custom()
else:
    print '账号或密码错误！'

cur.close()

conn.close()
