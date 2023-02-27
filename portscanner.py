########## PORT SCANNER - Developed by Parth Dhungana ##############

#importing modules
import csv
import socket
import time
import datetime
import threading
import MySQLdb
import sys
from queue import Queue
import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

#Customization Themes
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# #Database connection

db = MySQLdb.connect(host="localhost",user = 'root', password='', database='portscanner')
cursor1= db.cursor()

#logo path

logo_path="det2.ico"

#file path

file_path="logs.csv"

#main windown (root) properties:

main_window=customtkinter.CTk()
main_window.geometry("600x700")
main_window.resizable(False,False)
main_window.title("Port Scanner")
#main_window.iconbitmap(logo_path)
main_window.configure(bg="black")          

#name var for text entry:

namebox = StringVar()
ipbox = StringVar() 
spbox = IntVar()
epbox = IntVar()

#fonts:
#font=customtkinter.CTkFont(family='Papyrus', size=30, weight="bold")
header_font=customtkinter.CTkFont(family="Papyrus", size=35, weight="bold")
sub_font=customtkinter.CTkFont(family="Papyrus", size=25, weight="bold",underline=1)
normal_font=customtkinter.CTkFont(family="Papyrus", size=21, weight="bold")
input_font=customtkinter.CTkFont(family="Papyrus", size=21, weight="bold")
footer_font=customtkinter.CTkFont(family="Papyrus", size=16,weight="bold")

results = StringVar()
#functions for buttons:

#for scan button:

def scan_res():
    
    target = ipbox.get()
    
    if namebox.get()=="" or target=="" or spbox.get()=="" or epbox.get()=="":
        msg=messagebox.showerror("ERROR", "Empty feild(s)!\n\nPlease fill out all the feilds with the correct details!!")
            
    elif spbox.get()>epbox.get():
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of start port cannot be greater than that of end port!!")
        
    elif epbox.get()>65535 or epbox.get()<=0:
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of end port must be greater than 1 and less than or equal to 65,535!!")
    
    elif spbox.get()<0 or epbox.get()<0:
        msg=messagebox.showerror("ERROR", "ERROR!!\n\nValue of start port and end port must be a positive integer between 0 and 65,535!!")    
    
###########################################################################################################################################################################################################################################################################################################################################

    else:

        target = target.strip()
         # Split the IP into 4 octets
        octet = target.split('.')

        # Check if each octet is an integer
        if all(octet[i].isnumeric() for i in range(4)) and len(octet) == 4:
        # If all 4 octets are ints put the IP back together
            target = '.'.join(octet)                                                                                           
            
            
        #PORT SCANNER (MAIN)

            queue = Queue()
            open_ports=[]
            
            display_dt=datetime.datetime.now()
            c_dt=display_dt.strftime("%c")
            
            start_time = time.time()

            def scanner(port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    return True
                
                except:
                    return False
            
            def queue_range(port_lst):
                for port in port_lst:
                    queue.put(port)
                    
            def thread_func():
                while not queue.empty():
                    port = queue.get()
                    if scanner(port):
                        open_scanned=print("Port #{} is open!".format(port))
                        open_ports.append(port)
                        #return unittest

            port_lst = range(spbox.get(),epbox.get()+1)
            queue_range(port_lst)

            thread_lst = []

            for t in range(1000):
                thread=threading.Thread(target = thread_func)
                thread_lst.append(thread)
                
            for thread in thread_lst:
                thread.start()
                
            for thread in thread_lst:
                thread.join()

            end_time = time.time()
            
            elapsed_time = end_time-start_time
            
            op_results=("{} \n\nTarget Name: {} \n\n{} OPEN PORTS FOUND!!!\n\nPorts open on: {} \n\nTime elapsed: {} seconds.\n").format(c_dt,namebox.get(),len(open_ports),open_ports,elapsed_time)

            #storing output to variables
            
            a=str(c_dt)
            b=str(namebox.get())
            c=str(ipbox.get())
            d=str(spbox.get())
            e=str(epbox.get())
            f=str(open_ports)
            g=str(elapsed_time)
            data=[a,b,c,d,e,f,g]

            #Writing output to csv file
          
            with open(file_path, "a", newline="") as file_op:
                
                writer= csv.writer(file_op)

                writer.writerow(data)
            file_op.close()
            
            #Writing output to database

            cursor1.execute('INSERT INTO `logs`(`date_time`, `name`, `ip`, `start_port`, `end_port`, `open_ports`, `time_taken`) VALUES(%s, %s, %s, %s, %s, %s, %s)', data)

            
            db.commit()

            #Output
            
            messagebox.showinfo("Scan Result", op_results)

###########################################################################################################################################################################################################################################################################################################################################
             
        else:
            msg=messagebox.showerror("ERROR", "You have entered an invalid IP!!\n Use format (xxx.xxx.xxx.xxx)")
        
#for view logs button:
def prev_logs():
    msg_vlogs=messagebox.askyesno("View Logs", "Do you wish to view previous logs??")
    
    if msg_vlogs==True:
        
        log_window=customtkinter.CTk()
        log_window.geometry("1300x400")
        log_window.resizable(False,False)

        log_window.title("Port Scanner (View Logs)")
        log_window.iconbitmap(logo_path)
        
        
        #Output Database Table using Treeview
        
        tv = ttk.Treeview(log_window, columns=(1,2,3,4,5,6,7,8), show="headings", height="25")
        tv.pack()
        
        tv.heading(1, text="ID")
        tv.heading(2, text="Date/Time")
        tv.heading(3, text="Target Name")
        tv.heading(4, text="Target IP")
        tv.heading(5, text="Start Port")
        tv.heading(6, text="End Port")
        tv.heading(7, text="Open Ports")
        tv.heading(8, text="Time Taken(s)")
        
        sql = "SELECT * FROM  logs"
        cursor1.execute(sql)
        rows = cursor1.fetchall()
        
        for i in rows:
            tv.insert('','end', values=i)
        
        log_window.mainloop()
    else:
        pass

#for reset button:

def re_set():
    if ipbox.get()=="" and spbox.get()=="" and epbox.get()=="" and namebox.get()=="":
        pass
    
    elif ipbox.get()!="" or spbox.get()!="" or epbox.get()!="" or namebox.get():
        msg_re=messagebox.askyesno("RESET", "Are you sure you want to reset all the feilds??")
        
        if msg_re==True:
            ipbox.set("")
            spbox.set("")
            epbox.set("")
            namebox.set("")
            msg_done=messagebox.showinfo("RESET","Reset successful!!")
        else:
            pass
    
#for exit button:

def exit_prog():
    msg_ex=messagebox.askyesno("EXIT", "Are you sure you want to exit 🔎ort Scanner??")
    if msg_ex==True:
        exit()
    else:
        pass
  
#widgets:

lbl_header=customtkinter.CTkLabel(main_window, text = "🔎ort Scanner", font=header_font)
lbl_header.place(relx=0.5,rely=0.110,anchor=CENTER)

lbl_text1=customtkinter.CTkLabel(main_window, text = "Enter the required details below:", font=sub_font)
lbl_text1.place(relx=0.5,rely=0.250, anchor=CENTER)

#Target name:

lbl_name=customtkinter.CTkLabel(main_window, text="👉 Target Name:", font=normal_font)
lbl_name.place(relx=0.075,rely=0.370)

#target name input box:

text_name=customtkinter.CTkEntry(main_window, font=input_font, textvariable=namebox, width=250, border_width=1, text_color="red")
text_name.place(relx=0.480,rely=0.370)
text_name.focus()

#Target IP:

lbl_ip=customtkinter.CTkLabel(main_window, text="👉 Target IP Address:", font=normal_font)
lbl_ip.place(relx=0.075,rely=0.470)

#IP addr input box:

text_ip=customtkinter.CTkEntry(main_window, font=input_font, textvariable=ipbox, width=250, border_width=1, text_color="red")
text_ip.place(relx=0.480,rely=0.470)

#Start Port:

lbl_port1=customtkinter.CTkLabel(main_window, text="👉 Start Port Number:", font=normal_font)
lbl_port1.place(relx=0.075,rely=0.570)

#Start port input box:

text_box1=customtkinter.CTkEntry(main_window,font=input_font, textvariable=spbox, border_width=1, text_color="red")
text_box1.place(relx=0.480,rely=0.570)
text_box1.delete(0,END)

#End Port:

lbl_port2=customtkinter.CTkLabel(main_window, text="👉 End Port Number: ", font=normal_font)
lbl_port2.place(relx=0.075,rely=0.670)

#End port input box:

text_box2=customtkinter.CTkEntry(main_window,font=input_font, textvariable=epbox, border_width=1, text_color="red")
text_box2.place(relx=0.480,rely=0.670)
text_box2.delete(0,END)


#buttons:

bt_scan=customtkinter.CTkButton(main_window, text="Scan 🔎", command=scan_res, corner_radius=18, height =40, font=("Papyrus", 20, "bold"), text_color="gold")
#bt_scan.grid(row=0,column=0,padx=30)   
bt_scan.place(relx=0.185,rely=0.780)

bt_logs=customtkinter.CTkButton(main_window, text="View Logs 📜", command= prev_logs, corner_radius=18, height =40, font=("Papyrus", 20, "bold"))
bt_logs.place(relx= 0.575, rely =0.780)
bt_reset=customtkinter.CTkButton(main_window, text="Reset", command=re_set, corner_radius=18, height =40, font=("Papyrus", 20, "bold"))
bt_reset.place(relx=0.185,rely=0.870)

bt_exit=customtkinter.CTkButton(main_window, text="Exit", command= exit_prog, corner_radius=18, height =40, font=("Papyrus", 20, "bold"))
bt_exit.place(relx=0.605,rely=0.870)

#right click pop-up menu:

rt_clk = Menu(main_window, tearoff=0)

rt_clk.add_command(label="New Window")
rt_clk.add_separator()
rt_clk.add_command(label="Scan", command= scan_res)
rt_clk.add_command(label="View Logs", command= prev_logs)
rt_clk.add_command(label="Reset", command= re_set)
rt_clk.add_separator()
rt_clk.add_command(label="Exit", command= exit_prog)

def menupopup(event):
   
   try:
      rt_clk.tk_popup(event.x_root, event.y_root, 0)
   
   finally:
      rt_clk.grab_release()
    
main_window.bind("<Button-3>", menupopup)


#Window Theme (Dark Mode/Light Mode)
def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


appearance_mode_optionemenu = customtkinter.CTkOptionMenu(main_window, values=["Light", "Dark", "System"],command=change_appearance_mode_event, font=("Papyrus", 16, "bold"))
appearance_mode_optionemenu.place(relx=0.75,rely=0.015)
#default
appearance_mode_optionemenu.set("Dark")

#footer:

lbl_CR=customtkinter.CTkLabel(main_window, text="Copyright © 2023   Parth Dhungana, All Rights Reserved.", padx=150, font=footer_font)
lbl_CR.place(relx=0.5,rely=0.980,anchor=CENTER)

#MenuBar:
menubar=Menu(main_window)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="View Logs",command=prev_logs)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_prog)

menubar.add_cascade(label="Menu",menu=filemenu)


main_window.config(menu=menubar)

#screen loop:

main_window.mainloop()

