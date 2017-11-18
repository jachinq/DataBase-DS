# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2317- 11- 
'''
import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter.messagebox import *
import re
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
        self.b_shop = tk.Button(self.FrameMenu,image = self.ico_shopping,command = self.b_shopping
                               ,relief = 'groove')
        self.b_shop.grid(column=1,row = 2)
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
        self.Text_list = ['Text_name' + str(i) for i in range(7)]
        Lab_list = ['lab_name' + str(i) for i in range(7)]
        Lab_name = ['书名','作者','价格','出版社','ISBN','简介','库存']


        for i in range(7):
            self.bookValues[i] = tk.StringVar()
            self.bookValues[i] = self.BookDetInfo[0][i]

        #文本框，标签和分割线
            self.Text_list[i] = tk.Text(self.FrameDet
                 ,font = (14),relief = 'solid')
            Lab_list[i] = Label(self.FrameDet, text=Lab_name[i], style='bookDet.TLabel')
            self.Text_list[i].insert('insert',self.bookValues[i])
            self.Text_list[i].configure(state = 'disable')

        self.Text_list[6].place(relx=0.18, rely=0.88, relwidth=0.18, relheight=0.06)
        self.Text_list[5].place(relx=0.18, rely=0.5, relwidth=0.7, relheight=0.35)
        self.Text_list[4].place(relx=0.55, rely=0.42, relwidth=0.33, relheight=0.06)
        self.Text_list[3].place(relx=0.18, rely=0.33, relwidth=0.7, relheight=0.06)
        self.Text_list[2].place(relx=0.18, rely=0.42, relwidth=0.25, relheight=0.06)
        self.Text_list[1].place(relx=0.18, rely=0.24, relwidth=0.7, relheight=0.06)
        self.Text_list[0].place(relx=0.37, rely=0.082, relwidth=0.5, relheight=0.06)

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
        S.config(command=self.Text_list[5].yview)
        self.Text_list[5].config(yscrollcommand=S.set)

    def Shopping(self):
        #TODO 购物车
        pass
        self.FrameShopping =  tk.LabelFrame(top,text = '购物车',background = 'white')
        self.FrameShopping.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.87,)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_ShopInfo = Treeview(self.FrameShopping,
                                       columns=('c1', 'c2','c3','c4'),
                                       show="headings")
        self.libox_ShopInfo.column('c1', width=200, anchor='center')
        self.libox_ShopInfo.column('c2', width=40, anchor='center')
        self.libox_ShopInfo.column('c3', width=10, anchor='center')
        self.libox_ShopInfo.column('c4', width=40, anchor='center')

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

        self.btnSettlement = tk.Button(self.FrameShopping, text='结算', command=self.event_addToOrder
                                       , relief='groove',font = (u'幼圆',14))
        self.btnEditShop = tk.Button(self.FrameShopping, text='编辑数量', command=self.event_editOcount
                                     , relief='groove',font = (u'幼圆',14))
        self.btnDelShop = tk.Button(self.FrameShopping, text='移出购物车', command=self.event_removeFromShop
                                    , relief='groove',font = (u'幼圆',14))
        self.btnFlash = tk.Button(self.FrameShopping, text='刷新', command=self.b_shopping
                                    , relief='groove',font = (u'幼圆',14))
        self.btnDelShop.place(relx=0.31, rely=0.83, relwidth=0.18, relheight=0.07)
        self.btnEditShop.place(relx=0.51, rely=0.83, relwidth=0.15, relheight=0.07)
        self.btnSettlement.place(relx=0.76, rely=0.83, relwidth=0.11, relheight=0.07)
        self.btnFlash.place(relx=0.1, rely=0.83, relwidth=0.11, relheight=0.07)

    def Order(self):
        #TODO 订单
        pass
        self.FrameOrder =  tk.LabelFrame(top,text = '订单',background = 'white')
        self.FrameOrder.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.87,)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_ShopInfo = Treeview(self.FrameOrder,
                                       columns=('c1', 'c2', 'c3', 'c4'),
                                       show="headings")
        self.libox_ShopInfo.column('c1', width=200, anchor='center')
        self.libox_ShopInfo.column('c2', width=40, anchor='center')
        self.libox_ShopInfo.column('c3', width=10, anchor='center')
        self.libox_ShopInfo.column('c4', width=40, anchor='center')

        # 设置每列表头标题文本
        self.libox_ShopInfo.heading('c1', text='书名')
        self.libox_ShopInfo.heading('c2', text='单价')
        self.libox_ShopInfo.heading('c3', text='数量')
        self.libox_ShopInfo.heading('c4', text='总价')

        self.libox_ShopInfo.place(relx=0.1, rely=0.08, relwidth=0.77, relheight=0.7)
        # 滚动条
        ysb = Scrollbar(self.FrameOrder, orient='vertical', command=self.libox_ShopInfo.yview)
        xsb = Scrollbar(self.FrameOrder, orient='horizontal', command=self.libox_ShopInfo.xview)
        self.libox_ShopInfo.configure(yscroll=ysb.set, xscroll=xsb.set)
        ysb.config(command=self.libox_ShopInfo.yview)
        xsb.config(command=self.libox_ShopInfo.xview)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.btnSettlement = tk.Button(self.FrameOrder, text='结算', command=self.event_addToOrder
                                       , relief='groove', font=(u'幼圆', 14))
        self.btnEditShop = tk.Button(self.FrameOrder, text='编辑数量', command=self.event_editOcount
                                     , relief='groove', font=(u'幼圆', 14))
        self.btnDelShop = tk.Button(self.FrameOrder, text='移出购物车', command=self.event_removeFromShop
                                    , relief='groove', font=(u'幼圆', 14))
        self.btnFlash = tk.Button(self.FrameOrder, text='刷新', command=self.b_shopping
                                  , relief='groove', font=(u'幼圆', 14))
        self.btnDelShop.place(relx=0.31, rely=0.83, relwidth=0.18, relheight=0.07)
        self.btnEditShop.place(relx=0.51, rely=0.83, relwidth=0.15, relheight=0.07)
        self.btnSettlement.place(relx=0.76, rely=0.83, relwidth=0.11, relheight=0.07)
        self.btnFlash.place(relx=0.1, rely=0.83, relwidth=0.11, relheight=0.07)

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
        style = Style()
        style.configure('user.TLabel', anchor='w', font=(u'幼圆', 14), background='white'
                        , relief='flat', foreground='#4141CF')

        cur.execute('exec pro_getUserInfo %d' % self.Cid)
        self.userInfo = cur.fetchall()
        self.userValues = ['userValues' + str(i) for i in range(9)]
        self.labelname = ['labelUserName', 'labelUserSex','labelUserReal', 'labelUserPost'
            ,  'labelUserEmail', 'labelUserPhone','labelUserAddress']
        self.labelshowname = ['账户','性别','姓名','邮编','邮箱','手机','地址']
        self.entryname = ['entryUserName', 'entryUserSex', 'entryUserReal', 'entryUserPost'
            , 'entryUserEmail', 'entryUserPhone', 'entryUserAddress']

        for i in range(7):
            self.userValues[i] = tk.StringVar()
            self.userValues[i].set(self.userInfo[0][i])

        self.FrameUser =  tk.LabelFrame(top,text = '用户',background = '#fff')
        self.FrameUser.place(relx = 0.13,rely = 0,relheight = 1,relwidth = 0.87)
        self.userValue = ['userInfo'+str(i) for i in range(7)]
        for i in range(7):
            self.labelname[i] = Label(self.FrameUser, text=self.labelshowname[i], style='user.TLabel')
            self.entryname[i] = tk.Entry(self.FrameUser,state = 'readonly',textvariable = self.userValues[i]
                                 , font=(u'宋体', 18), relief='solid',fg = 'black')

        self.labelname[0].place(relx=0.2, rely=0.05, relwidth=0.148, relheight=0.08)
        self.labelname[1].place(relx=0.5, rely=0.05, relwidth=0.148, relheight=0.08)
        self.labelname[2].place(relx=0.2, rely=0.20, relwidth=0.148, relheight=0.08)
        self.labelname[3].place(relx=0.5, rely=0.20, relwidth=0.148, relheight=0.08)
        self.labelname[4].place(relx=0.2, rely=0.35, relwidth=0.148, relheight=0.08)
        self.labelname[5].place(relx=0.2, rely=0.50, relwidth=0.148, relheight=0.08)
        self.labelname[6].place(relx=0.2, rely=0.65, relwidth=0.148, relheight=0.08)

        self.entryname[0].place(relx=0.27, rely=0.05, relwidth=0.148, relheight=0.08)
        self.entryname[1].place(relx=0.57, rely=0.05, relwidth=0.148, relheight=0.08)
        self.entryname[2].place(relx=0.27, rely=0.20, relwidth=0.148, relheight=0.08)
        self.entryname[3].place(relx=0.57, rely=0.20, relwidth=0.148, relheight=0.08)
        self.entryname[4].place(relx=0.27, rely=0.35, relwidth=0.45, relheight=0.08)
        self.entryname[5].place(relx=0.27, rely=0.50, relwidth=0.45, relheight=0.08)
        self.entryname[6].place(relx=0.27, rely=0.65, relwidth=0.45, relheight=0.16)


        self.btnEditPswd = tk.Button(self.FrameUser, text='修改密码', command=self.EditUserPswd
                                       , relief='groove',font = (u'幼圆',14))
        self.btnEditUserInfo = tk.Button(self.FrameUser, text='修改信息', command=self.event_editUserInfo
                                     , relief='groove',font = (u'幼圆',14))
        self.btnEditPswd.place(relx=0.32, rely=0.85, relwidth=0.15, relheight=0.07)
        self.btnEditUserInfo.place(relx=0.52, rely=0.85, relwidth=0.15, relheight=0.07)

    def EditUserPswd(self):
        FrameEditPswd = tk.LabelFrame(self.FrameUser)

        FrameEditPswd.place(relx=0.2, rely=0.35, relwidth=0.55, relheight=0.6)
        #top.withdraw()top.state("zoomed")
        #top.deiconify()
        label_pswd = Label(FrameEditPswd,text = '修改密码',font = 14)
        label_pswd.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=0.08)

        label_orgin = Label(FrameEditPswd,text = '原密码',font = 14)
        label_newpswd = Label(FrameEditPswd,text = '新密码',font = 14)
        label_repswd = Label(FrameEditPswd,text = '确认密码',font = 14)
        label_orgin.place(relx=0.08, rely=0.2, relwidth=0.2, relheight=0.1)
        label_newpswd.place(relx=0.08, rely=0.4, relwidth=0.2, relheight=0.1)
        label_repswd.place(relx=0.08, rely=0.6, relwidth=0.2, relheight=0.1)
        entry_orgin = Entry(FrameEditPswd,font=(u'宋体', 14))
        entry_newpswd = Entry(FrameEditPswd,font=(u'宋体', 14),show = '*')
        entry_repswd = Entry(FrameEditPswd,font=(u'宋体', 14),show = '*')

        entry_orgin.place(relx=0.28, rely=0.2, relwidth=0.6, relheight=0.12)
        entry_newpswd.place(relx=0.28, rely=0.4, relwidth=0.6, relheight=0.12)
        entry_repswd.place(relx=0.28, rely=0.6, relwidth=0.6, relheight=0.12)

        Line_s = Separator(FrameEditPswd, orient='horizontal', style='Line1.TSeparator')
        Line_s.place(relx=0.0, rely=0.08, relwidth=1, relheight=0.007)

        def RePswd():
            '''
            确认修改密码，检测原密码是否正确。新密码是否输入一致
            全部信息确认无误后提交到数据库
            :return: 
            '''
            cur.execute('select Cid,Cpswd from customer where Cid = %d'% self.Cid)
            #conn.commit()
            userPswd = cur.fetchall()
            #print entry_orgin.get()
            if entry_orgin.get() != userPswd[0][1]:
                showerror('Error','原密码错误')
            elif entry_newpswd.get()==entry_repswd.get():
                if entry_newpswd.get()!='':
                    comm = "update customer set Cpswd = '%s' where cid = %d"%(entry_repswd.get(),self.Cid)
                    cur.execute(comm)
                    conn.commit()
                    FrameEditPswd.destroy()
                    showinfo('提示','修改成功')
                else:
                    showerror('错误','密码不能为空')
            else:
                showerror('错误','两次输入密码不一致')

        btnEditUserInfo = tk.Button(FrameEditPswd,text='确认修改',command=RePswd,relief='groove',font=(u'幼圆', 14))
        btnEditUserInfo.place(relx=0.58, rely=0.8, relwidth=0.3, relheight=0.12)

    def EditShopOcount(self):
        FrameEditShopO = tk.LabelFrame(self.FrameShopping)
        FrameEditShopO.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.3)

        label_title = Label(FrameEditShopO, text='修改数量', font=14)
        label_title.place(relx=0.0, rely=0.0, relwidth=0.4, relheight=0.2)

        entry_shopNum = Entry(FrameEditShopO, font=(u'宋体', 14))
        entry_shopNum.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.2)

        Line_s = Separator(FrameEditShopO, orient='horizontal', style='Line1.TSeparator')
        Line_s.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.007)

        def reNum():
            '''
            确认修改数量，自动修改相应的总价
            :return: 
            '''
            self.cur.execute('select ISBN,Bname from book')
            self.BookInfo = self.cur.fetchall()
            list_bookName = ''#保存ISBN
            list_box_bookname = self.libox_ShopInfo.item(self.libox_ShopInfo.focus(), "values")[0]#保存选中的书的ISBN
            for i in self.BookInfo:
                if list_box_bookname == i[1]:
                    list_bookName = i[0]
                    break
            list_bookNum = self.libox_ShopInfo.item(self.libox_ShopInfo.focus(), "values")[2]#保存数量
            list_bookPrice = self.libox_ShopInfo.item(self.libox_ShopInfo.focus(), "values")[3]#保存总价
            if entry_shopNum.get()!='':  #判断输入数量是否不空
                if entry_shopNum.get().isdigit(): #判断输入是否为数字
                    num =  int(entry_shopNum.get())  #获取已有书本数
                    price =  float(list_bookPrice)/int(list_bookNum)*num #获取书籍单价
                    cur.execute('update shopping set Ocount = %d,price = %.2f where Cid = %d and ISBN = %s'%(num,price,self.Cid,list_bookName))
                    conn.commit()
                    FrameEditShopO.destroy()
                    showinfo('提示','修改成功')
                else:
                    showwarning('警告','只能输入整数')
            else:
                showwarning('警告','值不能为空')


        btnEditUserInfo = tk.Button(FrameEditShopO,text='确认',command = reNum
                                    ,relief='groove',font=(u'幼圆', 14))
        btnEditUserInfo.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.2)

class Application(User):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        self.style = Style()
        #设置列表的标题风格
        self.style.configure("Treeview.Heading", foreground='blue')
        self.style.configure("Treeview", font=12)

        self.cur = conn.cursor()
        self.cur.execute('select ISBN,Bname from book')
        self.BookInfo = self.cur.fetchall()
        self.bookpage = 0
        self.maxpage = len(self.BookInfo) / 8
        self.num = 0
        if self.maxpage < len(self.BookInfo) / 8.0:
            self.num = len(self.BookInfo) % 8

        self.Cid = 70001

        User.__init__(self, master)

    def b_book(self, event=None):
        #TODO 书籍页面
        pass
        self.Page()

    def b_search(self, event=None):
        #TODO 搜索界面
        pass
        self.Search()

    def b_shopping(self):
        '''
        查看购物车信息，可以结算，可以编辑购物车，包括修改已有书籍数量，和删除已有的购物项
        :param event: 
        :return: 
        '''
        #TODO 购物车页面
        pass
        self.Shopping()
        cur.execute("exec pro_shop %d"%self.Cid)
        self.ShopInfo = cur.fetchall()
        for i in range(len(self.ShopInfo)):
            self.libox_ShopInfo.insert('', i, v=[self.ShopInfo[i][3], self.ShopInfo[i][4]
                ,self.ShopInfo[i][5], self.ShopInfo[i][6]])

    def b_order(self, event=None):
        #TODO 订单界面
        pass
        self.Order()

    def b_user(self, event=None):
        #TODO 用户个人界面
        pass
        self.User()

    def event_addToShop(self):
        '''添加至购物车功能,每次默认添加一本，修改数量要使用购物车页面的编辑数量功能
        '''
        pass
        ISBN = str(self.Text_list[4].get("1.0","12.0"))
        price = float(self.Text_list[2].get("1.0","16.0")[0:-2])
        Ocount = 1
        comm = '''exec pro_addtoshop %d,'%s',%d,%f''' % (self.Cid, ISBN, Ocount, price)
        cur.execute(comm)
        try:
            s = cur.fetchall()
            price = s[0][1] / s[0][0] * (Ocount + s[0][0])
            cur.execute('update shopping set ocount = %d,price = %.2f where cid = %d and isbn = %s' % (
                Ocount + s[0][0], price, self.Cid, ISBN))
            conn.commit()
            showinfo('提示','追加成功！')
        except:
            conn.commit()
            showinfo('提示','添加成功！')

    def event_editOcount(self):
        #TODO 编辑购物车书籍数量
        pass

        if self.libox_ShopInfo.focus():
            self.btnSettlement.configure(state = 'disable')
            self.btnEditShop.configure(state = 'disable')
            self.btnDelShop.configure(state = 'disable')
            self.EditShopOcount()
        else:
            showwarning('警告','选择要修改的项目')

    def event_removeFromShop(self):
        #TODO 将书籍移出购物车
        if self.libox_ShopInfo.focus():
            list_bookName = ''
            list_box_bookname = self.libox_ShopInfo.item(self.libox_ShopInfo.focus(), "values")[0]  # 保存选中的书的ISBN
            for i in self.BookInfo:
                if list_box_bookname == i[1]:
                    list_bookName = i[0]
                    break
            if  'yes' == askquestion('移除','真的要移出购物车吗?'):
                cur.execute("delete from shopping where Cid = %d and ISBN = '%s'"%(self.Cid,list_bookName))
                conn.commit()
        else:
            showwarning('警告','请选择要移除的项目')

    def SearchToDet(self):
        '''
        从搜索结果打开书籍详情页
        :return: 
        '''
        list_box_bookname = self.libox_bookInfo.item(self.libox_bookInfo.focus(), "values")[0]
        for i in self.BookInfo:
            if list_box_bookname == i[1]:
                self.BookInfoISBN = i[0]
                break
        self.Det()

    def event_search(self):
        '''
        完成搜索功能，支持模糊搜索，把搜索结果添加到treeview中
        :return: 
        '''
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

    def event_editUserInfo(self):
        '''
        编辑用户信息，将文本框设置为普通模式
        将按钮文本显示为确认
        '''
        for i in range(7):
            self.entryname[i].configure(state = 'normal')
        self.btnEditUserInfo.configure(text = '确认',command = self.event_confirm)

    def event_confirm(self):
        ''' 
        确认用户修改信息,将模式设置为不可用
        读取文本框的数据，写回数据库，并提示完成修改
        '''
        for i in range(7):
            self.userValues[i] = self.entryname[i].get()
        self.justy_userInfo()
        if self.userInfoFlag:
            for i in range(7):
                self.entryname[i].configure(state='readonly')

            self.btnEditUserInfo.configure(text = '修改信息',command = self.event_editUserInfo)
            comm = "update customer set Cuser='%s',Csex='%s',Creal='%s',Cpost=%d,Cemail='%s',Cnumber='%s',Caddress='%s' where cid = %d"%(
                self.userValues[0],self.userValues[1],self.userValues[2],int(self.userValues[3])
                     ,self.userValues[4],self.userValues[5],self.userValues[6]
                ,self.Cid)
            comm = str(comm.encode('utf-8'))
            cur.execute(comm)
            conn.commit()
            #print comm
            showinfo('提示', '修改成功')

    def justy_userInfo(self):
        '''
        判断用户填写信息是否正确
        :return: 
        '''
        self.userInfoFlag = True
        if not self.userValues[0].isalnum():
            showerror('错误', '账号只能由字母和数字组成')
            self.userInfoFlag = False

        if self.userValues[1] not in [u'男',u'女']:
            showerror('错误', '性别只能为\'男\'或\'女\'')
            self.userInfoFlag = False

        if '' == self.userValues[2]:
            showerror('错误', '姓名不能为空')
            self.userInfoFlag = False

        if not self.userValues[3].isdigit() or len(self.userValues[3]) != 6:
            showerror('错误', '邮编格式错误')
            self.userInfoFlag = False

        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
                , self.userValues[4]) == None:
            showerror('错误', 'Email格式错误')
            self.userInfoFlag = False

        if not self.userValues[5].isdigit() or len(self.userValues[5]) != 11:
            showerror('错误', '手机号格式错误')
            self.userInfoFlag = False

        if '' == self.userValues[6]:
            showerror('错误', '地址不能为空')
            self.userInfoFlag = False



conn = pymssql.connect(host='localhost:1433', user='sa', password='ghostttt'
                           , database='BookStore', charset="utf8")

cur = conn.cursor()
top = tk.Tk()
Application(top)
cur.close()
conn.close()


