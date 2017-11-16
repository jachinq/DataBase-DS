# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2317- 11- 
'''
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
import pymssql

class User(Frame):
    def __init__(self,top = None):
        Frame.__init__(self,top)
        #top = tk.Tk()
        top.title('User')
        top.geometry("740x458+230+100")
        self.Main(top)
        top.mainloop()

    def Main(self,top):
        #五个图标
        self.ico_book = ImageTk.PhotoImage(Image.open(r'ico\book.png'))
        self.ico_user = ImageTk.PhotoImage(Image.open(r'ico\user.png'))
        self.ico_search = ImageTk.PhotoImage(Image.open(r'ico\search.png'))
        self.ico_shopping = ImageTk.PhotoImage(Image.open(r'ico\shopping.png'))
        self.ico_order = ImageTk.PhotoImage(Image.open(r'ico\order.png'))

        self.FrameMenu = tk.LabelFrame(top,text = '',background = 'white')
        self.FrameMenu.place(relx = 0,rely = 0,relheight = 1,relwidth = 0.13,)

        self.b_book = tk.Button(self.FrameMenu,image = self.ico_book,command = self.b_book
                           ,relief = 'groove')
        self.b_book.grid(column=1,row = 0)
        self.b_search = tk.Button(self.FrameMenu,image = self.ico_search,command = self.b_search
                             , relief='groove')
        self.b_search.grid(column=1,row = 1)
        self.b_shopping = tk.Button(self.FrameMenu,image = self.ico_shopping,command = self.b_shopping
                               ,relief = 'groove')
        self.b_shopping.grid(column=1,row = 2)
        self.b_order = tk.Button(self.FrameMenu,image = self.ico_order,command = self.b_order
                            , relief='groove')
        self.b_order.grid(column=1,row = 3)
        self.b_user = tk.Button(self.FrameMenu,image = self.ico_user,command = self.b_user
                           , relief='groove')
        self.b_user.grid(column=1,row = 4)


    def Page(self):
        #TODO 实现翻页
        pass
        cur.execute('select ISBN,Bname from book')
        self.BookInfo = cur.fetchall()

        def pro():
            if self.bookpage > 0:
                self.bookpage -= 1
                # print self.bookpage
                self.Page()

        def nex():
            if self.bookpage < self.maxpage:
                self.bookpage += 1
                self.Page()

        self.Btn = ['b_book' + str(i) for i in range(8)]
        self.Lab = ['l_name' + str(i) for i in range(8)]
        self.Im = ['im' + str(i) for i in range(8)]
        self.relx = [0.05, 0.26, 0.47, 0.68]
        style = Style()
        style.configure('book.TLabel', relief='flat'
                                ,wraplength = 100,justify = 'center'
                                , font = (u'幼圆',12),anchor='n'
                                ,background = 'white')

        self.FramePage =  tk.LabelFrame(top,text = '书籍',background = 'white')
        self.FramePage.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.88,)

        self.bp = ImageTk.PhotoImage(Image.open(r'ico\pro.png'))
        self.bn = ImageTk.PhotoImage(Image.open(r'ico\next.png'))

        self.b_pro = tk.Button(self.FramePage, relief='groove', command=pro,image = self.bp)
        self.b_pro.place(relx=0.88, rely=0.38, relwidth=0.1, relheight=0.1)
        #54.395 54.6375

        self.b_next = tk.Button(self.FramePage, relief='groove', command=nex,image = self.bn)
        self.b_next.place(relx=0.88, rely=0.48, relwidth=0.1, relheight=0.1)

        j = -1
        for i in range(8):
            if j < self.num:
                j += 1

            self.path = r''
            if self.bookpage < self.maxpage:
                self.path = r"thu\%s.thumbnail"%self.BookInfo[8*self.bookpage + i][0]
                self.Lab[i] = Label(self.FramePage, text=self.BookInfo[8 * self.bookpage + i][1],style = 'book.TLabel')
            elif self.bookpage == self.maxpage and j < self.num:
                self.path = r"thu\%s.thumbnail" % self.BookInfo[8 * self.bookpage + j][0]
                self.Lab[i] = Label(self.FramePage, text=self.BookInfo[8 * self.bookpage + i][1],style = 'book.TLabel')

            elif self.bookpage == self.maxpage and j >= self.num:
                self.path = r"ico\none.png"
                self.Lab[i] = Label(self.FramePage, text='',anchor='n')

            self.Im[i] = ImageTk.PhotoImage(Image.open(self.path))
            self.Btn[i] = tk.Button(self.FramePage,bg = 'white',image = self.Im[i]
                                    ,command = self.Det,relief = 'groove')

            #位置
            if i < 4:
                self.Btn[i].place(relx = self.relx[i],rely = 0.05,relwidth = 0.16,relheight = 0.345)
                self.Lab[i].place(relx=self.relx[i], rely=0.4, relwidth=0.16, relheight=0.09)
            elif i >=4:
                self.Btn[i].place(relx=self.relx[i-4], rely=0.5, relwidth=0.16, relheight=0.345)
                self.Lab[i].place(relx = self.relx[i-4],rely = 0.85,relwidth = 0.16,relheight = 0.09)

            if self.bookpage == self.maxpage and j >= self.num:
                self.Btn[i].place_forget()
                self.Lab[i].place_forget()

    def Det(self):
        #TODO 详情查看
        pass
        style = Style()
        self.FrameDet =  tk.LabelFrame(top,text = '详情',background = 'white')
        self.FrameDet.place(relx = 0.22,rely = 0,relheight = 1,relwidth = 0.78,)

        Command2 = Button(self.FrameDet, text='返回', command=self.Page, style='TButton')
        Command2.place(relx=0.761, rely=0.883, relwidth=0.108, relheight=0.067)

        Command1 = Button(self.FrameDet, text='加入购物车', command=self.event_addToShop, style='TButton')
        Command1.place(relx=0.513, rely=0.883, relwidth=0.21, relheight=0.067)

        Text7 = tk.Text(self.FrameDet, font=(u'宋体', 14), relief='solid')
        Text7.place(relx=0.265, rely=0.867, relwidth=0.179, relheight=0.084)

        Text6 = tk.Text(self.FrameDet, font=(u'宋体', 14), relief='solid')
        Text6.place(relx=0.23, rely=0.425, relwidth=0.639, relheight=0.395)

        Text5 = tk.Text(self.FrameDet, font=(u'宋体', 14), relief='solid')
        Text5.place(relx=0.637, rely=0.311, relwidth=0.232, relheight=0.051)

        Text4 = tk.Text(self.FrameDet, font=(u'宋体', 14), relief='solid')
        Text4.place(relx=0.23, rely=0.327, relwidth=0.144, relheight=0.051)

        Text3 = tk.Text(self.FrameDet, font=(u'宋体', 14), relief='solid')
        Text3.place(relx=0.637, rely=0.213, relwidth=0.232, relheight=0.051)

        Text2 = tk.Text(self.FrameDet, state='disabled', font=(u'宋体', 14), relief='solid')
        Text2.place(relx=0.23, rely=0.229, relwidth=0.144, relheight=0.051)

        Text1 = tk.Text(self.FrameDet, state='disabled', font=(u'宋体', 14), relief='solid')
        Text1.place(relx=0.44, rely=0.082, relwidth=0.43, relheight=0.067)

        style.configure('TSeparator', background='#000000')
        Line1 = Separator(self.FrameDet, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.196, relwidth=1.009, relheight=0.002)

        Label7 = Label(self.FrameDet, text='库存', style='Label7.TLabel')
        Label7.place(relx=0.071, rely=0.883, relwidth=0.144, relheight=0.051)

        Label6 = Label(self.FrameDet, text='简介', style='Label6.TLabel')
        Label6.place(relx=0.071, rely=0.442, relwidth=0.108, relheight=0.051)

        Label5 = Label(self.FrameDet, text='ISBN', style='Label5.TLabel')
        Label5.place(relx=0.513, rely=0.327, relwidth=0.073, relheight=0.051)

        Label4 = Label(self.FrameDet, text='出版社', style='Label4.TLabel')
        Label4.place(relx=0.071, rely=0.344, relwidth=0.108, relheight=0.035)

        Label3 = Label(self.FrameDet, text='定价', style='Label3.TLabel')
        Label3.place(relx=0.513, rely=0.213, relwidth=0.073, relheight=0.051)

        Label2 = Label(self.FrameDet, text='作者', style='Label2.TLabel')
        Label2.place(relx=0.088, rely=0.245, relwidth=0.091, relheight=0.035)

        Label1 = Label(self.FrameDet, text='书名', style='Label1.TLabel')
        Label1.place(relx=0.319, rely=0.082, relwidth=0.1, relheight=0.067)

    def Shopping(self,top):
        #TODO 购物车
        pass
        self.FrameShopping =  tk.LabelFrame(top,text = '购物车',background = 'white')
        self.FrameShopping.place(relx = 0.22,rely = 0,relheight = 1,relwidth = 0.78,)

    def Order(self,top):
        #TODO 订单
        pass
        self.FrameOrder =  tk.LabelFrame(top,text = '订单',background = 'white')
        self.FrameOrder.place(relx = 0.22,rely = 0,relheight = 1,relwidth = 0.78,)

    def Search(self,top):
        #TODO 搜索
        pass

        self.style = Style()
        self.style.configure('TSeparator', background='#000000')
        self.style.configure('search.TLabel', anchor='w', font=(u'幼圆', 14),background = 'white'
                        ,relief = 'flat')

        self.FrameSearch =  tk.LabelFrame(top,text = '搜索',background = 'white')
        self.FrameSearch.place(relx = 0.22,rely = 0,relheight = 1,relwidth = 0.78)

        self.labelSearchBName = Label(self.FrameSearch,text = '书名',style = 'search.TLabel')
        self.labelSearchBName.place(relx = 0.05,rely = 0.05,relwidth = 0.148,relheight = 0.06)

        self.textSearch = tk.Text(self.FrameSearch, font=(u'幼圆', 18), relief='solid')#sunken,solid,raised,ridge,flat,groove
        self.textSearch.place(relx = 0.17,rely = 0.05,relwidth = 0.6,relheight = 0.06)

        self.buttonSearch = tk.Button(self.FrameSearch, text='Search', command=self.event_search, relief = 'groove')
        self.buttonSearch.place(relx = 0.8,rely = 0.05, relwidth=0.11, relheight=0.06)

        self.Line1 = Separator(self.FrameSearch, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0., rely=0.18, relwidth=1.00, relheight=0.002)

    def User(self,top):
        #TODO 账户
        pass
        self.Cid = 70003
        cur.execute('exec pro_getUserInfo %d' % self.Cid)
        self.userInfo = cur.fetchall()
        self.userValues = ['userValues' + str(i) for i in range(9)]
        self.labelname = ['labelUserName', 'labelUserSex','labelUserReal', 'labelUserPost'
            ,  'labelUserEmail', 'labelUserPhone','labelUserAddress']
        self.labelshowname = ['昵称','性别','真实姓名','邮编','邮箱','联系方式','地址']
        self.entryname = ['entryUserName', 'entryUserSex', 'entryUserReal', 'entryUserPost'
            , 'entryUserEmail', 'entryUserPhone', 'entryUserAddress']

        for i in range(9):
            self.userValues[i] = tk.StringVar()
            self.userValues[i].set(self.userInfo[0][i])

        style = Style()
        style.configure('user.TLabel', anchor='w', font=(u'幼圆', 14), background='white'
                        , relief='flat',foreground = '#4141CF')
        self.FrameUser =  tk.LabelFrame(top,text = '用户',background = '#fff')
        self.FrameUser.place(relx = 0.22,rely = 0,relheight = 1,relwidth = 0.78)

        for i in range(7):
            self.labelname[i] = Label(self.FrameUser, text=self.labelshowname[i], style='user.TLabel')
            self.entryname[i] = tk.Entry(self.FrameUser, textvariable=self.userValues[i], state='normal'
                                 , font=(u'宋体', 18), relief='solid',bg = '#fff')

        self.labelname[0].place(relx=0.05, rely=0.05, relwidth=0.148, relheight=0.08)
        self.labelname[1].place(relx=0.55, rely=0.05, relwidth=0.148, relheight=0.08)
        self.labelname[2].place(relx=0.05, rely=0.20, relwidth=0.148, relheight=0.08)
        self.labelname[3].place(relx=0.55, rely=0.20, relwidth=0.148, relheight=0.08)
        self.labelname[4].place(relx=0.05, rely=0.35, relwidth=0.148, relheight=0.08)
        self.labelname[5].place(relx=0.05, rely=0.50, relwidth=0.148, relheight=0.08)
        self.labelname[6].place(relx=0.05, rely=0.65, relwidth=0.148, relheight=0.08)

        self.entryname[0].place(relx=0.25, rely=0.05, relwidth=0.148, relheight=0.08)
        self.entryname[1].place(relx=0.65, rely=0.05, relwidth=0.148, relheight=0.08)
        self.entryname[2].place(relx=0.25, rely=0.20, relwidth=0.148, relheight=0.08)
        self.entryname[3].place(relx=0.65, rely=0.20, relwidth=0.148, relheight=0.08)
        self.entryname[4].place(relx=0.25, rely=0.35, relwidth=0.6, relheight=0.08)
        self.entryname[5].place(relx=0.25, rely=0.50, relwidth=0.6, relheight=0.08)
        self.entryname[6].place(relx=0.25, rely=0.65, relwidth=0.6, relheight=0.08)


class Application(User):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        self.cur = conn.cursor()
        self.cur.execute('select ISBN,Bname from book')
        self.BookInfo = self.cur.fetchall()
        self.booknum = 0
        self.bookpage = 0
        self.maxpage = len(self.BookInfo) / 8
        self.num = 0
        if self.maxpage < len(self.BookInfo) / 8.0:
            self.num = len(self.BookInfo) % 8
        User.__init__(self, master)

    def b_book(self, event=None):
        #TODO 书籍页面
        pass
        self.Page()

    def b_search(self, event=None):
        #TODO 搜索界面
        pass
        self.Search(top)

    def b_shopping(self, event=None):
        #TODO 购物车页面
        pass
        self.Shopping(top)

    def b_order(self, event=None):
        #TODO 订单界面
        pass
        self.Order(top)

    def b_user(self, event=None):
        #TODO 用户个人界面
        pass
        self.User(top)

    def event_addToShop(self):
        #TODO 添加至购物车功能
        pass
        print '添加成功'

    def event_search(self):
        #TODO 搜索功能
        pass


conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")
cur = conn.cursor()
top = tk.Tk()
Application(top)
cur.close()
conn.close()


