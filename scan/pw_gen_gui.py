from tkinter import *
import tkinter.messagebox as messagebox
from pw_gen import User

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def password_generate(self):

        User_dict = {'first_name':self.first_name_i.get(), 'last_name':self.last_name_i.get(),      
                     'abb_name':self.abb_name_i.get(), 'year':self.year_i.get(), 'mouth':self.mouth_i.get(), 
                     'day':self.day_i.get(), 'phone':self.phone_i.get(), 'email':self.e_mail_i.get(),
                     'qq':self.qq_i.get(), 'old_account':self.old_account_i.get()}                                  
       
        user = User(User_dict)

        self.password_list = user.password_generate()


        self.infolabel['text'] = '生成密码数量: 0' + str(len(self.password_list))

        with open('password.txt', 'w+') as f:
            for i in self.password_list:
                f.write(i + '\n')

        messagebox.showinfo('生成成功', '生成成功 - 文件保存为 password.txt')

    def createWidgets(self):
        self.helloLabel = Label(self, text='A&D-社工密码生成器',
                                font=('Fira', 15), width=20, height=1)
        self.helloLabel.grid(row=1, column=2, padx=1, pady=1)

        self.introduction = Label(self, text='一款简单的社会工程学密码生成器,后续慢慢改进',
                                  font=('Arial', 10),height=2)
        self.introduction.grid(row=2, column=2)

        self.first_name = Label(self, text='名字(英文)')
        self.first_name.grid(row=3,column=1)
        self.first_name_i = Entry(self, text='')
        self.first_name_i.grid(row=3, column=2,padx=1, pady=1)
        
        self.last_name = Label(self, text='姓(英文)')
        self.last_name.grid(row=4, column=1)
        self.last_name_i = Entry(self, text='')
        self.last_name_i.grid(row=4, column=2)
        
        self.abb_name = Label(self, text='名字缩写(英文)')
        self.abb_name.grid(row=5, column=1)
        self.abb_name_i = Entry(self, text='')
        self.abb_name_i.grid(row=5, column=2)
        
        self.year = Label(self, text='出生年份(eg 2001)')
        self.year.grid(row=6, column=1)
        self.year_i = Entry(self, text='')
        self.year_i.grid(row=6, column=2)
        
        self.mouth = Label(self, text='月份(eg 01)')
        self.mouth.grid(row=7, column=1)
        self.mouth_i = Entry(self, text='')
        self.mouth_i.grid(row=7, column=2)
        
        self.day = Label(self, text='日期(eg 01)')
        self.day.grid(row=8, column=1)
        self.day_i = Entry(self, text='')
        self.day_i.grid(row=8, column=2)
        
        self.qq = Label(self, text='qq号码')
        self.qq.grid(row=9, column=1)
        self.qq_i = Entry(self, text='')
        self.qq_i.grid(row=9, column=2)
        
        self.e_mail = Label(self, text='邮箱(去掉@和其后面)')
        self.e_mail.grid(row=10, column=1)
        self.e_mail_i = Entry(self, text='')
        self.e_mail_i.grid(row=10, column=2)
        
        self.phone = Label(self, text='电话号码')
        self.phone.grid(row=11, column=1)
        self.phone_i = Entry(self, text='')
        self.phone_i.grid(row=11, column=2)
        
        self.old_account = Label(self, text='旧密码')
        self.old_account.grid(row=12, column=1)
        self.old_account_i = Entry(self, text='')
        self.old_account_i.grid(row=12, column=2)
         

        self.filecount = '生成密码数量: 0'
        self.infolabel = Label(self, text=self.filecount,
                               font=('Arial', 10), width=15, height=1)
        self.infolabel.grid(row=13, column=1)

        self.showText = Button(self, text='开始生成', command=self.password_generate)
        self.showText.grid(row=13, column=2)



if __name__ == '__main__':
    app = Application()
    app.master.title('A&D-密码生成器')
    app.master.geometry('450x350')
    app.mainloop()