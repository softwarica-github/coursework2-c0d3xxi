
########## PORT SCANNER - Developed by Parth Dhungana ##############

#importing modules

import csv
import socket
import time
import datetime
import threading
from queue import Queue
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

#logo path

logo_path=""

main_window=Tk()
main_window.geometry("600x600")
main_window.resizable(False,False)
main_window.title("Port Scanner")
main_window.iconbitmap(logo_path)
main_window.configure(bg="black")          

#name var for text entry:

namebox = StringVar()
ipbox = StringVar() 
spbox = IntVar()
epbox = IntVar()

#fonts:

header_font= Font(family="Papyrus", size=30, weight="bold")
sub_font=Font(family="Papyrus", size=20, weight="bold",underline=1)
normal_font=Font(family="Papyrus", size=16, weight="bold")
input_font=Font(family="Papyrus", size=16, weight="bold")
footer_font=Font(family="Papyrus", size=11,weight="bold")

results = StringVar()
#functions for buttons:

#for scan button:

def scan_res():
    
    if namebox.get()=="" or ipbox.get()=="" or spbox.get()=="" or epbox.get()=="":
        msg=messagebox.showerror("ERROR", "Empty feild(s)!\n\nPlease fill out all the feilds with the correct details!!")
        
    elif spbox.get()>epbox.get():
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of start port cannot be greater than that of end port!!")
        
    elif epbox.get()>65535 or epbox.get()<=0:
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of end port must be greater than 1 and less than or equal to 65,535!!")
    
    elif spbox.get()<0 or epbox.get()<0:
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of start port and end port must be a positive integer between 0 and 65,535!!")
        
    
###########################################################################################################################################################################################################################################################################################################################################

    else:
         res_window=Tk()
         res_window.geometry("1200x720")
         res_window.resizable(False,False)

         res_window.title("Port Scanner (Scan Results)")
         res_window.iconbitmap(logo_path)
         res_window.configure(bg="black")
        
         lbl_header1=Label(res_window, text = "Scan results 🔎",bg="black", fg="Green", font=("Papyrus", 30,"bold"))
         lbl_header1.place(relx=0.5,rely=0.110,anchor=CENTER)
       
        #output display
        
         lbl_op=Label(res_window, text=op_results, fg="Black", bg="Green",font=("Papyrus", 16,"bold"))
         lbl_op.place(relx=0.5,rely=0.505, anchor=CENTER)
        
         bt_exit_res=ttk.Button(res_window, text="Exit", command= res_window.destroy)
         bt_exit_res.place(relx=0.695,rely=0.810)
        
        #op_text.place(relx=0.5,rely=0.5,anchor=CENTER)
         lbl_CR=Label(res_window, text="Copyright © 2022   Parth Dhungana, All Rights Reserved.", bg="Green", fg="black", padx=400, font=("Papyrus", 11,"bold"))
         lbl_CR.place(relx=0.5,rely=0.980,anchor=CENTER)

         res_window.mainloop()

 #widgets:

lbl_header=Label(main_window, text = "🔎ort Scanner",bg="black", fg="Green", font=header_font)
lbl_header.place(relx=0.5,rely=0.110,anchor=CENTER)

lbl_text1=Label(main_window, text = "Enter the required details below:", bg="black", fg ="white", font=sub_font)
lbl_text1.place(relx=0.5,rely=0.250, anchor=CENTER)

#Target name:

lbl_name=Label(main_window, text="👉 Target Name:", bg="black", fg="Green", font=normal_font)
lbl_name.place(relx=0.075,rely=0.370)

#target name input box:

text_name=Entry(main_window, font=input_font, textvariable=namebox)
text_name.place(relx=0.480,rely=0.370)
text_name.focus()

#Target IP:

lbl_ip=Label(main_window, text="👉 Target IP Address:", bg="black", fg="Green", font=normal_font)
lbl_ip.place(relx=0.075,rely=0.470)

#IP addr input box:

text_ip=Entry(main_window, font=input_font, textvariable=ipbox)
text_ip.place(relx=0.480,rely=0.470)

#Start Port:

lbl_port1=Label(main_window, text="👉 Start Port Number:", bg="black", fg="Green", font=normal_font)
lbl_port1.place(relx=0.075,rely=0.570)

#Start port input box:

text_box1=Entry(main_window,font=input_font, width = 7, textvariable=spbox)
text_box1.place(relx=0.480,rely=0.570)
text_box1.delete(0,END)

#End Port:

lbl_port2=Label(main_window, text="👉 End Port Number: ", bg="black", fg="Green", font=normal_font)
lbl_port2.place(relx=0.075,rely=0.670)

#End port input box:

text_box2=Entry(main_window,font=input_font, width = 7, textvariable=epbox)
text_box2.place(relx=0.480,rely=0.670)
text_box2.delete(0,END)


#Frame
button_frame= Frame(main_window, bg="black")
button_frame.place(relx=0.5,rely=0.850, anchor=CENTER)

#buttons:

bt_scan=ttk.Button(button_frame, text="Scan 🔎", command=scan_res)
bt_scan.grid(row=0,column=0,padx=30)   #place(relx=0.185,rely=0.810)

bt_logs=ttk.Button(button_frame, text="View Logs", command= prev_logs)
bt_logs.grid(row=0,column=1,padx=30)

bt_reset=ttk.Button(button_frame, text="Reset", command=re_set)
bt_reset.grid(row=0,column=2,padx=30)    #place(relx=0.440,rely=0.810)

bt_exit=ttk.Button(button_frame, text="Exit", command= exit_prog)
bt_exit.grid(row=0,column=3,padx=30)     #place(relx=0.695,rely=0.810)


main_window.mainloop()