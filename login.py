#-*- coding:utf-8 -*-

from HeadFile import *

class Login_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('欢迎')
        self.master.geometry('400x350+500+150')
        self.master.resizable(0,0)
        self.create_Background()


        self.style = Style()
        self.style.configure('TButton',font=('幼圆',14,'bold'),relief = 'groove')
        self.style.configure('TLabel',anchor='w', font=('幼圆',14,'bold'),background = 'white')
        self.style.configure('TLabelframe',background='white', font=(u'宋体', 14))

        self.create_Main()
        self.create_login()
        self.master.mainloop()

    def create_Main(self):
        '''
        程序主界面
        :param top: 
        :return: 
        '''
        #五个图标
        self.ico_book = ImageTk.PhotoImage(Image.open(r'ico\book.png'))
        self.ico_user = ImageTk.PhotoImage(Image.open(r'ico\user.png'))
        self.ico_search = ImageTk.PhotoImage(Image.open(r'ico\search.png'))
        self.ico_shopping = ImageTk.PhotoImage(Image.open(r'ico\shopping.png'))
        self.ico_order = ImageTk.PhotoImage(Image.open(r'ico\order.png'))

        self.FrameMenu = tk.LabelFrame(login_windows,text = '',background = 'white')
        self.FrameMenu.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.62)

        self.b_register = tk.Button(login_windows, text='登陆', command=self.create_login
                                    , font=('幼圆', 14, 'bold'), relief='groove', fg='blue')
        self.b_register.place(relx=0.02, rely=0.26, relwidth=0.15, relheight=0.09)

        self.b_register = tk.Button(login_windows, text='注册', command=self.create_register
                                    , font=('幼圆', 14, 'bold'), relief='groove', fg='blue')
        self.b_register.place(relx=0.17, rely=0.26, relwidth=0.15, relheight=0.09)

        self.b_admin = tk.Button(login_windows, text='管理员', command=self.create_admin
                                 , font=('幼圆', 14, 'bold'), relief='groove', fg='blue')
        self.b_admin.place(relx=0.78, rely=0.26, relwidth=0.2, relheight=0.09)

    def create_Background(self):
        self.image = Image.open("back.thumbnail")
        self.im = ImageTk.PhotoImage(self.image)
        self.picture = tk.Canvas(self.master,bg = 'gray')
        self.picture.create_image(0,0,anchor = 'nw', image=self.im)
        self.picture.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.30)

    def create_login(self):
        
        FrameUserLogin = Frame(login_windows,style='TLabelframe')
        FrameUserLogin.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.62)

        self.b_login = Button(FrameUserLogin, text='登陆', command=self.b_login_cmd, style='TButton')
        self.b_login.place(relx=0.65, rely=0.755, relwidth=0.16, relheight=0.13)

        self.Label1 = Label(FrameUserLogin, text='账号', style='TLabel')
        self.Label2 = Label(FrameUserLogin, text='密码', style='TLabel')
        self.Label1.place(relx=0.12, rely=0.27, relwidth=0.13, relheight=0.13)
        self.Label2.place(relx=0.12, rely=0.5, relwidth=0.13, relheight=0.13)
        
        self.textLoginUser = tk.StringVar(value='Amy')
        self.textLoginPswd = tk.StringVar(value='123')
        self.entry_LoginUser = Entry(FrameUserLogin, textvariable=self.textLoginUser, font=('宋体', 14))
        self.entry_LoginPswd = Entry(FrameUserLogin, textvariable=self.textLoginPswd, font=('宋体',14),show = '*')
        self.entry_LoginPswd.place(relx=0.32, rely=0.5, relwidth=0.6, relheight=0.16)
        self.entry_LoginUser.place(relx=0.32, rely=0.27, relwidth=0.6, relheight=0.16)

    def create_register(self):
        FrameUserRegister = Frame(login_windows, style='TLabelframe')
        FrameUserRegister.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.62)

        self.b_register = Button(FrameUserRegister, text='确认注册', style='TButton')
        self.b_register.place(relx=0.556, rely=0.755, relwidth=0.26, relheight=0.13)

        self.label_RegisterUser = Label(FrameUserRegister, text='账号', style='TLabel')
        self.label_RegisterPswd = Label(FrameUserRegister, text='密码', style='TLabel')
        self.label_RegisterRePswd = Label(FrameUserRegister, text='确认密码', style='TLabel')
        self.label_RegisterUser.place(relx=0.12, rely=0.08, relwidth=0.13, relheight=0.13)
        self.label_RegisterPswd.place(relx=0.12, rely=0.27, relwidth=0.13, relheight=0.13)
        self.label_RegisterRePswd.place(relx=0.08, rely=0.5, relwidth=0.26, relheight=0.13)

        #self.textRegisterUser = tk.StringVar(value='')
        #self.textRegisterPswd = tk.StringVar(value='')
        #self.textReRegisterPswd = tk.StringVar(value='')
        self.entry_RegisterUser = Entry(FrameUserRegister,font=('宋体', 14))#,textvariable=self.textRegisterUser
        self.entry_RegisterPswd = Entry(FrameUserRegister, font=('宋体', 14), show ='*')#, textvariable=self.textRegisterPswd
        self.entry_ReRegisterPswd = Entry(FrameUserRegister, font=('宋体', 14),show = '*')#, textvariable=self.textReRegisterPswd
        self.entry_RegisterUser.place(relx=0.32, rely=0.08, relwidth=0.6, relheight=0.16)
        self.entry_RegisterPswd.place(relx=0.32, rely=0.27, relwidth=0.6, relheight=0.16)
        self.entry_ReRegisterPswd.place(relx=0.32, rely=0.5, relwidth=0.6, relheight=0.16)

    def create_admin(self):
        
        FrameAdminLogin = Frame(login_windows,style='TLabelframe')
        FrameAdminLogin.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.62)

        self.b_AdminLogin = Button(FrameAdminLogin, text='登陆', command=self.b_login_admin, style='TButton')
        self.b_AdminLogin.place(relx=0.65, rely=0.755, relwidth=0.16, relheight=0.13)

        self.label_AdminUser = Label(FrameAdminLogin, text='Admin', style='TLabel')
        self.label_AdminPswd = Label(FrameAdminLogin, text='Pswd', style='TLabel')
        self.label_AdminUser.place(relx=0.12, rely=0.27, relwidth=0.18, relheight=0.13)
        self.label_AdminPswd.place(relx=0.12, rely=0.5, relwidth=0.13, relheight=0.13)

        self.textAdminUser = tk.StringVar(value='')
        self.textAdminPswd = tk.StringVar(value='')
        self.entry_AdminUser = Entry(FrameAdminLogin, textvariable=self.textAdminUser, font=('宋体', 14))
        self.entry_AdminPswd = Entry(FrameAdminLogin, textvariable=self.textAdminPswd, font=('宋体',14),show = '*')
        self.entry_AdminUser.place(relx=0.32, rely=0.27, relwidth=0.6, relheight=0.16)
        self.entry_AdminPswd.place(relx=0.32, rely=0.5, relwidth=0.6, relheight=0.16)

class Application(Login_ui):
    def __init__(self, master=None):
        Login_ui.__init__(self, master)

    def b_login_cmd(self):
        comm = "select Cuser,Cpswd,Cid from customer"
        cur.execute(comm)
        user = cur.fetchall()

        username = self.entry_LoginUser.get()
        pswd = self.entry_LoginPswd.get()
        Flag = True
        for i in user:
            if username == i[0] and pswd == i[1]:
                Flag = False
                try:
                    login_windows.destroy()
                except:
                    askretrycancel('糟糕','要重试吗?')
                setCid(i[2])
                import User
        if Flag:
            showerror('错误', '账户名或密码错误')

    def b_login_admin(self):
        #TODO 管理员登录
        pass

if __name__ == '__main__':
    login_windows = tk.Tk()
    Application(login_windows)


