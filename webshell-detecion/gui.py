from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import scrolledtext


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def webshell_scan(self):
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.externals import joblib
        from FileTravel import visitDir
        import time

        webshell_vectorizer = joblib.load('AndShell_dict.m')
        clf = joblib.load('AndShell_scan.m')

        path = self.input.get()
        file_content, full_files = visitDir(path, '.php')
        X = webshell_vectorizer.transform(file_content)

        bad_list = []
        for i in range(X.shape[0]):
            result = clf.predict(X[i])
            if result == 1:
                continue
            else:
                bad_list.append(full_files[i])

        for i in bad_list :
            i = i + '\n'
            time.sleep(0.1)
            self.content.insert(END, i)
            self.content.update()

    def createWidgets(self):
        self.helloLabel = Label(self, text='A&D工作室',
                                font=('Arial',15), width=15, height=2)
        self.helloLabel.grid(row=1, column=3, padx=2, pady=1)

        self.introduction = Label(self, text='A&D工作室开发的基于机器学习的webshell扫描器，目前只支持PHP',
                                  font=('Arial', 10),height=2)
        self.introduction.grid(row=2, column=3)

        self.input = Entry(self, show='', width=50)
        self.input.grid(row=3, column=3)

        self.showText = Button(self, text='show', command=self.webshell_scan)
        self.showText.grid(row=3, column=4)

        self.content = scrolledtext.ScrolledText(self, height=18, width=50)
        self.content.grid(row=4, column=3)


    def show(self):
        var = self.input.get()
        var = var+'\n'
        self.content.insert('insert', var)

    def hello(self):
        name = self.nameInput.get()
        messagebox.showinfo('Message', 'hello, %s'%name)



app = Application()
app.master.title('hello, world')
app.master.geometry('500x400')
app.mainloop()