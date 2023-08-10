from os import walk
import tkinter as t
import tkinter.messagebox as m

r = t.Tk()
r.geometry('300x500')
r.title('jw查找文件')
exePaths = t.StringVar()
exePaths.set('查找结果：')
exeText = t.Label(r, text='请输入要查找的文件名（如：xxx.exe）：')
exe = t.Entry(r)
pathText = t.Label(r, text=r'请输入要查找的目录（如：C：\xxx\xxx）：')
path = t.Entry(r)
exeText.pack()
exe.pack()
pathText.pack()
path.pack()
nPath = t.Listbox(r, listvariable=exePaths,width=40)


def cz():
    exePaths.set('查找结果：')
    try:
        files = walk(path.get())
        for p, f, e in files:
            for ne in e:
                if ne == exe.get():
                    nPath.insert('end', p + '\\' + ne)
        nPath.pack()
    except:
        m.showwarning(title='错误', message='无法查找')


finds = t.Button(r, text='查找', command=cz, width=10)
finds.pack()

r.mainloop()
