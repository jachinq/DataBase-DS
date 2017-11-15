# -*- coding: utf-8 -*-
'''
This is a scrpit for ...
Author: Jachin
Data: 2017- 11- 
'''

import pymssql
conn = pymssql.connect(host='localhost:1433'
                       ,user='sa'
                       ,password='ghostttt'
                       ,database='BookStore'
                       ,charset="utf8")
cur = conn.cursor()
cur.execute('select ISBN,Bname from book')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
BookInfo = cur.fetchall()
cur.close()
conn.close()

import tkinter as tk
from tkinter.ttk import *
from PIL import Image,ImageTk

Pic = ['Picture'+str(i) for i in range(12)]
Lab = ['l_name'+str(i) for i in range(12)]
Im = ['im'+str(i) for i in range(12)]
TLab = [Lab[i] + '.TLabel' for i in range(12)]
setBlue = ['setBlue' + str(i) for i in range(12)]
setBlack = ['setBlack' + str(i) for i in range(12)]
relx = [0.05, 0.2, 0.35, 0.5, 0.65, 0.8]
rely = [0.06, 0.54, 0.4, 0.88]

#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。

book = 0
page = 0
maxpage = len(BookInfo)/12
if maxpage < len(BookInfo) / 12.0:num = len(BookInfo) % 12
def main():
    top = tk.Tk()
    top.title('主界面')
    top.resizable(0,0)
    top.geometry('1100x705+260+60')#964,136

    style = Style()
    style.configure('TLabelframe',foreground='#000000', background='#FFFFFF', font=(u'宋体',14))

    #主界面背景图
    Picture = tk.Canvas(top)
    #im4 = ImageTk.PhotoImage(Image.open(r"main.thumbnail"))
    #Picture.create_image(0, 0,anchor = 'nw', image=im4)
    Picture.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.22)
    #1078 155.1

    #翻页的图标
    bp = ImageTk.PhotoImage(Image.open(r'ico\pro.png'))
    bn = ImageTk.PhotoImage(Image.open(r'ico\next.png'))

    #概览页和详情页的框架
    Frame1 = LabelFrame(top, text='', style='TLabelframe')
    Frame2 = LabelFrame(top, text='', style='TLabelframe')
    Frame3 = LabelFrame(Frame2, text='', style='TLabelframe')


    #详情页的图标
    P_det = tk.Canvas(Frame3,bg = '#FFFFFF')
    im_det = ImageTk.PhotoImage(Image.open(r'ico\det2.png'))
    P_det.create_image(10,15, anchor='nw', image=im_det)
    P_det.place(relx=0.05, rely=-0.0, relwidth=0.16, relheight=0.18)

    def pag():
        global num
        Frame1.place(relx=0.005, rely=0.216, relwidth=0.989, relheight=0.775)
        #1087.9 546.375

        def pro():
            global page
            if page > 0:
                page -= 1
                # print page
                pag()

        def nex():
            global page
            global maxpage
            if page < maxpage:
                page += 1
                pag()



        b_pro = tk.Button(Frame1, relief='groove', command=pro,image = bp)
        b_pro.place(relx=0.95, rely=0.35, relwidth=0.05, relheight=0.1)
        #54.395 54.6375

        b_next = tk.Button(Frame1, relief='groove', command=nex,image = bn)
        b_next.place(relx=0.95, rely=0.45, relwidth=0.05, relheight=0.1)

        j = -1
        for i in range(12):
            if j < num:
                j += 1
            style.configure(TLab[i],anchor='center',font=(u'幼圆', 12)
                                , relief='flat'
                                ,background = '#FFFFFF'
                                ,wraplength = 100,justify = 'center')

            Pic[i] = tk.Canvas(Frame1,bg = '#FFFFFF')
            if page < maxpage:
                path = r"thu\%s.thumbnail"%BookInfo[12*page + i][0]
                Lab[i] = Label(Frame1, text=BookInfo[12 * page + i][1], style=TLab[i], anchor='n')
            elif page == maxpage and j < num:
                path = r"thu\%s.thumbnail" % BookInfo[12 * page + j][0]
                Lab[i] = Label(Frame1, text=BookInfo[12 * page + i][1], style=TLab[i], anchor='n')

            elif page == maxpage and j >= num:
                path = r"ico\none.png"
                Lab[i] = Label(Frame1, text='', style=TLab[i], anchor='n')


            Im[i] = ImageTk.PhotoImage(Image.open(path))
            Pic[i].create_image(0,0,anchor = 'nw', image=Im[i])

            if i < 6:
                Pic[i].place(relx=relx[i], rely=0.06, relwidth=0.107, relheight=0.315)
            else:
                Pic[i].place(relx=relx[i-6], rely=0.54, relwidth=0.107, relheight=0.315)


            if i < 6 :
                Lab[i].place(relx=relx[i], rely=0.4, relwidth=0.107, relheight=0.12)
            else:
                Lab[i].place(relx=relx[i-6], rely=0.88, relwidth=0.107, relheight=0.12)


            def do(event):
                Frame1.place_forget()
                det()

            Lab[i].bind('<Button-1>',do)

        def event():
            def setBlue0(event):
                    global book
                    style.configure(TLab[0], foreground='blue')
                    book = 0

            def setBlack0(event):
                style.configure(TLab[0], foreground='black')

            Lab[0].bind('<Enter>', setBlue0)
            Lab[0].bind('<Leave>', setBlack0)

            def setBlue1(event):
                global book
                style.configure(TLab[1], foreground='blue')
                book = 1

            def setBlack1(event):
                style.configure(TLab[1], foreground='black')

            Lab[1].bind('<Enter>', setBlue1)
            Lab[1].bind('<Leave>', setBlack1)

            def setBlue2(event):
                global book
                style.configure(TLab[2], foreground='blue')
                book = 2

            def setBlack2(event):
                style.configure(TLab[2], foreground='black')

            Lab[2].bind('<Enter>', setBlue2)
            Lab[2].bind('<Leave>', setBlack2)

            def setBlue3(event):
                global book
                style.configure(TLab[3], foreground='blue')
                book = 3

            def setBlack3(event):
                style.configure(TLab[3], foreground='black')

            Lab[3].bind('<Enter>', setBlue3)
            Lab[3].bind('<Leave>', setBlack3)

            def setBlue4(event):
                global book
                style.configure(TLab[4], foreground='blue')
                book = 4

            def setBlack4(event):
                style.configure(TLab[4], foreground='black')

            Lab[4].bind('<Enter>', setBlue4)
            Lab[4].bind('<Leave>', setBlack4)

            def setBlue5(event):
                global book
                style.configure(TLab[5], foreground='blue')
                book = 5

            def setBlack5(event):
                style.configure(TLab[5], foreground='black')
            Lab[5].bind('<Enter>', setBlue5)
            Lab[5].bind('<Leave>', setBlack5)

            def setBlue6(event):
                global book
                style.configure(TLab[6], foreground='blue')
                book = 6

            def setBlack6(event):
                style.configure(TLab[6], foreground='black')

            Lab[6].bind('<Enter>', setBlue6)
            Lab[6].bind('<Leave>', setBlack6)

            def setBlue7(event):
                style.configure(TLab[7], foreground='blue')

            def setBlack7(event):
                style.configure(TLab[7], foreground='black')

            Lab[7].bind('<Enter>', setBlue7)
            Lab[7].bind('<Leave>', setBlack7)

            def setBlue8(event):
                global book
                style.configure(TLab[8], foreground='blue')
                book = 8

            def setBlack8(event):
                style.configure(TLab[8], foreground='black')

            Lab[8].bind('<Enter>', setBlue8)
            Lab[8].bind('<Leave>', setBlack8)

            def setBlue9(event):
                global book
                style.configure(TLab[9], foreground='blue')
                book = 9

            def setBlack9(event):
                style.configure(TLab[9], foreground='black')

            Lab[9].bind('<Enter>', setBlue9)
            Lab[9].bind('<Leave>', setBlack9)

            def setBlue10(event):
                global book
                style.configure(TLab[10], foreground='blue')
                book = 10

            def setBlack10(event):
                style.configure(TLab[10], foreground='black')

            Lab[10].bind('<Enter>', setBlue10)
            Lab[10].bind('<Leave>', setBlack10)

            def setBlue11(event):
                global book
                style.configure(TLab[11], foreground='blue')
                book = 11

            def setBlack11(event):
                style.configure(TLab[11], foreground='black')

            Lab[11].bind('<Enter>', setBlue11)
            Lab[11].bind('<Leave>', setBlack11)
        event()

    def det():
        style.configure('TLabel', anchor='w', font=(u'幼圆', 14),background = 'white')
        style.configure('TButton', font=(u'幼圆', 14),relief = 'groove')
        Frame2.place(relx=0.005, rely=0.005, relwidth=0.989, relheight=0.98)
        Frame3.place(relx=0.25, rely=-0.008, relwidth=0.5, relheight=1)

        def back():
            Frame2.place_forget()
            Frame3.place_forget()
            pag()
            #Frame1.place(relx=0.005, rely=0.216, relwidth=0.989, relheight=0.775)

        def addToShopping():
            #TODO 确认加入购物车，消息框
            pass

        #下面开始定义控件
        label_det = Label(Frame3, text=BookInfo[12*page+book][1], style=TLab[i], anchor='n')

        Command2 = Button(Frame3, text='返回', command=back, style='TButton')
        Command2.place(relx=0.761, rely=0.883, relwidth=0.108, relheight=0.067)

        Command1 = Button(Frame3, text='加入购物车', command=addToShopping, style='TButton')
        Command1.place(relx=0.513, rely=0.883, relwidth=0.21, relheight=0.067)

        Text7 = tk.Text(Frame3,  font=(u'宋体', 14), relief='solid')
        Text7.place(relx=0.265, rely=0.867, relwidth=0.179, relheight=0.084)

        Text6 = tk.Text(Frame3,  font=(u'宋体', 14), relief='solid')
        Text6.place(relx=0.23, rely=0.425, relwidth=0.639, relheight=0.395)

        Text5 = tk.Text(Frame3,  font=(u'宋体', 14), relief='solid')
        Text5.place(relx=0.637, rely=0.311, relwidth=0.232, relheight=0.051)

        Text4 = tk.Text(Frame3,  font=(u'宋体', 14), relief='solid')
        Text4.place(relx=0.23, rely=0.327, relwidth=0.144, relheight=0.051)

        Text3 = tk.Text(Frame3, font=(u'宋体', 14), relief='solid')
        Text3.place(relx=0.637, rely=0.213, relwidth=0.232, relheight=0.051)

        Text2 = tk.Text(Frame3,state='disabled',  font=(u'宋体', 14), relief='solid')
        Text2.place(relx=0.23, rely=0.229, relwidth=0.144, relheight=0.051)

        Text1 = tk.Text(Frame3,  state='disabled', font=(u'宋体', 14), relief='solid')
        Text1.place(relx=0.44, rely=0.082, relwidth=0.43, relheight=0.067)

        style.configure('TSeparator', background='#000000')
        Line1 = Separator(Frame3, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.196, relwidth=1.009, relheight=0.002)

        
        Label7 = Label(Frame3, text='库存', style='Label7.TLabel')
        Label7.place(relx=0.071, rely=0.883, relwidth=0.144, relheight=0.051)

        Label6 = Label(Frame3, text='简介', style='Label6.TLabel')
        Label6.place(relx=0.071, rely=0.442, relwidth=0.108, relheight=0.051)

        Label5 = Label(Frame3, text='ISBN', style='Label5.TLabel')
        Label5.place(relx=0.513, rely=0.327, relwidth=0.073, relheight=0.051)

        Label4 = Label(Frame3, text='出版社', style='Label4.TLabel')
        Label4.place(relx=0.071, rely=0.344, relwidth=0.108, relheight=0.035)

        Label3 = Label(Frame3, text='定价', style='Label3.TLabel')
        Label3.place(relx=0.513, rely=0.213, relwidth=0.073, relheight=0.051)

        Label2 = Label(Frame3, text='作者', style='Label2.TLabel')
        Label2.place(relx=0.088, rely=0.245, relwidth=0.091, relheight=0.035)

        Label1 = Label(Frame3, text='书名', style='Label1.TLabel')
        Label1.place(relx=0.319, rely=0.082, relwidth=0.1, relheight=0.067)

    pag()

    top.mainloop()
    try: top.destroy()
    except: pass



if __name__ == "__main__":
    main()
