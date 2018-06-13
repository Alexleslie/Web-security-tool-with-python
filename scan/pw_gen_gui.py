from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import scrolledtext
import time
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
       
        self.content.delete(1.0, END)

        for i in self.password_list :
            i = i + '\n'
            time.sleep(0.1)
            self.content.insert(END, i)
            self.content.update()
        
        self.infolabel['text'] = self.filecount

        messagebox.showinfo('生成成功', '生成结束')

    def createWidgets(self):
        self.helloLabel = Label(self, text='A&D-社工密码生成器',
                                font=('Fira', 15), width=20, height=1)
        self.helloLabel.grid(row=1, column=2, padx=1, pady=1)

        self.introduction = Label(self, text='一款简单的社会工程学密码生成器,后续慢慢改进',
                                  font=('Arial', 10),height=2)
        self.introduction.grid(row=2, column=2)

        self.first_name = Label(self, text='名字')
        self.first_name.grid(row=3,column=1)
        self.first_name_i = Text(self, text='')
        self.first_name_i.grid(row=3, column=2)
        
        self.last_name = Label(self, text='姓')
        self.last_name.grid(row=4, column=1)
        self.last_name_i = Text(self, text='')
        self.last_name_i.grid(row=4, column=2)
        
        self.abb_name = Label(self, text='缩写')
        self.abb_name.grid(row=5, column=1)
        self.abb_name_i= Text(self, text='')
        self.abb_name_i.grid(row=5, column=2)
        
        self.year = Label(self, text='year')
        self.year.grid(row=6, column=1)
        self.year_i = Text(self, text='')
        self.year_i.grid(row=6, column=2)
        
        self.mouth = Label(self, text='mouth')
        self.mouth.grid(row=6, column=1)
        self.mouth_i = Text(self, text='')
        self.mouth_i.grid(row=6, column=2)
        
        self.day = Label(self, text='day')
        self.day.grid(row=7, column=1)
        self.day_i = Text(self, text='')
        self.day_i.grid(row=7, column=2)
        
        self.qq = Label(self, text='qq')
        self.qq.grid(row=7, column=1)
        self.qq = Text(self, text='')
        self.qq_i.grid(row=7, column=2)
        
        self.e_mail = Label(self, text='e-mail')
        self.e_mail.grid(row=8, column=1)
        self.e_mail_i = Label(self, text='')
        self.e_mail_i.grid(row=8, column=2)
        
        self.phone = Label(self, text='phone')
        self.phone.grid(row=9, column=1)
        self.phone_i = Label(self, text='')
        self.phone_i.grid(row=9, column=2)
        
        self.old_account = Label(self, text='old_account')
        self.old_account.grid(row=10, column=1)
        self.old_account_i = Label(self, text='')
        self.old_account_i.grid(row=10, column=2)
         
        
        
        self.filecount = '生成密码数量: 0'
        self.infolabel = Label(self, text=self.filecount,
                               font=('Arial', 10), width=10, height=1)
        self.infolabel.grid(row=4, column=3)

        self.showText = Button(self, text='开始生成', command=self.password_generate)
        self.showText.grid(row=3, column=3)

        self.tofile = Button(self, text='保存', command=self.save)
        self.tofile.grid(row=5, column=3)

        self.content = scrolledtext.ScrolledText(self, height=17, width=50)
        self.content.grid(row=5, column=2)


    def save(self):
        with open('password.txt', 'w+') as f:
            for i in self.password_list:
                f.write(i+'\n')
        messagebox.showinfo('结果', '保存成功 - 文件名为 password.txt')


if __name__ == '__main__':
    app = Application()
    app.master.title('A&D-密码生成器')
    app.master.geometry('520x400')
    app.mainloop()