from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

main_window=Tk()
main_window.geometry("600x600")
main_window.resizable(False,False)
main_window.title("Port Scanner")
main_window.configure(bg="black")          

header_font= Font(family="Papyrus", size=30, weight="bold")
sub_font=Font(family="Papyrus", size=20, weight="bold",underline=1)
normal_font=Font(family="Papyrus", size=16, weight="bold")
input_font=Font(family="Papyrus", size=16, weight="bold")
footer_font=Font(family="Papyrus", size=11,weight="bold")

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


main_window.mainloop()