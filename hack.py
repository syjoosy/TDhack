from tkinter import *
from tkinter import messagebox as mb
import os
import shutil

eng = True
window = Tk()
version = '0.1'
name = 'TDHack v.' + version
window.title(name)
window.geometry('250x200')
lbl = Label(window, text="Teardown hack for version 0.7.2", font=("Arial", 12))
lbl.pack(expand=1, anchor=NW)


def hack():
    global eng
    if (os.name != "nt"):
        if (eng == True):
            mb.showerror("TDHack ERROR", "Only Windows support right now")
            exit()
        else:
            mb.showerror("TDHack ошибка", "Только Windows поддерживается в настоящее время")
            exit()
    location = ''
    global username
    homepath = os.getenv('USERPROFILE')
    path_documents = homepath + '\Documents\Teardown\savegame.xml'
    path_app = homepath + '\AppData\Local\Teardown\savegame.xml'
    if (os.path.isfile(path_documents) == False) and (os.path.isfile(path_app) == False):
        if (eng == True):
            mb.showerror("TDHack ERROR", "The program could not find the save file")
            exit()
        else:
            mb.showerror("TDHack ошибка", "Программа не смогла найти файл сохранений")
            exit()
    elif (os.path.isfile(path_documents) == True):
        location = 'Documents'
    elif (os.path.isfile(path_app) == True):
        location = 'AppData'
    try:
        if (location == 'AppData'):
            path = homepath + '\AppData\Local\Teardown'
        else:
            path = homepath + '\Documents\Teardown'
        path_backup = path + '\savegame_backup.xml'
        path_newfile = path + '\savegame_new.xml'
        shutil.copyfile(path_app, path_backup)
        f = open(path_app, 'r')
        new_file = open(path_newfile, 'w')
        for line in f:
            new_file.write(re.sub("([\t][\t]+)", "", line))
        new_file.close()
        new_file = open(path_newfile, 'r')
        lines = new_file.readlines()
        f.close()
        new_file.close()
        tool_start = False
        tool_end = False
        mission_start = False
        mission_end = False
        f = open(path_app, 'w')
        for line in lines:
            if (cash.get() == 1):
                if (line.startswith("<cash") == True):
                    line = '<cash value="9999999"/>\n'
            if (levels.get() == 1):
                if (line.startswith("<mission>") == True):
                    mission_start = True
                if (line.startswith("</mission>") == True):
                    mission_end = True
                if (weapons.get() == 1):
                    if (line.startswith("<tool>") == True):
                        tool_start = True
                    if (line.startswith("</tool>") == True):
                        tool_end = True
                if (mission_end == True):
                    mission_start = False
                    mission_end = False
                    line = '''
                    <mission>
                    <mall_foodcourt value="1">
                        <score value="1"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="1.1"/>
                    </mall_foodcourt>
                    <lee_computers value="1">
                        <score value="3"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="4.8"/>
                    </lee_computers>
                    <marina_gps value="1">
                        <score value="3"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="2.3"/>
                    </marina_gps>
                    <mansion_fraud value="1">
                        <score value="3"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="2.3"/>
                    </mansion_fraud>
                    <caveisland_propane value="1">
                        <score value="3"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="2.3"/>
                    </caveisland_propane>
                    <frustrum_chase value="1">
                        <score value="3"/>
                        <timeleft value="-1.0"/>
                        <missiontime value="2.3"/>
                    </frustrum_chase>
                </mission>
                    '''
            if (tool_end == True):
                tool_start = False
                tool_end = False
                line = '''
                    <tool>
                    <sledge>
                        <enabled value="1"/>
                    </sledge>
                    <spraycan>
                        <enabled value="1"/>
                    </spraycan>
                    <extinguisher>
                        <enabled value="1"/>
                    </extinguisher>
                    <shotgun>
                        <enabled value="1"/>
                    </shotgun>
                    <rocket>
                        <enabled value="1"/>
                    </rocket>
                    <pipebomb>
                        <enabled value="1"/>
                    </pipebomb>
                    <gun>
                        <enabled value="1"/>
                    </gun>
                    <bomb>
                        <enabled value="1"/>
                    </bomb>
                    <blowtorch>
                        <enabled value="1"/>
                    </blowtorch>
                    <plank>
                        <enabled value="1"/>
                    </plank>
                </tool>'''
            if (tool_start == True):
                line = ''
            if (mission_start == True):
                line = ''
            f.write(line)
        f.close()
        os.remove(path_newfile)
        if (eng == True):
            mb.showinfo("TDHack", f"Hack successful!\nThe folder {path} contains a backup copy")
        else:
            mb.showinfo("TDHack", f"Успешно!\nВ папке {path} находится резервная копия")
    except:
        if (eng == True):
            mb.showerror("TDHack ERROR", "Error opening save file")
            exit()
        else:
            mb.showerror("TDHack ошибка", "Ошибка открытия файла сохранений")
            exit()


def change_language():
    global eng
    if (eng == True):
        lbl.configure(text="Взлом Teardown для версии 0.7.2")
        chk.configure(text="Открыть все уровни")
        chk1.configure(text="Открыть всё оружие")
        chk2.configure(text="Бесконечные деньги")
        btn.configure(text='ENG')
        btn1.configure(text='Взломать')
        eng = False
    elif (eng == False):
        lbl.configure(text="Teardown hack for version 0.7.2")
        chk.configure(text="Open all levels")
        chk1.configure(text="Open all weapon")
        chk2.configure(text="Unlimited cash")
        btn.configure(text='RU')
        btn1.configure(text='Hack')
        eng = True

levels = IntVar()
weapons = IntVar()
cash = IntVar()

btn = Button(window, text="RU", command=change_language)
btn.pack(expand = 1, anchor = NE, padx = 5, ipadx = 5)

chk = Checkbutton(window, text='Open all levels', var=levels)
chk.pack()

chk1 = Checkbutton(window, text='Open all weapons', var=weapons)
chk1.pack()

chk2 = Checkbutton(window, text='Unlimited cash', var=cash)
chk2.pack()

btn1 = Button(window, text="Hack", command=hack)
btn1.pack()

lbl_info = Label(window, text="by syjoosy", font=("Arial Bold", 18))
lbl_info.pack(expand=1, anchor=SE)

window.mainloop()