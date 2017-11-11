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

Pic = []
Lab = []
Im = []
TLab = []
relx = [0.05, 0.2, 0.35, 0.5, 0.65, 0.8]
rely = [0.06, 0.54, 0.4, 0.88]
for i in range(12):
    Pic.append('Picture'+str(i))
    Lab.append('l_name'+str(i))
    Im.append('im'+str(i))
    TLab.append(Lab[i] + '.TLabel')
#所有控件和控件绑定变量引用字典，使用这个字典是为了方便在其他函数中引用所有控件。

book = 0
page = 0
maxpage = len(BookInfo)/12
if maxpage < len(BookInfo) / 12.0:
    num = len(BookInfo) % 12
print maxpage
def main():
    top = tk.Tk()
    top.title('主界面')
    top.resizable(0,0)
    top.geometry('1100x705+260+60')#964,136

    style = Style()

    Picture = tk.Canvas(top)
    image4 = Image.open(r"back.thumbnail")
    im4 = ImageTk.PhotoImage(image4)
    Picture.create_image(0, 0,anchor = 'nw', image=im4)
    Picture.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.22)

    style.configure('TLabelframe',foreground='#000000', background='#FFFFFF', font=(u'宋体',14))
    Frame1 = LabelFrame(top, text='书籍', style='TLabelframe')
    Frame1.place(relx=0.005, rely=0.216, relwidth=0.989, relheight=0.775)

    def pro():
        global page
        if page > 0:
            page -= 1
        print page
        pag()
    def nex():
        global page
        global maxpage
        if page < maxpage-1:
            page += 1
        print page
        pag()

    b_pro = tk.Button(Frame1,text = '<',relief = 'groove',command = pro)
    b_pro.place(relx=0.95, rely=0.35, relwidth=0.05, relheight=0.1)

    b_next = tk.Button(Frame1,text = '>',relief = 'groove',command = nex)
    b_next.place(relx=0.95, rely=0.45, relwidth=0.05, relheight=0.1)

    def pag():
        global num
        for i in range(12):

            style.configure(TLab[i],anchor='center',font=(u'幼圆', 12)
                            , relief='flat'
                            ,background = '#fff', foreground='black'
                            ,wraplength = 100,justify = 'center')

            Pic[i] = tk.Canvas(Frame1)
            path = r"thu\%s.thumbnail"%BookInfo[12*page + i][0]
            Im[i] = ImageTk.PhotoImage(Image.open(path))
            Pic[i].create_image(0,0,anchor = 'nw'
                                  , image=Im[i])
            if i < 6:
                Pic[i].place(relx=relx[i], rely=0.06, relwidth=0.107, relheight=0.315)
            else:
                Pic[i].place(relx=relx[i-6], rely=0.54, relwidth=0.107, relheight=0.315)

            Lab[i] = Label(Frame1, text=BookInfo[12 * page + i][1],style = TLab[i],anchor = 'n')
            if i < 6 :
                Lab[i].place(relx=relx[i], rely=0.4, relwidth=0.107, relheight=0.12)
            else:
                Lab[i].place(relx=relx[i-6], rely=0.88, relwidth=0.107, relheight=0.12)


            def do(event):
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
        global path
        style.configure('TLabelframe', foreground='#000000', background='#FFFFFF', font=(u'宋体', 14))
        Frame2 = LabelFrame(top, text='详情', style='TLabelframe')
        Frame2.place(relx=0.005, rely=0.216, relwidth=0.989, relheight=0.775)

        style.configure(TLab[i], anchor='center', font=(u'幼圆', 12)
                        , relief='flat'
                        , background='#fff', foreground='black'
                        , wraplength=100, justify='center')

        P_det = tk.Canvas(Frame2)
        print page,book
        path = r"thu\%s.thumbnail" % BookInfo[12*page+book][0]
        im_det = ImageTk.PhotoImage(Image.open(path))
        P_det.create_image(0, 0, anchor='nw'
                            , image=im_det)
        P_det.place(relx=0.05, rely=0.06, relwidth=0.107, relheight=0.315)

        label_det = Label(Frame2, text=BookInfo[12*page+book][1], style=TLab[i], anchor='n')
        label_det.place(relx=0.05, rely=0.4, relwidth=0.107, relheight=0.12)

        def back():
            Frame2.destroy()
            pag()

        button_det = tk.Button(Frame2,text = '返回',relief = 'groove',command = back)
        button_det.place(relx=0.45, rely=0.84, relwidth=0.107, relheight=0.12)

    pag()

    top.mainloop()
    try: top.destroy()
    except: pass



if __name__ == "__main__":
    main()
