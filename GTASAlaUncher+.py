from tkinter import *
import webbrowser, os, shutil


def openMod():
    webbrowser.open('https://www.gtavicecity.ru')


def openVK():
    webbrowser.open('https://sa-launcher-plus.github.io/launch-site/')


def openGTASA():
    os.startfile('gta_sa.exe')
    quit()


def openGTASAMP():
    os.startfile('samp.exe')
    quit()


def openDELETE():
    root = Tk()
    root.title('Дополнительная информация')
    root.geometry('350x500')
    root.resizable(width=False, height=False)
    root.iconbitmap('iconlc+.ico')

    lab = Label(root, text='''Доп.информация:

Язык программирования
на котором работает лаунчер:
~~~ Python 3.7.4 32bit ~~~

Модули Python,
используемые в
работе лаунчера:
~~~ tkinter, os, webbrowser ~~~

Разработчик сборки и лаунчера:
~~~ Матвей Воронцов ~~~

Программист(ы):
~~~ Матвей Воронцов ~~~''')
    lab.config(font=('Times', 18))
    lab.pack()

    root.mainloop()


def openINST():
    os.startfile('инструкция.txt')


def toch_download():
    root = Tk()
    root.title('Идёт смена прицела')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\tochka\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def green_download():
    root = Tk()
    root.title('Идёт смена прицела')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\green\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def st_download():
    root = Tk()
    root.title('Идёт смена прицела')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\standart\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def fiol_download():
    root = Tk()
    root.title('Идёт смена прицела')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\fiol\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def form_download():
    root = Tk()
    root.title('Идёт смена прицела')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\form\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def stand_download():
    root = Tk()
    root.title('Идёт смена скинов')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\skins\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def pricel_download():
    win = Tk()
    win.title('Сменить прицел для сборки')
    win.resizable(width=False, height=False)
    win.geometry('335x300')
    win.iconbitmap('iconlc+.ico')

    butTochka = Button(win, text='Точка вместо прицела')
    butTochka.config(width=30, height=3, command=toch_download)
    butTochka.pack()

    butGreen = Button(win, text='Современный зелёный прицел')
    butGreen.config(width=30, height=3, command=green_download)
    butGreen.pack()

    butSt = Button(win, text='Классический (стандартный) прицел')
    butSt.config(width=30, height=3, command=st_download)
    butSt.pack()

    butPe = Button(win, text='Фиолетовый прицел')
    butPe.config(width=30, height=3, command=fiol_download)
    butPe.pack()

    butForm = Button(win, text='Прицел другой формы')
    butForm.config(width=30, height=3, command=form_download)
    butForm.pack()

    win.mainloop()


def terminator_download():
    root = Tk()
    root.title('Идёт смена скинов')
    root.geometry('350x5')
    root.resizable(width=False, height=False)

    dir = os.path.abspath(os.curdir)
    folder_from = r'' + dir + '\\' + 'edit_launch\\terminator\\'
    folder_to = dir + '\\' + r'\models'

    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            os.system(f'rd /S /Q {folder_to}\\{f}')
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

    root.destroy()

    root2 = Tk()
    root2.title('Смена завершена')
    root2.geometry('350x5')
    root2.resizable(width=False, height=False)

    root2.mainloop()

    root.mainloop()


def skins_download():
    win = Tk()
    win.title('Смена скинов')
    win.resizable(width=False, height=False)
    win.geometry('335x150')
    win.iconbitmap('iconlc+.ico')

    butStar = Button(win, text='Сменить все скины на стандартные')
    butStar.config(width=30, height=3, command=stand_download)
    butStar.pack()

    butTerminator = Button(win, text='''Сменить все скины на скины со 
сборки по тематике терминатора''')
    butTerminator.config(width=30, height=3, command=terminator_download)
    butTerminator.pack()

    win.mainloop()


def cleo_null_download():
    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir + '\\CLEO\\')


def cleo_full_download():
    dir = os.path.abspath(os.curdir)
    os.system(r"explorer.exe " + dir + '\\edit_launch\\cleo_full\\CLEO\\')


def html_open():
    os.startfile('info_cleo.html')


def cleo_download():
    win = Tk()
    win.title('CLEO скрипты')
    win.resizable(width=False, height=False)
    win.geometry('335x200')
    win.iconbitmap('iconlc+.ico')

    butFull = Button(win, text='''Открыть папку
с CLEO скриптами''')
    butFull.config(width=30, height=3, command=cleo_full_download)
    butFull.pack()

    butNull = Button(win, text='''Открыть папку CLEO
в папке с игрой''')
    butNull.config(width=30, height=3, command=cleo_null_download)
    butNull.pack()

    info = Button(win, text='''Читать информацию
о CLEO скриптах''')
    info.config(width=30, height=3, command=html_open)
    info.pack()

    win.mainloop()


window = Tk()
window.title('GTA SA LaUncher+ CRAZY RUSSIA Custom | V1.0')
window.resizable(width=False, height=False)
window.geometry('650x322')
window.iconbitmap('iconlc+.ico')

photo = PhotoImage(file="fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()

dev = Button(window, text='Страница разработчика')
dev.config(width=21, height=1, bg='white smoke', fg='black', command=openVK)
dev.place(x=2, y=296)

playClassic = Button(window, text='''Играть в классическую
GTA (GTA SA)''')
playClassic.config(width=21, height=2, bg='white smoke', fg='black', command=openGTASA)
playClassic.place(x=485, y=66)

playMultiplayer = Button(window, text='''Играть в мультиплеерную
GTA (GTA SAMP 0.3.7)''')
playMultiplayer.config(width=21, height=2, bg='white smoke', fg='black', command=openGTASAMP)
playMultiplayer.place(x=485, y=107)

download = Button(window, text='''Скачать дополнительные
моды (модификации)''')
download.config(width=21, height=2, bg='white smoke', fg='black', command=openMod)
download.place(x=485, y=148)

delete = Button(window, text='''Дополнительная
информация''')
delete.config(width=21, height=2, bg='white smoke', fg='black', command=openDELETE)
delete.place(x=485, y=189)

pricel = Button(window, text='''Сменить прицел''')
pricel.config(width=20, height=2, bg='white smoke', fg='black', command=pricel_download)
pricel.place(x=17, y=160)

skins = Button(window, text='''Смена скинов''')
skins.config(width=20, height=2, bg='white smoke', fg='black', command=skins_download)
skins.place(x=17, y=201)

cl = Button(window, text='''Сборка CLEO скриптов''')
cl.config(width=20, height=2, bg='white smoke', fg='black', command=cleo_download)
cl.place(x=17, y=242)

text3 = Label(window, text='Created by Matvey Vorontsov', fg='black')
text3.config(font=('Arial', 8))
text3.place(x=497, y=303)

window.mainloop()
