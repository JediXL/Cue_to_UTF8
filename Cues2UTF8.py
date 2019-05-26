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
        mb.showinfo("Done", "Now All .cue files are Fixed")


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
root.title("Cues-to-UTF8")
path = tk.StringVar()
filelist = []
cues = tk.StringVar()

lab_path = tk.Label(root, text="1. Select Path", fg='#2F4F4F')
lab_path.grid(row=0, column=0, sticky="w")
enr_path = tk.Entry(root, textvariable=path, bg="white")
enr_path.grid(row=1, column=0, sticky="ew")
# bp = tk.BitmapImage(file="open.bmp")
bt_sel = tk.Button(root, text="Open", command=selectPath)
bt_sel.grid(row=1, column=1, sticky="ew")

Separator(
    root, orient="horizontal").grid(
        row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

lab_sel = tk.Label(root, text="2. Select Files", fg='#2F4F4F')
lab_sel.grid(row=4, column=0, sticky="w")
cue_list = tk.Listbox(root, listvariable=cues, selectmode="multiple")
cue_list.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)


Separator(
    root, orient="horizontal").grid(
        row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=1)

bt_start = tk.Button(
    root,
    text="Start",
    highlightbackground="yellow",
    fg="Black",
    highlightthickness=30,
    command=toUTF8)
bt_start.grid(row=7, column=0, columnspan=2, sticky="ew")

Separator(
    root, orient="horizontal").grid(
        row=8, column=0, columnspan=2, sticky="ew", padx=5, pady=3)

lab_sign = tk.Label(root, text="Created by @Jedi.L")
lab_sign.grid(row=9, column=0, columnspan=2, sticky="ew")

root.mainloop()
