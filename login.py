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

        self.b_register = Button(FrameUserRegister, text='确认注册', style='TButton',command = self.event_register)
        self.b_register.place(relx=0.556, rely=0.755, relwidth=0.26, relheight=0.13)

        self.label_RegisterUser = Label(FrameUserRegister, text='账号', style='TLabel')
        self.label_RegisterPswd = Label(FrameUserRegister, text='密码', style='TLabel')
        self.label_RegisterRePswd = Label(FrameUserRegister, text='确认密码', style='TLabel')
        self.label_RegisterUser.place(relx=0.12, rely=0.1, relwidth=0.13, relheight=0.13)
        self.label_RegisterPswd.place(relx=0.12, rely=0.31, relwidth=0.13, relheight=0.13)
        self.label_RegisterRePswd.place(relx=0.08, rely=0.52, relwidth=0.26, relheight=0.13)

        #self.textRegisterUser = tk.StringVar(value='')
        #self.textRegisterPswd = tk.StringVar(value='')
        #self.textReRegisterPswd = tk.StringVar(value='')
        self.entry_RegisterUser = Entry(FrameUserRegister,font=('宋体', 14))#,textvariable=self.textRegisterUser
        self.entry_RegisterPswd = Entry(FrameUserRegister, font=('宋体', 14), show ='*')#, textvariable=self.textRegisterPswd
        self.entry_ReRegisterPswd = Entry(FrameUserRegister, font=('宋体', 14),show = '*')#, textvariable=self.textReRegisterPswd
        self.entry_RegisterUser.place(relx=0.32, rely=0.1, relwidth=0.6, relheight=0.16)
        self.entry_RegisterPswd.place(relx=0.32, rely=0.31, relwidth=0.6, relheight=0.16)
        self.entry_ReRegisterPswd.place(relx=0.32, rely=0.52, relwidth=0.6, relheight=0.16)

    def create_admin(self):
        '''
        管理员登陆界面
        :return: 
        '''
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

    def register_userInfo(self):
        '''
        用户注册信息填写界面
        :return: 
        '''
        self.FrameUserInfo = tk.LabelFrame(login_windows,bg = 'white')
        self.FrameUserInfo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.style.configure('heading.TLabel',font = 4,background = '#E6E6E6',anchor = 'center')

        label_heading = Label(self.FrameUserInfo,text = '请填写信息以完成注册',style = 'heading.TLabel')
        label_heading.place(relx=0.0, rely=0.00, relwidth=1, relheight=0.07)

        Line_s = Separator(self.FrameUserInfo, orient='horizontal', style='Line1.TSeparator')
        Line_s.place(relx=0.0, rely=0.07, relwidth=1, relheight=0.007)

        label_name = Label(self.FrameUserInfo,text = '姓名')
        label_post = Label(self.FrameUserInfo,text = '邮编')
        label_sex = Label(self.FrameUserInfo,text = '性别')
        label_num = Label(self.FrameUserInfo,text = '手机')
        label_email = Label(self.FrameUserInfo,text = '邮箱')
        label_address = Label(self.FrameUserInfo,text = '地址')
        label_name.place(relx=0.1, rely=0.12, relwidth=0.14, relheight=0.09)
        label_post.place(relx=0.1, rely=0.27, relwidth=0.14, relheight=0.09)
        label_sex.place(relx=0.6, rely=0.27, relwidth=0.14, relheight=0.09)
        label_num.place(relx=0.1, rely=0.42, relwidth=0.14, relheight=0.09)
        label_email.place(relx=0.1, rely=0.57, relwidth=0.14, relheight=0.09)
        label_address.place(relx=0.1, rely=0.72, relwidth=0.14, relheight=0.09)

        self.entry_name = Entry(self.FrameUserInfo,font = 1)
        self.entry_post = Entry(self.FrameUserInfo,font = 1)
        self.entry_sex = Entry(self.FrameUserInfo,font = 1)
        self.entry_num = Entry(self.FrameUserInfo,font = 1)
        self.entry_email = Entry(self.FrameUserInfo,font = 1)
        self.entry_address = Entry(self.FrameUserInfo,font = 1)
        self.entry_name.place(relx=0.24, rely=0.12, relwidth=0.36, relheight=0.09)
        self.entry_post.place(relx=0.24, rely=0.27, relwidth=0.36, relheight=0.09)
        self.entry_sex.place(relx=0.74, rely=0.27, relwidth=0.16, relheight=0.09)
        self.entry_num.place(relx=0.24, rely=0.42, relwidth=0.66, relheight=0.09)
        self.entry_email.place(relx=0.24, rely=0.57, relwidth=0.66, relheight=0.09)
        self.entry_address.place(relx=0.24, rely=0.72, relwidth=0.66, relheight=0.09)


        self.b_AdminLogin = Button(self.FrameUserInfo, text='确定', command=self.event_reRegister, style='TButton')
        self.b_AdminLogin.place(relx=0.76, rely=0.85, relwidth=0.14, relheight=0.1)
        self.b_AdminLogin = Button(self.FrameUserInfo, text='取消', command=self.cancel_register, style='TButton')
        self.b_AdminLogin.place(relx=0.5, rely=0.85, relwidth=0.14, relheight=0.1)
        
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

    def event_register(self):
        '''
        用户注册功能。检查用户名，密码格式
        :return: 
        '''
        username = self.entry_RegisterUser.get()
        pswd = self.entry_RegisterPswd.get()
        repswd = self.entry_ReRegisterPswd.get()
        if str(username.encode('utf-8')).isalnum():#检查输入格式
            cur.execute('select Cuser from customer')
            userexsit = cur.fetchall()          #获取数据库中已存在的用户名
            flag = True
            for i in userexsit:
                if username == i[0]:
                    showwarning('Warning','用户名已存在')
                    flag = False
            if flag:#如果用户名不存在，则判断两次密码是否一致
                if str(pswd.encode('utf-8')).isalnum():#检查输入格式
                    if pswd == repswd:
                        self.register_userInfo()
                    else:
                        showwarning('提示','两次输入密码不一致')
                else:
                    showwarning('提示', '密码请使用字母和数字的组合')
        else:
            showwarning('提示','请使用字母和数字的组合')

    def b_login_admin(self):
        #TODO 管理员登录
        pass
        print '管理员登陆'

    def cancel_register(self):
        '''
        用户取消信息填写功能
        :return: 
        '''
        if askyesno('提醒','确定取消注册吗?'):
            self.FrameUserInfo.destroy()
        else:
            pass

    def justy_userInfo(self):
        '''
        判断用户注册填写信息是否正确
        :return: 
        '''
        self.userInfoFlag = True#所有信息都正确的标志

        if len(self.entry_name.get())<2:
            showerror('错误', '姓名格式错误')
            self.userInfoFlag = False

        if not self.entry_post.get().isdigit() or len(self.entry_post.get()) != 6:
            showerror('错误', '邮编格式错误')
            self.userInfoFlag = False

        if self.entry_sex.get() not in [u'男',u'女']:
            showerror('错误', '性别只能为\'男\'或\'女\'')
            self.userInfoFlag = False


        reg = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
        if re.match(reg, self.entry_email.get()) == None:
            showerror('错误', 'Email格式错误')
            self.userInfoFlag = False

        if not self.entry_num.get().isdigit() or len(self.entry_num.get()) != 11:
            showerror('错误', '手机号格式错误')
            self.userInfoFlag = False

        if '' == self.entry_address.get():
            showerror('错误', '地址不能为空')
            self.userInfoFlag = False

    def event_reRegister(self):
        '''
        注册，把用户注册信息写入数据库
        :return: 
        '''
        self.justy_userInfo()
        if self.userInfoFlag:
            s =  (self.entry_RegisterUser.get(),self.entry_RegisterPswd.get()
                    ,str(self.entry_name.get().encode('utf-8')),str(self.entry_sex.get().encode('utf-8'))
                   ,self.entry_num.get(),self.entry_email.get(),str(self.entry_address.get().encode('utf-8'))
                   ,int(self.entry_post.get()))
            comm = "insert into customer values ('%s','%s','%s','%s','%s','%s','%s',%d)"%(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7])
            cur.execute(comm)
            conn.commit()
            showinfo('提示','注册成功')
            self.FrameUserInfo.destroy()

if __name__ == '__main__':
    login_windows = tk.Tk()
    Application(login_windows)


