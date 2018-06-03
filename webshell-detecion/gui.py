from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import scrolledtext
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import time


def load_file(file_path, encoding='ISO-8859-15'):
    t = ''
    try:
        with open(file_path, encoding=encoding) as f:
            for line in f:
                line = line.strip('\n')
                t += line
    except Exception as e:
        print(e)
    return t


def visitDir(path, name='.php'):
    full_files = []
    file_content = []
    if not os.path.isdir(path):
        print('ERROR:', path, 'is not a directory or does not exist')
        return False, False
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     print(os.path.join(root, d))
        for f in files:
            file = os.path.join(root, f)
            if name in file:
                file_content.append(load_file(file))
                full_files.append(file)
    return file_content, full_files


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def webshell_scan(self):
        webshell_vectorizer = joblib.load('AndShell_dict.m')
        clf = joblib.load('AndShell_scan.m')

        path = self.input.get()
        file_content, full_files = visitDir(path, '.php')
        if file_content == False:
            messagebox.showinfo('错误', '输入不规范，必须是文件夹路径或者文件路径')
            return
        X = webshell_vectorizer.transform(file_content)

        self.bad_list = []
        for i in range(X.shape[0]):
            result = clf.predict(X[i])
            if result == 1:
                continue
            else:
                self.bad_list.append(full_files[i])

        self.content.delete(1.0, END)

        for i in self.bad_list :
            i = i + '\n'
            time.sleep(0.1)
            self.content.insert(END, i)
            self.content.update()
        self.filecount = '扫描文件数: {} , 发现文件数: {}'.format(len(full_files), len(self.bad_list))
        self.infolabel['text'] = self.filecount

        messagebox.showinfo('扫描成功', '扫描结束')

    def createWidgets(self):
        self.helloLabel = Label(self, text='A&D-WebShell-Scanner',
                                font=('Fira', 15), width=20, height=1)
        self.helloLabel.grid(row=1, column=2, padx=1, pady=1)

        self.introduction = Label(self, text='A&D工作室开发的基于机器学习的webshell扫描器，目前只支持PHP',
                                  font=('Arial', 10),height=2)
        self.introduction.grid(row=2, column=2)

        self.pathLabel = Label(self, text='路径:')
        self.pathLabel.grid(row=3,column=1)

        self.input = Entry(self, width=50)
        self.input.grid(row=3, column=2)

        self.filecount = '扫描文件数: 0 , 发现文件数: 0'
        self.infolabel = Label(self, text=self.filecount,
                               font=('Arial', 10), width=30, height=1)
        self.infolabel.grid(row=4, column=2)

        self.showText = Button(self, text='开始扫描', command=self.webshell_scan)
        self.showText.grid(row=3, column=3)

        self.tofile = Button(self, text='保存', command=self.save)
        self.tofile.grid(row=5, column=3)

        self.content = scrolledtext.ScrolledText(self, height=17, width=50)
        self.content.grid(row=5, column=2)


    def save(self):
        with open('result.txt', 'w+') as f:
            for i in self.bad_list:
                f.write(i+'\n')
        messagebox.showinfo('结果', '保存成功 - 文件名为 result.txt')


if __name__ == '__main__':
    app = Application()
    app.master.title('A&D-webshell扫描器')
    app.master.geometry('520x400')
    app.mainloop()