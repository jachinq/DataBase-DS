# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2317- 11- 
'''
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk

class User(Frame):
    def __init__(self,top = None):
        Frame.__init__(self,top)

        top.title('User')
        top.geometry("458x440+230+100")
        self.Main()
        top.mainloop()

    def Main(self):
        #五个图标
        self.ico_book = ImageTk.PhotoImage(Image.open(r'ico\book.png'))
        self.ico_user = ImageTk.PhotoImage(Image.open(r'ico\user.png'))
        self.ico_search = ImageTk.PhotoImage(Image.open(r'ico\search.png'))
        self.ico_shopping = ImageTk.PhotoImage(Image.open(r'ico\shopping.png'))
        self.ico_order = ImageTk.PhotoImage(Image.open(r'ico\order.png'))

        FrameMenu = tk.LabelFrame(top,text = '',background = 'white')
        FrameMenu.place(relx = 0,rely = 0,relheight = 0.22,relwidth = 1,)
        b_book = tk.Button(FrameMenu,image = self.ico_book,command = self.event_book
                           ,relief = 'groove')
        b_book.grid(column=0,row = 1)
        b_search = tk.Button(FrameMenu,image = self.ico_search,command = self.event_search
                             , relief='groove')
        b_search.grid(column=1,row = 1)
        b_shopping = tk.Button(FrameMenu,image = self.ico_shopping,command = self.event_shopping
                               ,relief = 'groove')
        b_shopping.grid(column=2,row = 1)
        b_order = tk.Button(FrameMenu,image = self.ico_order,command = self.event_order
                            , relief='groove')
        b_order.grid(column=3,row = 1)
        b_user = tk.Button(FrameMenu,image = self.ico_user,command = self.event_user
                           , relief='groove')
        b_user.grid(column=4,row = 1)


    def Page(self):
        #TODO 实现翻页
        pass
        FramePage =  tk.LabelFrame(top,text = '书籍',background = 'white')
        FramePage.place(relx = 0,rely = 0.22,relheight = 0.78,relwidth = 1,)


    def Det(self):
        #TODO 详情查看
        pass
        FrameDet =  tk.LabelFrame(top,text = '详情',background = 'white')
        FrameDet.place(relx = 0,rely = 0.22,relheight = 0.78,relwidth = 1,)

    def Shopping(self):
        #TODO 购物车
        pass
        FrameShopping =  tk.LabelFrame(top,text = '购物车',background = 'white')
        FrameShopping.place(relx = 0,rely = 0.22,relheight = 0.78,relwidth = 1,)

    def Order(self):
        #TODO 订单
        pass
        FrameOrder =  tk.LabelFrame(top,text = '订单',background = 'white')
        FrameOrder.place(relx = 0,rely = 0.22,relheight = 0.78,relwidth = 1,)

    def Search(self):
        #TODO 搜索
        pass

        style = Style()
        style.configure('TSeparator', background='#000000')
        style.configure('TLabel', anchor='w', font=(u'幼圆', 14),background = 'white'
                        ,relief = 'flat')

        FrameSearch =  tk.LabelFrame(top,text = '搜索',background = 'white')
        FrameSearch.place(relx = 0,rely = 0.22,relwidth = 1,relheight = 0.78,)

        labelSearchBName = Label(FrameSearch,text = '书名')
        labelSearchBName.place(relx = 0.05,rely = 0.05,relwidth = 0.2,relheight = 0.1)

        textSearch = tk.Text(FrameSearch, font=(u'幼圆', 18), relief='solid')#sunken,solid,raised,ridge,flat,groove
        textSearch.place(relx = 0.17,rely = 0.05,relwidth = 0.6,relheight = 0.1)

        buttonSearch = tk.Button(FrameSearch, text='Search', command=self.event_addToShop, relief = 'groove')
        buttonSearch.place(relx = 0.8,rely = 0.05, relwidth=0.11, relheight=0.1)

        Line1 = Separator(FrameSearch, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.23, relwidth=1.00, relheight=0.002)

    def User(self):
        #TODO 账户
        pass
        FrameUser =  tk.LabelFrame(top,text = '用户',background = 'white')
        FrameUser.place(relx = 0,rely = 0.22,relheight = 0.78,relwidth = 1,)


class Application(User):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        User.__init__(self, master)

    def event_book(self, event=None):
        #TODO 书籍页面
        pass
        self.Page()
    
    def event_search(self, event=None):
        #TODO 搜索
        pass
        self.Search()

    def event_shopping(self, event=None):
        #TODO 购物车页面
        pass
        self.Shopping()

    def event_order(self, event=None):
        #TODO 订单界面
        pass
        self.Order()

    def event_user(self, event=None):
        #TODO 用户个人界面
        pass
        self.User()

    def event_addToShop(self):
        #TODO 添加至购物车
        pass
        print '添加成功'

top = tk.Tk()
Application(top)