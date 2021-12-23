from tkinter import *
from tkinter import filedialog as fd
import hashlib
import os

root=Tk()
root.geometry("250x190")

def apply_md5():
    txtfile = fd.askopenfilename(title="Open File",
                                         filetypes=(("Text Files", "*.txt"),))
    rtxtfile = open(txtfile, 'r')
    name=os.path.basename(txtfile)
    formattedname=name.split('.')[0]
    para = rtxtfile.read()
    bpara = para.hex()
    bpara = bytes.fromhex(para)
    hfile = hashlib.md5(bpara.encode())
    efile = open(str(formattedname)+"md5"+".txt", 'w')
    efile.write(str(hfile))
    print("MD5 function")
    
    
def apply_sha256():
    txtfile = fd.askopenfilename(title="Open File",
                                         filetypes=(("Text Files", "*.txt"),))
    rtxtfle = open(txtfile, 'r')
    name=os.path.basename(txtfile)
    formattedname=name.split('.')[0]
    para = txtfile.read()
    bpara = bytes.para
    bpara = bpara.hex()
    hfile = hashlib.sha256(bpara.encode())
    efile = open(str(formattedname)+"sha256"+".txt", 'w')
    efile.write(str(hfile))
    print("SHA function")   
    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()
