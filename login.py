#-*- coding:utf-8 -*-

from HeadFile import *

d = {}
class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.image = Image.open("back.thumbnail")
        self.im = ImageTk.PhotoImage(self.image)
        self.master.title('欢迎')
        self.master.geometry('400x350+500+150')
        self.master.resizable(0,0)
        self.create_Background()
        self.create_login()

        self.master.mainloop()

    def create_Background(self):
        self.picture = tk.Canvas(self.master,bg = 'gray')
        self.picture.create_image(0,0,anchor = 'nw', image=self.im)
        self.picture.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.30)

    def create_login(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        self.style.configure('TButton',font=('幼圆',14,'bold'),relief = 'groove')
        self.style.configure('TLabel',anchor='w', font=('幼圆',14,'bold'))

        self.style.configure('Frame1.TLabelframe', foreground='#000000', background='white', font=(u'宋体', 14))
        Frame1 = LabelFrame(top,text = '',style='Frame1.TLabelframe')
        Frame1.place(relx=0.02, rely=0.316, relwidth=0.96, relheight=0.65)

        self.b_login = Button(Frame1, text='登陆', command=self.b_login_cmd, style='TButton')
        self.b_login.place(relx=0.656, rely=0.755, relwidth=0.16, relheight=0.15)

        self.Label1 = Label(Frame1, text='账号', style='TLabel')
        self.Label1.place(relx=0.15, rely=0.25, relwidth=0.13, relheight=0.15)

        self.Text1Var = tk.StringVar(value='')
        self.Text1 = Entry(Frame1, textvariable=self.Text1Var, font=('宋体',14))
        self.Text1.place(relx=0.356, rely=0.25, relwidth=0.6, relheight=0.2)

        self.Text2Var = tk.StringVar(value='')
        self.Text2 = Entry(Frame1, textvariable=self.Text2Var, font=('宋体',14),show = '*')
        self.Text2.place(relx=0.356, rely=0.5, relwidth=0.6, relheight=0.2)

        self.Label2 = Label(Frame1, text='密码', style='TLabel')
        self.Label2.place(relx=0.15, rely=0.5, relwidth=0.13, relheight=0.15)

        self.b_register = tk.Button(self.top, text='登陆', command=self.create_login
                                    ,font=('幼圆', 14, 'bold'), relief='groove',fg = 'blue')
        self.b_register.place(relx=0.02, rely=0.255, relwidth=0.15, relheight=0.09)

        self.b_register = tk.Button(self.top, text='注册', command=self.create_register
                                    , font=('幼圆', 14, 'bold'), relief='groove',fg = 'blue')
        self.b_register.place(relx=0.17, rely=0.255, relwidth=0.15, relheight=0.09)


    def create_register(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        self.style.configure('TButton', font=('幼圆', 14, 'bold'), relief='groove')
        self.style.configure('TLabel', anchor='w', font=('幼圆', 14, 'bold'))

        self.style.configure('Frame1.TLabelframe', foreground='#000000', background='white', font=(u'宋体', 14))
        Frame1 = LabelFrame(top, text='', style='Frame1.TLabelframe')
        Frame1.place(relx=0.02, rely=0.316, relwidth=0.96, relheight=0.65)

        self.b_login = Button(Frame1, text='确认注册', style='TButton')
        self.b_login.place(relx=0.556, rely=0.755, relwidth=0.32, relheight=0.15)

        self.Label1 = Label(Frame1, text='账号', style='TLabel')
        self.Label1.place(relx=0.15, rely=0.01, relwidth=0.13, relheight=0.15)

        self.Text1Var = tk.StringVar(value='')
        self.Text1 = Entry(Frame1, textvariable=self.Text1Var, font=('宋体', 14))
        self.Text1.place(relx=0.356, rely=0.01, relwidth=0.6, relheight=0.2)

        self.Label2 = Label(Frame1, text='密码', style='TLabel')
        self.Label2.place(relx=0.15, rely=0.25, relwidth=0.13, relheight=0.15)

        self.Text1Var = tk.StringVar(value='')
        self.Text2 = Entry(Frame1, textvariable=self.Text1Var, font=('宋体', 14),show = '*')
        self.Text2.place(relx=0.356, rely=0.25, relwidth=0.6, relheight=0.2)

        self.Label3 = Label(Frame1, text='确认密码', style='TLabel')
        self.Label3.place(relx=0.1, rely=0.5, relwidth=0.26, relheight=0.15)

        self.Text2Var = tk.StringVar(value='')
        self.Text3 = Entry(Frame1, textvariable=self.Text2Var, font=('宋体', 14),show = '*')
        self.Text3.place(relx=0.356, rely=0.5, relwidth=0.6, relheight=0.2)


        self.b_register = tk.Button(self.top, text='登陆', command=self.create_login
                                    ,font=('幼圆', 14, 'bold'), relief='groove',fg = 'blue')
        self.b_register.place(relx=0.02, rely=0.255, relwidth=0.15, relheight=0.09)

        self.b_register = tk.Button(self.top, text='注册', command=self.create_register
                                    , font=('幼圆', 14, 'bold'), relief='groove',fg = 'blue')
        self.b_register.place(relx=0.17, rely=0.255, relwidth=0.15, relheight=0.09)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def b_login_cmd(self):
        d['username'] = self.Text1.get()
        d['psw'] = self.Text2.get()
        if d['username'] == 'sa' and d['psw'] == 'ghost':
            try:
                top.destroy()
            except:
                pass
            import User
        else:
            tkinter.messagebox.showerror('错误', '账户名或密码错误')


top = tk.Tk()
Application(top)


##########################################
##########################################
