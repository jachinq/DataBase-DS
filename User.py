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
        top.resizable(0,0)
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
        #do = ['do' + str(i) for i in range(8)]

        def do0(event):
            print self.BookInfo[8 * self.bookpage + 0][0],self.BookInfo[8 * self.bookpage + 0][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 0][0]
        self.Btn[0].bind('<Button-1>', do0)
        def do1(event):
            print self.BookInfo[8 * self.bookpage + 1][0],self.BookInfo[8 * self.bookpage + 1][1]
            self.BookInfoISBN =  self.BookInfo[8 * self.bookpage + 1][0]
        self.Btn[1].bind('<Button-1>', do1)
        def do2(event):
            print self.BookInfo[8 * self.bookpage + 2][0],self.BookInfo[8 * self.bookpage + 2][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 2][0]
        self.Btn[2].bind('<Button-1>', do2)
        def do3(event):
            print self.BookInfo[8 * self.bookpage + 3][0],self.BookInfo[8 * self.bookpage + 3][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 3][0]
        self.Btn[3].bind('<Button-1>', do3)
        def do4(event):
            print self.BookInfo[8 * self.bookpage + 4][0],self.BookInfo[8 * self.bookpage + 4][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 4][0]
        self.Btn[4].bind('<Button-1>', do4)
        def do5(event):
            print self.BookInfo[8 * self.bookpage + 5][0],self.BookInfo[8 * self.bookpage + 5][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 5][0]
        self.Btn[5].bind('<Button-1>', do5)
        def do6(event):
            print self.BookInfo[8 * self.bookpage + 6][0],self.BookInfo[8 * self.bookpage + 6][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 6][0]
        self.Btn[6].bind('<Button-1>', do6)
        def do7(event):
            print self.BookInfo[8 * self.bookpage + 7][0],self.BookInfo[8 * self.bookpage + 7][1]
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 7][0]
        self.Btn[7].bind('<Button-1>', do7)

    def Det(self):
        #TODO 详情查看
        pass
        style = Style()
        style.configure('bookDet.TLabel', relief='flat'
                        , font=(u'幼圆', 12), anchor='center'
                        , background='white',foreground = '#4141CF')
        style.configure('TButton', relief='flat', font=(u'幼圆', 12), anchor='center')
        self.FrameNone = tk.LabelFrame(top,text = '详情',background = 'white')
        self.FrameNone.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 1,)

        self.FrameDet =  tk.LabelFrame(self.FrameNone,background = 'white')
        self.FrameDet.place(relx = 0.145,rely = -0.01,relheight = 1,relwidth = 0.6,)

        def Back():
            self.FrameNone.destroy()
        self.btn_detB = Button(self.FrameDet, text='返回', command=Back, style='TButton')
        self.btn_detB.place(relx=0.76, rely=0.88, relwidth=0.12, relheight=0.08)

        self.btn_addTS = Button(self.FrameDet, text='加入购物车', command=self.event_addToShop, style='TButton')
        self.btn_addTS.place(relx=0.5, rely=0.88, relwidth=0.24, relheight=0.08)

        #图标
        P_det = tk.Canvas(self.FrameDet, bg='#FFFFFF')
        self.im_det = ImageTk.PhotoImage(Image.open(r'ico\det2.png'))
        P_det.create_image(0.4, 8, anchor='nw', image=self.im_det)
        P_det.place(relx=0.05, rely=-0.0, relwidth=0.16, relheight=0.18)
        comm = "exec pro_getBookDetInfo '%s'"%self.BookInfoISBN
        cur.execute(comm)
        self.BookDetInfo = cur.fetchall()
        self.bookValues=['a','b','c','d','e','f','g']
        Text_list = ['Text_name' + str(i) for i in range(7)]
        Lab_list = ['lab_name' + str(i) for i in range(7)]
        Lab_name = ['书名','作者','价格','出版社','ISBN','简介','库存']


        for i in range(7):
            self.bookValues[i] = tk.StringVar()
            self.bookValues[i] = self.BookDetInfo[0][i]

        #文本框，标签和分割线
            Text_list[i] = tk.Text(self.FrameDet
                 ,font = (14),relief = 'solid')
            Lab_list[i] = Label(self.FrameDet, text=Lab_name[i], style='bookDet.TLabel')
            Text_list[i].insert('insert',self.bookValues[i])
            Text_list[i].configure(state = 'disable')

        Text_list[6].place(relx=0.18, rely=0.88, relwidth=0.18, relheight=0.06)
        Text_list[5].place(relx=0.18, rely=0.5, relwidth=0.7, relheight=0.35)
        Text_list[4].place(relx=0.55, rely=0.42, relwidth=0.33, relheight=0.06)
        Text_list[3].place(relx=0.18, rely=0.33, relwidth=0.7, relheight=0.06)
        Text_list[2].place(relx=0.18, rely=0.42, relwidth=0.25, relheight=0.06)
        Text_list[1].place(relx=0.18, rely=0.24, relwidth=0.7, relheight=0.06)
        Text_list[0].place(relx=0.37, rely=0.082, relwidth=0.5, relheight=0.06)

        Lab_list[6].place(relx=0.07, rely=0.88, relwidth=0.1, relheight=0.06)
        Lab_list[5].place(relx=0.07, rely=0.5, relwidth=0.1, relheight=0.06)
        Lab_list[4].place(relx=0.45, rely=0.42, relwidth=0.1, relheight=0.06)
        Lab_list[3].place(relx=0.04, rely=0.33, relwidth=0.12, relheight=0.06)
        Lab_list[2].place(relx=0.06, rely=0.42, relwidth=0.1, relheight=0.06)
        Lab_list[1].place(relx=0.06, rely=0.24, relwidth=0.1, relheight=0.06)
        Lab_list[0].place(relx=0.25, rely=0.08, relwidth=0.1, relheight=0.06)

        style.configure('TSeparator', background='#000000')
        Line1 = Separator(self.FrameDet, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.196, relwidth=1.009, relheight=0.002)

        S = Scrollbar(self.FrameDet)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        S.config(command=Text_list[5].yview)
        Text_list[5].config(yscrollcommand=S.set)

    def Shopping(self):
        #TODO 购物车
        pass
        self.FrameShopping =  tk.LabelFrame(top,text = '购物车',background = 'white')
        self.FrameShopping.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.87,)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_ShopInfo = Treeview(self.FrameShopping,
                                       columns=('c1', 'c2','c3','c4'),
                                       show="headings")
        self.libox_ShopInfo.column('c1', width=80, anchor='center')
        self.libox_ShopInfo.column('c2', width=80, anchor='center')
        self.libox_ShopInfo.column('c3', width=80, anchor='center')
        self.libox_ShopInfo.column('c4', width=80, anchor='center')

        # 设置每列表头标题文本
        self.libox_ShopInfo.heading('c1', text='书名')
        self.libox_ShopInfo.heading('c2', text='单价')
        self.libox_ShopInfo.heading('c3', text='数量')
        self.libox_ShopInfo.heading('c4', text='总价')

        self.libox_ShopInfo.place(relx=0.1, rely=0.08, relwidth=0.77, relheight=0.7)
        # 滚动条
        ysb = Scrollbar(self.FrameShopping, orient='vertical', command=self.libox_ShopInfo.yview)
        xsb = Scrollbar(self.FrameShopping, orient='horizontal', command=self.libox_ShopInfo.xview)
        self.libox_ShopInfo.configure(yscroll=ysb.set, xscroll=xsb.set)
        ysb.config(command=self.libox_ShopInfo.yview)
        xsb.config(command=self.libox_ShopInfo.xview)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.btnSettlement = tk.Button(self.FrameShopping, text='结算', command=self.event_addToOrder, relief='groove')
        self.btnSettlement.place(relx=0.7, rely=0.8, relwidth=0.11, relheight=0.07)

        self.btnEditShop = tk.Button(self.FrameShopping, text='编辑', command=self.event_addToOrder, relief='groove')
        self.btnEditShop.place(relx=0.5, rely=0.8, relwidth=0.11, relheight=0.07)

    def Order(self):
        #TODO 订单
        pass
        self.FrameOrder =  tk.LabelFrame(top,text = '订单',background = 'white')
        self.FrameOrder.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.78,)

    def Search(self):
        #TODO 搜索
        pass
        self.style = Style()
        self.style.configure('TSeparator', background='#000000')
        self.style.configure('search.TLabel', anchor='w', font=(u'幼圆', 14),background = 'white'
                        ,relief = 'flat')

        self.FrameSearch =  tk.LabelFrame(top,background = 'white',text='搜索')
        self.FrameSearch.place(relx = 0.13,rely = 0,relwidth = 0.87,relheight = 1,)

        self.labelSearchBName = Label(self.FrameSearch,text = '书名',style = 'search.TLabel')
        #self.labelSearchBName.place(relx = 0.2,rely = 0.07,relwidth = 0.148,relheight = 0.06)

        self.textSearch = tk.Text(self.FrameSearch, font=18, relief='solid')
        self.textSearch.place(relx = 0.22,rely = 0.05,relwidth = 0.4,relheight = 0.06)

        self.buttonSearch = tk.Button(self.FrameSearch, text='Search', command=self.event_search, relief = 'groove')
        self.buttonSearch.place(relx = 0.65,rely = 0.05, relwidth=0.11, relheight=0.07)

        self.var = tk.StringVar()
        self.var.set('书名')

        self.r1 = Radiobutton(top, text='书名', variable=self.var, value='书名')
        self.r1.place(relx = 0.35,rely = 0.17,relwidth = 0.07,relheight = 0.05)
        self.r2 = Radiobutton(top, text='作者', variable=self.var, value='作者')
        self.r2.place(relx = 0.45,rely = 0.17,relwidth = 0.07,relheight = 0.05)

        self.Line1 = Separator(self.FrameSearch, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0.14, rely=0.22, relwidth=0.69, relheight=0.007)

        self.Line2 = Separator(self.FrameSearch, orient='vertical', style='Line1.TSeparator')
        self.Line2.place(relx=0.14, rely=-0.015, relwidth=0.002, relheight=1.1)
        self.Line2 = Separator(self.FrameSearch, orient='vertical', style='Line1.TSeparator')
        self.Line2.place(relx=0.83, rely=-0.015, relwidth=0.002, relheight=1.1)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_bookInfo = Treeview(self.FrameSearch,
                        columns=('c1', 'c2'),
                        show="headings")
        self.libox_bookInfo.column('c1', width=80, anchor='center')
        self.libox_bookInfo.column('c2', width=80, anchor='center')

        # 设置每列表头标题文本
        self.libox_bookInfo.heading('c1', text='书名')
        self.libox_bookInfo.heading('c2', text='作者')

        #滚动条
        self.libox_bookInfo.place(relx=0.2, rely=0.3, relwidth=0.57, relheight=0.5)
        ysb = Scrollbar(self.FrameSearch, orient='vertical', command=self.libox_bookInfo.yview)
        xsb = Scrollbar(self.FrameSearch, orient='horizontal', command=self.libox_bookInfo.xview)
        self.libox_bookInfo.configure(yscroll=ysb.set, xscroll=xsb.set)
        ysb.config(command=self.libox_bookInfo.yview)
        xsb.config(command=self.libox_bookInfo.xview)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.btnShowDet = tk.Button(self.FrameSearch, text='查看详情', command=self.SearchToDet, relief='groove')
        self.btnShowDet.place(relx=0.66, rely=0.85, relwidth=0.11, relheight=0.07)

        #self.libox_bookInfo.bind('<Double-Button-1>',self.SearchToDet)

    def User(self):
        #TODO 账户
        pass
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
        self.style = Style()
        #设置列表的标题风格
        self.style.configure("Treeview.Heading", foreground='blue')

        self.cur = conn.cursor()
        self.cur.execute('select ISBN,Bname from book')
        self.BookInfo = self.cur.fetchall()
        self.bookpage = 0
        self.maxpage = len(self.BookInfo) / 8
        self.num = 0
        if self.maxpage < len(self.BookInfo) / 8.0:
            self.num = len(self.BookInfo) % 8

        self.Cid = 70003

        User.__init__(self, master)

    def b_book(self, event=None):
        #TODO 书籍页面
        pass
        self.Page()

    def b_search(self, event=None):
        #TODO 搜索界面
        pass
        self.Search()

    def b_shopping(self, event=None):
        #TODO 购物车页面
        pass
        self.Shopping()


    def b_order(self, event=None):
        #TODO 订单界面
        pass
        self.Order()

    def b_user(self, event=None):
        #TODO 用户个人界面
        pass
        self.User()

    def event_addToShop(self):
        #TODO 添加至购物车功能
        pass
        print '添加成功'

    def SearchToDet(self):
        list_box_bookname = self.libox_bookInfo.item(self.libox_bookInfo.focus(), "values")[0]
        for i in self.BookInfo:
            if list_box_bookname == i[1]:
                self.BookInfoISBN = i[0]
                break
        self.Det()

    def event_search(self):
        #TODO 搜索功能
        #print self.BookInfo
        cur.execute('select ISBN,Bname,Bauth from book')
        self.BookInfo = cur.fetchall()
        self.libox_bookInfo.delete(*self.libox_bookInfo.get_children())
        if self.var.get() == u'书名':
            for i in range(len(self.BookInfo)):
                if self.textSearch.get("1.0") in self.BookInfo[i][1]:
                    self.libox_bookInfo.insert('', i, v=[self.BookInfo[i][1], self.BookInfo[i][2]])
        if self.var.get() == u'作者':
            for i in range(len(self.BookInfo)):
                if self.textSearch.get("1.0") in self.BookInfo[i][2]:
                    self.libox_bookInfo.insert('', i, v=[self.BookInfo[i][1], self.BookInfo[i][2]])

    def event_addToOrder(self):
        #TODO 把购物车的书籍清空，生成相应的的订单
        pass

conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")
cur = conn.cursor()
top = tk.Tk()
Application(top)
cur.close()
conn.close()


