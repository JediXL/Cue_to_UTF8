'''
@auther: Jedi.L
@Date: Wed, May 22, 2019 2:08
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''

# import sys
# import os

import tkinter as tk
from tkinter.ttk import Separator
import tkinter.messagebox as mb
import os

import chardet
import codecs
from tkinter.filedialog import askdirectory


def selectPath():
    cue_path = askdirectory()
    path.set(cue_path)
    scan()


def scan():
    # selected or not
    filelist = []
    f_dir = os.listdir(path.get())
    for f in f_dir:
        if os.path.splitext(f)[1] == ".cue":
            filelist.append(f)
    cues.set(filelist)


# Trans All found .cue files to UTF-8
def toUTF8():
    # !!! does not backup the origin file
    if cues.get() == '':
        mb.showinfo("Error", " .cue file not find")
    else:
        selected_index = list(cue_list.curselection())
        for i in selected_index:
            filepath = path.get() + '/' + cue_list.get(i)
            # print(filepath)
            trans(filepath)
        mb.showinfo("Done", "Now All .cue files are UTF-8")


# Trans .cue file to UTF-8
def trans(filepath):
    content = codecs.open(filepath, 'rb').read()
    source_encoding = chardet.detect(content)['encoding']
    if source_encoding is None:
        mb.showinfo("Error", "Can not detect file encoding")
        return
    # print("  ", source_encoding, filepath)
    if source_encoding != 'utf-8' and source_encoding != 'UTF-8-SIG':
        content = content.decode(source_encoding,
                                 'ignore')  # .encode(source_encoding)
        codecs.open(filepath, 'w', encoding='UTF-8').write(content)


# for GUI
root = tk.Tk()
root.title("Cues2UTF8")
path = tk.StringVar()
filelist = []
cues = tk.StringVar()

lab_path = tk.Label(root, text=" 1. Select Folder Path:")
lab_path.pack()
enr_path = tk.Entry(root, textvariable=path, bg="white")
enr_path.pack()

# bp = tk.BitmapImage(file="open.bmp")
bt_sel = tk.Button(root, text="Open", command=selectPath)
bt_sel.pack(fill="x")

Separator(root, orient="horizontal").pack(fill="x")


lab_sel = tk.Label(root, text="2. Select Files")
lab_sel.pack()
cue_list = tk.Listbox(root, listvariable=cues, selectmode="multiple")
cue_list.pack()

Separator(root, orient="horizontal").pack(fill="x", pady=5)
bt_start = tk.Button(root, text="Click to Start", command=toUTF8)
bt_start.pack(fill="x")


root.mainloop()
