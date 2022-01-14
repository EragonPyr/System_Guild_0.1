# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#User datas
user_id=[]
user_pass=[]
user_name=[]
user_surname=[]
user_tel=[]
user_ema=[]
user_balan=[]
user_soft=[]
user_hard=[]
user_casu=[]
user_spe=[]
#Mission datas
mission_id=[]
mission_type=[]
mission_boss=[]
mission_title=[]
mission_explanation=[]
mission_reward=[]
mission_worker=[]
#Message datas
message_id=[]
message_time=[]
message_text=[]
admin_data=open("admin.txt","r")
admin=admin_data.readline()
admin_data.close()
global mission_num
global control_us
control_us=0
def time():
    string = strftime('%H:%M:%S %p')
    watch_lb.config(text = string)
    watch_lb.after(1000, time)
def user_set_new():
    global user_num
    user_data=open("user_data.txt","w")
    user_data.write(str(user_num))
    user_data.write("\n")
    for i in range(int(user_num)):
        i=i+1001
        user_data.write(str(i))
        user_data.write("\n")
        i=i-1001
        user_data.write(str(user_pass[i]))
        user_data.write("\n")
        user_data.write(str(user_name[i]))
        user_data.write("\n")
        user_data.write(str(user_surname[i]))
        user_data.write("\n")
        user_data.write(str(user_tel[i]))
        user_data.write("\n")
        user_data.write(str(user_ema[i]))
        user_data.write("\n")
        user_data.write(str(user_balan[i]))
        user_data.write("\n")
        user_data.write(str(user_soft[i]))
        user_data.write("\n")
        user_data.write(str(user_hard[i]))
        user_data.write("\n")
        user_data.write(str(user_casu[i]))
        user_data.write("\n")
        user_data.write(str(user_spe[i])) 
        user_data.write("\n")
    user_data.close()
def user_set():
    global user_num
    global test_id
    global control_us
    print(test_id)
    if control_us==1:
        if nihahahaha.tb_pass_a_c.get()==nihahahaha.tb_pass_b_c.get():
            control_us=0
            test_id+=1001
            user_id.append(str(test_id))
            test_id-=1001
            print(user_id[test_id])
            user_pass.append(nihahahaha.tb_pass_a_c.get())
            user_name.append(nihahahaha.tb_name_c.get())
            user_surname.append(nihahahaha.tb_surname_c.get())
            user_tel.append(nihahahaha.tb_tel_c.get())
            user_ema.append(nihahahaha.tb_mail_c.get())
            user_balan.append("200")
            user_soft.append("0")
            user_hard.append("0")
            user_casu.append("0")
            user_spe.append("0")
            mail = smtplib.SMTP("smtp.gmail.com",587)          
            mail.ehlo()
            mail.starttls()
            mail.login("systemguildcompany@gmail.com","SystemGuildCompany123*")  
            mesaj = MIMEMultipart()

            mesaj["From"] = " systemguildcompany@gmail.com"
            mesaj["To"] = user_ema[test_id]

            mesaj["Subject"] = "Account confirmation"
            gmail_mes_ta="Welcome to System Guild Family "+nihahahaha.tb_name_c.get()+"\nWe are happy for see you in here\nAnd your id is"+user_id[test_id]
            body = gmail_mes_ta
            body_text = MIMEText(body, "plain")  
            mesaj.attach(body_text)
            mail.sendmail( mesaj["From"], mesaj["To"], mesaj.as_string())
            user_data=open("user_data.txt","w")
            user_data.write(str(user_num))
            user_data.write("\n")
            for i in range(int(user_num)):
                i=i+1001
                user_data.write(str(i))
                user_data.write("\n")
                i=i-1001
                user_data.write(str(user_pass[i]))
                user_data.write("\n")
                user_data.write(str(user_name[i]))
                user_data.write("\n")
                user_data.write(str(user_surname[i]))
                user_data.write("\n")
                user_data.write(str(user_tel[i]))
                user_data.write("\n")
                user_data.write(str(user_ema[i]))
                user_data.write("\n")
                user_data.write(str(user_balan[i]))
                user_data.write("\n")
                user_data.write(str(user_soft[i]))
                user_data.write("\n")
                user_data.write(str(user_hard[i]))
                user_data.write("\n")
                user_data.write(str(user_casu[i]))
                user_data.write("\n")
                user_data.write(str(user_spe[i])) 
                user_data.write("\n")
            user_data.close()
        else:
            messagebox.showinfo("Warning","We have a problem ,control the text boxes and try again")
    else:
        if user_1_1_p.tb_pass_a.get()==user_1_1_p.tb_pass_b.get():
            user_pass[test_id]=user_1_1_p.tb_pass_a.get()
            user_name[test_id]=user_1_1_p.tb_name.get()
            user_surname[test_id]=user_1_1_p.tb_surname.get()
            user_tel[test_id]=user_1_1_p.tb_tel.get()
            user_ema[test_id]=user_1_1_p.tb_mail.get()
            user_data=open("user_data.txt","w")
            user_data.write(user_num)
            user_data.write("\n")
            for i in range(int(user_num)):
                i=i+1001
                user_data.write(str(i))
                user_data.write("\n")
                i=i-1001
                user_data.write(user_pass[i])
                user_data.write("\n")
                user_data.write(user_name[i])
                user_data.write("\n")
                user_data.write(user_surname[i])
                user_data.write("\n")
                user_data.write(user_tel[i])
                user_data.write("\n")
                user_data.write(user_ema[i])
                user_data.write("\n")
                user_data.write(user_balan[i])
                user_data.write("\n")
                user_data.write(user_soft[i])
                user_data.write("\n")
                user_data.write(user_hard[i])
                user_data.write("\n")
                user_data.write(user_casu[i])
                user_data.write("\n")
                user_data.write(user_spe[i]) 
                user_data.write("\n")
            user_data.close()
            messagebox.showinfo("Confirmation","Your change has been saved")
        else:
            messagebox.showinfo("Warning","We have a problem ,control the text boxes and try again")
    """try:
        
    except:
        messagebox.showinfo("Warning","user_data.txt is not in suitable form\nClose the app and repair user_data.txt")"""
def user_get():
    print("hip1")
    try:
        user_data=open("user_data.txt","r")
        global user_num
        need=user_data.readline()
        user_num=need.replace("\n","")
        for i in range(int(user_num)):
            need=user_data.readline()
            user_id.append(need.replace("\n",""))
            need=user_data.readline()
            user_pass.append(need.replace("\n",""))
            need=user_data.readline()
            user_name.append(need.replace("\n",""))
            need=user_data.readline()
            user_surname.append(need.replace("\n",""))
            need=user_data.readline()
            user_tel.append(need.replace("\n",""))
            need=user_data.readline()
            user_ema.append(need.replace("\n",""))
            need=user_data.readline()
            user_balan.append(need.replace("\n",""))
            need=user_data.readline()
            user_soft.append(need.replace("\n",""))
            need=user_data.readline()
            user_hard.append(need.replace("\n",""))
            need=user_data.readline()
            user_casu.append(need.replace("\n",""))
            need=user_data.readline()
            user_spe.append(need.replace("\n",""))
            print(i)
        user_data.close()
    except:
        messagebox.showinfo("Warning","user_data.txt is not in suitable form\nClose the app and repair user_data.txt")
user_get()
def mission_get():
    print("hip2")
    try:
        mission_dt=open("mission_dt.txt","r")
        need=mission_dt.readline()
        mission_num=int(need.replace("\n",""))
        for i in range(mission_num):
            need=mission_dt.readline()
            mission_id.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_type.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_boss.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_title.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_explanation.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_reward.append(need.replace("\n",""))
            need=mission_dt.readline()
            mission_worker.append(need.replace("\n",""))
        mission_dt.close()
    except:
        messagebox.showinfo("Warning","mission_dt.txt is not in suitable form\nClose the app and repair mission_dt.txt")
mission_get()
def mission_set():
    mission_dt=open("mission_dt.txt","w")
    mission_dt.write(str(len(mission_id)))
    mission_dt.write("\n")
    for i in range(int(len(mission_id))):
        #print("con_1")
        mission_dt.write(str(mission_id[i]))
        mission_dt.write("\n")
        #print("con_2")
        mission_dt.write(str(mission_type[i]))
        mission_dt.write("\n")
        #print("con_3")
        mission_dt.write(str(mission_boss[i]))
        mission_dt.write("\n")
        #print("con_4")
        mission_dt.write(mission_title[i])
        mission_dt.write("\n")
        #print("con_5")
        mission_dt.write(mission_explanation[i])
        mission_dt.write("\n")
        #print("con_6")
        mission_dt.write(str(mission_reward[i]))
        mission_dt.write("\n")
        #print("con_7")
        mission_dt.write(str(mission_worker[i]))
        mission_dt.write("\n")
        #print("con_8")
def message_get():
    try:
        message_file=open("messages.txt","r")
        a=0
        while a==0:
            mess=message_file.readline()
            if mess=='\n':
                break
            if len(mess)==0:
                break
            message_id.append(mess)
            message_time.append(message_file.readline())
            message_text.append(message_file.readline())
    except:
        messagebox.showinfo("Warning","messages.txt is not in suitable form\nClose the app and repair messages.txt")
message_get()
def entry_p():
    print("no problemep")
    def finitto():
        root.destroy()
    def login_user_func():
        try:
            global test_id
            global test_ps
            test_id=int(entry_tb_1.get())
            test_ps=entry_tb_2.get()
            test_id=test_id-1001
            #print(admin)
            #print(test_id)
            if test_ps==admin and test_id==8998:
                root.destroy()
                admin_p()
                print("\nAdmin\n")
            elif str(user_pass[test_id])==str(test_ps):
                #print(test_id,"0")
                root.destroy()
                user_1_p()
            else:
                messagebox.showinfo("Warning","Your id/password is not suitable try again")
        except:
            messagebox.showinfo("Warning","Your id/password is not suitable try again")
    def new_user_func():
        root.destroy()
        nihahahaha()
        
    root = Tk()
    root.geometry('720x400')
    root.configure(background='#ffe8be')
    root.title('System Guild')
    tb_try_1=StringVar(root)
    tb_try_2=StringVar(root)
    logo=PhotoImage(file='System Guild-logos_black.png') #Burada normalde logo vardı ama nedense logo gözükmemeye başlayınca çıkardım
    logo_lb=Label(image=logo,bg='#ffe8be')
    #logo_lb=Label(root, text='System Guild', bg='#ffe8be', font=('arial', 20, 'italic'))
    logo_lb.place(relx=0.36,rely=0.05,relwidth=0.3,relheight=0.5)
    
    entry_lb_1=Label(root, text='User id:', bg='#ffe8be', font=('arial', 12, 'normal'))
    entry_lb_1.place(relx=0.32,rely=0.6)
    entry_lb_2=Label(root, text='User Password:', bg='#ffe8be', font=('arial', 12, 'normal'))
    entry_lb_2.place(relx=0.32,rely=0.7)
    
    entry_tb_1=Entry(root,textvariable=tb_try_1)
    entry_tb_1.place(relx=0.5,rely=0.61)
    entry_tb_2=Entry(root,textvariable=tb_try_2,show='*')
    entry_tb_2.place(relx=0.5,rely=0.71)
    
    Button(root, text='Login', bg='#F0F8FF', font=('arial', 12, 'normal'), command=login_user_func).place(relx=0.55, rely=0.8)
    Button(root, text='Sign Up', bg='#F0F8FF', font=('arial', 12, 'normal'), command=new_user_func).place(relx=0.35, rely=0.8)
    Button(root, text='Close', bg='#F0F8FF', font=('arial', 12, 'normal'), command=finitto).place(relx=0.87, rely=0.05)
    root.mainloop()
def nihahahaha():
    def back_to_start():
        i_am_bored.destroy()
        entry_p()
    def i_did_it():
        global user_num
        global test_id
        global control_us
        if nihahahaha.tb_name_c.get() != "" and nihahahaha.tb_surname_c.get() != "" and nihahahaha.tb_tel_c.get() != "" and nihahahaha.tb_mail_c.get() != "" and nihahahaha.tb_pass_a_c.get() != "" and nihahahaha.tb_pass_b_c.get() != "":
            if nihahahaha.tb_tel_c.get().isnumeric()==True:
                test_id=int(user_num)
                user_num=int(user_num)+1
                control_us=1
                user_set()
                messagebox.showinfo("Confirmation","Your account created\nAnd your user id sent your e-mail")
                i_am_bored.destroy()
                entry_p()
            else:
                messagebox.showinfo("Warning","Tel number must consist of numbers only")
        else:
            messagebox.showinfo("Warning","Don't leave any space")
    i_am_bored = Tk()
    i_am_bored.geometry('720x400')
    i_am_bored.configure(background='#ffe8be')
    i_am_bored.title('System Guild')
    
    Label(i_am_bored, text='Name:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=20)
    Label(i_am_bored, text='Surname:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=60)
    Label(i_am_bored, text='Tel Number:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=100)
    Label(i_am_bored, text='E-Mail:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=140)
    Label(i_am_bored, text='Password:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=180)
    Label(i_am_bored, text='Password Again:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=220)
    
    name_1_c=StringVar(i_am_bored,"")
    name_2_c=StringVar(i_am_bored,"")
    tel_1_c=StringVar(i_am_bored,"")
    mail_1_c=StringVar(i_am_bored,"")
    pass_1_c=StringVar(i_am_bored,"")
    pass_2_c=StringVar(i_am_bored,"")
    
    nihahahaha.tb_name_c=Entry(i_am_bored,textvariable=name_1_c)
    nihahahaha.tb_name_c.place(x=320, y=20)
    nihahahaha.tb_surname_c=Entry(i_am_bored,textvariable=name_2_c)
    nihahahaha.tb_surname_c.place(x=320, y=60)
    nihahahaha.tb_tel_c=Entry(i_am_bored,textvariable=tel_1_c)
    nihahahaha.tb_tel_c.place(x=320, y=100)
    nihahahaha.tb_mail_c=Entry(i_am_bored,textvariable=mail_1_c)
    nihahahaha.tb_mail_c.place(x=320, y=140)
    nihahahaha.tb_pass_a_c=Entry(i_am_bored,textvariable=pass_1_c,show='*')
    nihahahaha.tb_pass_a_c.place(x=320, y=180)
    nihahahaha.tb_pass_b_c=Entry(i_am_bored,textvariable=pass_2_c,show='*')
    nihahahaha.tb_pass_b_c.place(x=320, y=220)
    
    Button(i_am_bored, text='Back to Start Page', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_to_start).place(x=40, y=280)
    Button(i_am_bored, text='Confirm', bg='#F0F8FF', font=('arial', 12, 'normal'), command=i_did_it).place(x=375, y=280)
    
    i_am_bored.mainloop()
    
def user_1_p():
    rank_info="Your ranks:\nSoftware: "+user_soft[test_id]+"\nHardware: "+user_hard[test_id]+"\nCasual: "+user_casu[test_id]+"\nSpecial: "+user_spe[test_id]
    balance_info="Your balance: "+user_balan[test_id]
    print(test_id,"1")
    def profile_check():
        u_p_1.destroy()
        user_1_1_p()
    def rank_check():
	    messagebox.showinfo("Rank Info",rank_info)
    def my_mission():
        u_p_1.destroy()
        user_1_5_p()
    def take_mission():
        u_p_1.destroy()
        user_1_4_p()
    def new_mission():
        u_p_1.destroy()
        user_1_3_p()
    def send_message():
        u_p_1.destroy()
        user_1_2_p()
    def balance_check():
	    messagebox.showinfo("Balance Info",balance_info)
    def help_me():
   	    messagebox.showinfo("Help","Profile=Check and edit your profile\nRanks=Check your ranks\nMy Quests=Your created and took quests\nQuest Board=Quests are taken from here\nCreate a Quest=Create your own quest\nSend Message to Admin=In special stations you can send message to admin in here\nBalance=Check your money\nLog Out=I think you can guess")
    def log_out_u():
        u_p_1.destroy()
        entry_p()
    u_p_1 = Tk()
    u_p_1.geometry('720x400')
    u_p_1.configure(background='#ffe8be')
    u_p_1.title('System Guild')
    
    Button(u_p_1, text='Profile', bg='#F0F8FF', font=('arial', 12, 'normal'), command=profile_check).place(x=40, y=20)
    Button(u_p_1, text='Ranks', bg='#F0F8FF', font=('arial', 12, 'normal'), command=rank_check).place(x=40, y=60)
    Button(u_p_1, text='My Quests', bg='#F0F8FF', font=('arial', 12, 'normal'), command=my_mission).place(x=40, y=100)
    Button(u_p_1, text='Quest Board', bg='#F0F8FF', font=('arial', 12, 'normal'), command=take_mission).place(x=40, y=140)
    Button(u_p_1, text='Create a Quest', bg='#F0F8FF', font=('arial', 12, 'normal'), command=new_mission).place(x=40, y=180)
    Button(u_p_1, text='Send a Message To Admin', bg='#F0F8FF', font=('arial', 12, 'normal'), command=send_message).place(x=40, y=220)
    Button(u_p_1, text='Balance', bg='#F0F8FF', font=('arial', 12, 'normal'), command=balance_check).place(x=40, y=260)
    Button(u_p_1, text='Help', bg='#F0F8FF', font=('arial', 12, 'normal'), command=help_me).place(x=640, y=340)
    Button(u_p_1, text='Log Out', bg='#F0F8FF', font=('arial', 12, 'normal'), command=log_out_u).place(x=40, y=340)
    logo=PhotoImage(file='System Guild-logos_black.png') #Burada normalde logo vardı ama nedense logo gözükmemeye başlayınca çıkardım
    logo_lb=Label(image=logo,bg='#ffe8be')
    logo_lb.place(relx=0.5,rely=0.05,relwidth=0.45,relheight=0.75)
    u_p_1.mainloop()
def user_1_1_p():
    print(test_id,"2")
    def back_user_main():
        u_p_1_1.destroy()
        user_1_p()
    u_p_1_1 = Tk()
    u_p_1_1.geometry('720x400')
    u_p_1_1.configure(background='#ffe8be')
    u_p_1_1.title('System Guild')
    
    try:
        Label(u_p_1_1, text='Name:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=20)
        Label(u_p_1_1, text='Surname:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=60)
        Label(u_p_1_1, text='Tel Number:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=100)
        Label(u_p_1_1, text='E-Mail:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=140)
        Label(u_p_1_1, text='Password:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=180)
        Label(u_p_1_1, text='Password Again:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=220)
        
        name_1=StringVar(u_p_1_1,value=user_name[test_id])
        name_2=StringVar(u_p_1_1,value=user_surname[test_id])
        tel_1=StringVar(u_p_1_1,value=user_tel[test_id])
        mail_1=StringVar(u_p_1_1,value=user_ema[test_id])
        pass_1=StringVar(u_p_1_1,value=user_pass[test_id])
        pass_2=StringVar(u_p_1_1,value=user_pass[test_id])
        
        user_1_1_p.tb_name=Entry(u_p_1_1,textvariable=name_1)
        user_1_1_p.tb_name.place(x=320, y=20)
        user_1_1_p.tb_surname=Entry(u_p_1_1,textvariable=name_2)
        user_1_1_p.tb_surname.place(x=320, y=60)
        user_1_1_p.tb_tel=Entry(u_p_1_1,textvariable=tel_1)
        user_1_1_p.tb_tel.place(x=320, y=100)
        user_1_1_p.tb_mail=Entry(u_p_1_1,textvariable=mail_1)
        user_1_1_p.tb_mail.place(x=320, y=140)
        user_1_1_p.tb_pass_a=Entry(u_p_1_1,textvariable=pass_1,show='*')
        user_1_1_p.tb_pass_a.place(x=320, y=180)
        user_1_1_p.tb_pass_b=Entry(u_p_1_1,textvariable=pass_2,show='*')
        user_1_1_p.tb_pass_b.place(x=320, y=220)

        Button(u_p_1_1, text='Back to Menu', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_user_main).place(x=40, y=280)
        Button(u_p_1_1, text='Save The Changes', bg='#F0F8FF', font=('arial', 12, 'normal'), command=user_set).place(x=300, y=280)
    except:
        messagebox.showinfo("Warning","Your inputs are not suitable")
    u_p_1_1.mainloop()
def user_1_2_p():
    def back_user_main_2():
        u_p_1_2.destroy()
        user_1_p()
    def send_message_1():
        try:
            admins_text=message_tb.get()
            dateTimeObj = datetime.now()
            timee=dateTimeObj.strftime("%H:%M:%S.%f - %b %d %Y")
            a_m=open("messages.txt","a")
            a_m.write(str(test_id+1001))
            a_m.write("\n")
            a_m.write(timee)
            a_m.write("\n")
            a_m.write(admins_text)
            a_m.write("\n")
            a_m.close()
            messagebox.showinfo("Confirmation","Your message sent succesfully")
            u_p_1_2.destroy()
            user_1_p()
        except:
            messagebox.showinfo("Warning","Don't use unacceptable(Turkish characters etc.) character")
    u_p_1_2 = Tk()
    u_p_1_2.geometry('720x400')
    u_p_1_2.configure(background='#ffe8be')
    u_p_1_2.title('System Guild')
    
    message_tb=Entry(u_p_1_2)
    message_tb.place(x=30,y=30,relwidth=0.92,relheight=0.7)
    
    Button(u_p_1_2, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_user_main_2).place(x=30, y=340)
    Button(u_p_1_2, text='Send', bg='#F0F8FF', font=('arial', 12, 'normal'), command=send_message_1).place(x=645, y=340)
    u_p_1_2.mainloop()
def user_1_3_p():
    def we_got_a_problem():
        messagebox.showinfo("Warning","We got a problem check your inputs and try again")
    def back_user_main_2():
        u_p_1_3.destroy()
        user_1_p()
    
    u_p_1_3 = Tk()
    u_p_1_3.geometry('720x400')
    u_p_1_3.configure(background='#ffe8be')
    u_p_1_3.title('System Guild')
    def new_questo():
        global test_id
        try:
            type_cho=str(listbox_que.curselection())
            type_cho=type_cho.replace("(","")
            type_cho=type_cho.replace(")","")
            type_cho=type_cho.replace(",","")
            type_cho=int(type_cho)
            if q_t_tb.get()==None or q_e_tb.get()==None or q_r_tb.get()==None or type_cho==None or q_r_tb.get().isnumeric()!=True:
                we_got_a_problem()
            else:
                if q_r_tb.get()>user_balan[test_id]:
                    messagebox.showinfo("Warning","Your reward higher than your balance")
                else:
                    mission_dt=open("mission_dt.txt","r")
                    need=mission_dt.readline()
                    mission_num=int(need.replace("\n",""))
                    mission_dt.close()
                    mission_num+=1
                    mission_id.append(mission_num+9999)
                    mission_type.append(type_cho+1)
                    mission_boss.append(test_id+1001)
                    mission_title.append(q_t_tb.get())
                    mission_explanation.append(q_e_tb.get())
                    mission_reward.append(q_r_tb.get())
                    mission_worker.append("-1")
                    need_int=int(user_balan[int(test_id)])
                    need_int-=int(q_r_tb.get())                    
                    user_balan[int(test_id)]=str(need_int)
                    user_set_new()
                    mission_set()
                    messagebox.showinfo("Confirmation","Your mission added")
                    u_p_1_3.destroy()
                    user_1_p()
        except:
            we_got_a_problem()
    def getListboxValue():
        mSelected = listbox_que.curselection()
        return itemSelected
    def help_que():
        messagebox.showinfo("Help Info","You must fill in all the blanks\nIn Quest type select one of them \nAnd final one reward textbox's input must be an integer")
    listbox_que=Listbox(u_p_1_3, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
    listbox_que.insert('0', 'Software')
    listbox_que.insert('1', 'Harware')
    listbox_que.insert('2', 'Casual')
    listbox_que.insert('3', 'Special')
    listbox_que.place(x=140, y=50)
    
    Label(u_p_1_3, text='Quest Type:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=50)
    Label(u_p_1_3, text='Quest Title:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=260, y=50)
    Label(u_p_1_3, text='Quest Explanation:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=180)
    Label(u_p_1_3, text='Quest Reward:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=260, y=80)

    q_t_tb=Entry(u_p_1_3)
    q_t_tb.place(x=410, y=53)
    q_e_tb=Entry(u_p_1_3)
    q_e_tb.place(x=200, y=183,relwidth=0.65,relheight=0.3)
    q_r_tb=Entry(u_p_1_3)
    q_r_tb.place(x=410, y=83)
    
    Button(u_p_1_3, text='Help', bg='#F0F8FF', font=('arial', 12, 'normal'), command=help_que).place(x=620, y=53)
    Button(u_p_1_3, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_user_main_2).place(x=40, y=340)
    Button(u_p_1_3, text='Create a New Quest', bg='#F0F8FF', font=('arial', 12, 'normal'), command=new_questo).place(x=515, y=340)
    u_p_1_3.mainloop()
def user_1_4_p():
    u_p_1_4 = Tk()
    u_p_1_4.geometry('720x400')
    u_p_1_4.configure(background='#ffe8be')
    u_p_1_4.title('System Guild')
    global aa
    aa=0
    sel_que=Entry(u_p_1_4)
    sel_que.place(x=520,y=53,relwidth=0.22)
    qwe=0
    def quest_info():
        global using_number
        global hardness
        qu_in_pa=""
        try:
            quest_pano_in=Label(u_p_1_4,text=qu_in_pa,justify=LEFT,anchor='w')
            quest_pano_in.place(x=330, y=140,relwidth=0.49,relheight=0.475)
            if len(str(sel_que.get()))>1 and sel_que.get().isnumeric()==True:
                using_number=int(sel_que.get())-10000
                u_n_2=int(mission_boss[using_number])-1001
                exp_txt=mission_explanation[using_number]
                for i in range(35,len(exp_txt),+70):
                    exp_txt = exp_txt[:i]+"\n "+exp_txt[i:]
                hardness=int(mission_reward[using_number])
                hardness-=200
                hardness*=2
                if hardness<0:
                    hardness=0
                qu_in_pa=qu_in_pa+" Quest Giver's Number:\t"
                qu_in_pa=qu_in_pa+user_tel[u_n_2]
                qu_in_pa=qu_in_pa+"\n Quest Giver's E-Mail:\t"
                qu_in_pa=qu_in_pa+user_ema[u_n_2]
                qu_in_pa=qu_in_pa+"\n Quest Title:\t\t"
                qu_in_pa=qu_in_pa+mission_title[using_number]
                qu_in_pa=qu_in_pa+"\n Quest Explanation:\t"
                qu_in_pa=qu_in_pa+exp_txt
                qu_in_pa=qu_in_pa+"\n Quest Reward:\t\t"
                qu_in_pa=qu_in_pa+mission_reward[using_number]
                qu_in_pa=qu_in_pa+"\n Quest Requirements:\t"
                qu_in_pa=qu_in_pa+str(hardness)
                quest_pano_in=Label(u_p_1_4,text=qu_in_pa,justify=LEFT,anchor='w')
                quest_pano_in.place(x=330, y=140,relwidth=0.49,relheight=0.475)
            else:
                if qwe==1:
                    messagebox.showinfo("Warning","Your input is not suitable try again")
        except:
            messagebox.showinfo("Warning","Your input is not suitable try again")
    quest_info()
    qwe=1
    def take_quest():
        global hardness
        global using_number
        try:
            if mission_boss[using_number]==test_id:
                messagebox.showinfo("Warning","You can't take the task you created yourself")
            else:
                capability=0
                if int(mission_type[using_number])==1:
                    if hardness<=int(user_soft[test_id]):
                        capability=1
                elif int(mission_type[using_number])==2:
                    if hardness<=int(user_hard[test_id]):
                        capability=1
                elif int(mission_type[using_number])==3:
                    if hardness<=int(user_casu[test_id]):
                        capability=1
                else:
                    if hardness<=int(user_spe[test_id]):
                        capability=1
                if capability==1:
                    enough_a=int(test_id)+1001
                    mission_worker[using_number]=str(enough_a)
                    mission_set()
                    messagebox.showinfo("Confirmation","Your process has been done successfully")
                else:
                    messagebox.showinfo("Warning","Your rank is not enough for this quest")
        except:
            messagebox.showinfo("Warning","Your inputs are not suitable")
    def back_user_main_4():
        u_p_1_4.destroy()
        user_1_p()
    def board_change():
        global aa
        global board_text
        board_text=""
        if aa==0:
            board_text=board_text+" SOFTWARE\n\n"
        elif aa==1:
            board_text=board_text+" HARDWARE\n\n"
        elif aa==2:
            board_text=board_text+" CASUAL\n\n"
        else:
            board_text=board_text+" SPECIAL\n\n"
        for i in range(len(mission_id)):
            aa+=1
            print(aa)
            if int(mission_type[i])==(aa) and int(mission_worker[i])==-1:
                board_text=board_text+" Mission id:\t"
                board_text=board_text+str(mission_id[i])
                board_text=board_text+"\n"
                board_text=board_text+" Mission Title:\t"
                board_text=board_text+str(mission_title[i])
                board_text=board_text+"\n"
                board_text=board_text+" Mission Reward:\t"
                board_text=board_text+str(mission_reward[i])
                board_text=board_text+"\n"
                board_text=board_text+"\n"
            aa-=1
        aa+=1
        aa=aa%4
        quest_pano_tb=Label(u_p_1_4,text=board_text,justify=LEFT,anchor='w')
        quest_pano_tb.place(x=40, y=50,relwidth=0.38,relheight=0.7)
    board_change()
    
    Label(u_p_1_4, text='Quests:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=20)
    Label(u_p_1_4, text='Quest id:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=420, y=50)
    

    Button(u_p_1_4, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_user_main_4).place(x=40, y=340)
    Button(u_p_1_4, text='Change the Quest Board', bg='#F0F8FF', font=('arial', 12, 'normal'), command=board_change).place(x=127, y=340)
    
    Button(u_p_1_4, text='About Quest', bg='#F0F8FF', font=('arial', 12, 'normal'), command=quest_info).place(x=580, y=90)
    Button(u_p_1_4, text='Take Quest', bg='#F0F8FF', font=('arial', 12, 'normal'), command=take_quest).place(x=587, y=340)

    u_p_1_4.mainloop()
def user_1_5_p():
    global test_id
    global full_quest_txt
    full_quest_txt=""
    def back_to_u_m_t():
        u_p_1_5.destroy()
        user_1_p()
    def quest_comp():
        global u_n_2_d
        global u_n_2_c
        global using_number_c
        global hardnesss
        if test_id != int(mission_boss[using_number_c])-1001:
            messagebox.showinfo("Warning","If you are not employer you can not do this")
        else:
            if u_n_2_d==-1:
                messagebox.showinfo("Warning","Pending quests can not complete")
            else:
                ne_in_1=int(user_balan[u_n_2_d])
                ne_in_2=int(mission_reward[using_number_c])
                ne_in_1+=int(ne_in_2)
                user_balan[u_n_2_d]=str(ne_in_1)
                qu_ty=int(mission_type[using_number_c])
                if qu_ty==1:
                    rank_int=int(user_soft[u_n_2_d])
                    rank_int+=int(hardnesss/2)
                    user_soft[u_n_2_d]=str(rank_int)
                elif qu_ty==2:
                    rank_int=int(user_hard[u_n_2_d])
                    rank_int+=int(hardnesss/2)
                    user_hard[u_n_2_d]=str(rank_int)
                elif qu_ty==3:
                    rank_int=int(user_casu[u_n_2_d])
                    rank_int+=int(hardnesss/2)
                    user_casu[u_n_2_d]=str(rank_int)
                else:
                    rank_int=int(user_spe[u_n_2_d])
                    rank_int+=int(hardnesss/2)
                    user_spe[u_n_2_d]=str(rank_int)
                mission_worker[using_number_c]=-2
                user_set_new()
                mission_set()
                messagebox.showinfo("Confirmation","Your process has been done successfully")
    def quest_canc():
        global u_n_2_d
        global u_n_2_c
        global using_number_c
        global hardnesss
        if test_id != int(mission_boss[using_number_c])-1001 and test_id != int(mission_worker[using_number_c])-1001:
            messagebox.showinfo("Warning","If you are not employer/employee you can not do this")
        elif test_id == int(mission_worker[using_number_c])-1001:
            mission_worker[using_number_c]=-1
            mission_set()
            messagebox.showinfo("Canfirmation","Your process has been done successfully")
        else:
            if u_n_2_d==-1:
                ne_in_1_b=int(user_balan[u_n_2_c])
                ne_in_2_b=int(mission_reward[using_number_c])
                ne_in_1_b+=int(ne_in_2_b)
                user_balan[u_n_2_c]=str(ne_in_1_b)
                mission_worker[using_number_c]=-2
                user_set_new()
                mission_set()
                messagebox.showinfo("Confirmation","Your process has been done successfully")
            else:
                ne_in_1_b=int(user_balan[u_n_2_c])
                ne_in_2_b=int(user_balan[u_n_2_d])
                ne_in_3_b=int(mission_reward[using_number_c])
                ne_in_1_b+=int(ne_in_3_b/2)
                ne_in_2_b+=int(ne_in_3_b/2)
                user_balan[u_n_2_c]=str(ne_in_1_b)
                user_balan[u_n_2_d]=str(ne_in_2_b)
                mission_worker[using_number_c]=-2
                user_set_new()
                mission_set()
                messagebox.showinfo("Confirmation","Your process has been done successfully\nBut don't forget you paid penalty money to employee")
    def quest_info_my():
        try:
            global full_quest_txt
            global u_n_2_c
            global u_n_2_d
            global using_number_c
            global hardnesss
            full_quest_txt=""
            using_number_c=int(quest_id_tb.get())-10000
            u_n_2_c=int(mission_boss[using_number_c])-1001
            u_n_2_d=int(mission_worker[using_number_c])-1001
            if u_n_2_d<-2:
                u_n_2_d+=1001
            exp_txt_c=mission_explanation[using_number_c]
            for i in range(27,len(exp_txt_c),+60):
                exp_txt_c = exp_txt_c[:i]+"\n "+exp_txt_c[i:]
            hardnesss=int(mission_reward[using_number_c])
            hardnesss-=200
            hardnesss*=2
            if hardnesss<0:
                hardnesss=0
            full_quest_txt=full_quest_txt+" Quest Giver's id:\t\t"
            full_quest_txt=full_quest_txt+user_id[u_n_2_c]
            full_quest_txt=full_quest_txt+"\n Quest Taker's id:\t\t"
            if u_n_2_d==-1:
                full_quest_txt=full_quest_txt+"Quest Still Pending"
                print("helooooooooo",u_n_2_d)
            elif u_n_2_d==-2:
                full_quest_txt=full_quest_txt+"Quest Over"
            else:
                full_quest_txt=full_quest_txt+user_id[u_n_2_d]
            full_quest_txt=full_quest_txt+"\n Quest Title:\t\t"
            full_quest_txt=full_quest_txt+mission_title[using_number_c]
            full_quest_txt=full_quest_txt+"\n Quest Explanation:\t"
            full_quest_txt=full_quest_txt+exp_txt_c
            full_quest_txt=full_quest_txt+"\n Quest Reward:\t\t"
            full_quest_txt=full_quest_txt+mission_reward[using_number_c]
            full_quest_txt=full_quest_txt+"\n Quest Requirements:\t"
            full_quest_txt=full_quest_txt+str(hardnesss)
            full_quest=Label(u_p_1_5,text=full_quest_txt,justify=LEFT,anchor='w')
            full_quest.place(x=380, y=140,relwidth=0.42,relheight=0.475)
        except:
            messagebox.showinfo("Warning","Input is not suitable try again")
    u_p_1_5 = Tk()
    u_p_1_5.geometry('720x400')
    u_p_1_5.configure(background='#ffe8be')
    u_p_1_5.title('System Guild')
    board_text_a=""
    
    full_quest=Label(u_p_1_5,text=full_quest_txt,justify=LEFT,anchor='w')
    full_quest.place(x=380, y=140,relwidth=0.42,relheight=0.475)
    
    for i in range(len(mission_id)):
        if (int(mission_boss[i])==int(test_id+1001) or int(mission_worker[i])==int(test_id+1001)) and int(mission_worker[i])!=-2:
            board_text_a=board_text_a+" Mission id:\t"
            board_text_a=board_text_a+str(mission_id[i])
            board_text_a=board_text_a+"\n"
            board_text_a=board_text_a+" Mission Title:\t"
            board_text_a=board_text_a+str(mission_title[i])
            board_text_a=board_text_a+"\n"
            board_text_a=board_text_a+" Mission Reward:\t"
            board_text_a=board_text_a+str(mission_reward[i])
            board_text_a=board_text_a+"\n"
            board_text_a=board_text_a+" Your Role:\t"
            if int(mission_worker[i])==int(test_id):
                board_text_a=board_text_a+"Employee"
            else:
                board_text_a=board_text_a+"Employer"
            board_text_a=board_text_a+"\n"
            board_text_a=board_text_a+"\n"
    Label(u_p_1_5, text='Your Quests:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=40, y=20)
    Label(u_p_1_5, text='Quest id:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=420, y=50)
    
    my_quest_pano_tb=Label(u_p_1_5,text=board_text_a,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
    my_quest_pano_tb.place(x=40, y=50,relwidth=0.45,relheight=0.7)
    
    quest_id_tb=Entry(u_p_1_5)
    quest_id_tb.place(x=500, y=53,relwidth=0.2)
    
    Button(u_p_1_5, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=back_to_u_m_t).place(x=40, y=340)
    Button(u_p_1_5, text='Quest Info', bg='#F0F8FF', font=('arial', 12, 'normal'), command=quest_info_my).place(x=510, y=80)
    
    Button(u_p_1_5, text='Cancel The Quest', bg='#F0F8FF', font=('arial', 12, 'normal'), command=quest_canc).place(x=380, y=340)
    Button(u_p_1_5, text='Quest Complated', bg='#F0F8FF', font=('arial', 12, 'normal'), command=quest_comp).place(x=545, y=340)
    
    u_p_1_5.mainloop()
def admin_p():
    ad_p_1 = Tk()
    ad_p_1.geometry('720x400')
    ad_p_1.configure(background='#ffe8be')
    ad_p_1.title('System Guild')
    def user_list_func():
        ad_p_1.destroy()
        admin_1_p()
    def mission_list_func():
        ad_p_1.destroy()
        admin_2_p()
    def messages_func():
        ad_p_1.destroy()
        admin_3_p()
    def a_log_out_func():
        ad_p_1.destroy()
        entry_p()
    logo=PhotoImage(file='System Guild-logos_black.png')
    logo_lb=Label(image=logo,bg='#ffe8be')
    logo_lb.place(relx=0.4,rely=0.05,relwidth=0.5,relheight=0.8)
    
    Button(ad_p_1, text='User List', bg='#F0F8FF', font=('arial', 12, 'normal'), command=user_list_func).place(x=40, y=40)
    Button(ad_p_1, text='Mission List', bg='#F0F8FF', font=('arial', 12, 'normal'), command=mission_list_func).place(x=40, y=80)
    Button(ad_p_1, text='Messages', bg='#F0F8FF', font=('arial', 12, 'normal'), command=messages_func).place(x=40, y=120)
    Button(ad_p_1, text='Log Out', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_log_out_func).place(x=40, y=300)    
    
    ad_p_1.mainloop()
def admin_1_p():
    global user_num
    global c_i
    c_i=5
    a_p_1 = Tk()
    a_p_1.geometry('720x400')
    a_p_1.configure(background='#ffe8be')
    a_p_1.title('System Guild')
    def a_back_1():
        a_p_1.destroy()
        admin_p()
    def a_u_m_i():
        us_id_a=int(a_user_tb.get())
        us_id_a-=1001
        a_user_info=""
        a_user_info=a_user_info+" User id:\t\t"
        a_user_info=a_user_info+user_id[us_id_a]
        a_user_info=a_user_info+"\n User Password:\t"
        a_user_info=a_user_info+user_pass[us_id_a]
        a_user_info=a_user_info+"\n User Name:\t"
        a_user_info=a_user_info+user_name[us_id_a]
        a_user_info=a_user_info+"\n User Surname:\t"
        a_user_info=a_user_info+user_surname[us_id_a]
        a_user_info=a_user_info+"\n User Tel Number:\t"
        a_user_info=a_user_info+user_tel[us_id_a]
        a_user_info=a_user_info+"\n User G-Mail:\t"
        a_user_info=a_user_info+user_ema[us_id_a]
        a_user_info=a_user_info+"\n User Software:\t"
        a_user_info=a_user_info+user_soft[us_id_a]
        a_user_info=a_user_info+"\n User Hardware:\t"
        a_user_info=a_user_info+user_hard[us_id_a]
        a_user_info=a_user_info+"\n User Casual:\t"
        a_user_info=a_user_info+user_casu[us_id_a]
        a_user_info=a_user_info+"\n User Special:\t"
        a_user_info=a_user_info+user_spe[us_id_a]
        a_user_info=a_user_info+"\n User Balance:\t"
        a_user_info=a_user_info+user_balan[us_id_a]
        a_user_info_lb=Label(a_p_1,text=a_user_info,justify=LEFT,anchor='w')
        a_user_info_lb.place(x=380, y=140,relwidth=0.42,relheight=0.475)
    def next_page_u():
        global c_i
        a_user_list=""
        for i in range(c_i,c_i+5,1):
            if i==int(user_num):
                c_i=-5
                break
            a_user_list=a_user_list+" User id:\t\t"
            a_user_list=a_user_list+user_id[i]
            a_user_list=a_user_list+"\n User Name:\t"
            a_user_list=a_user_list+user_name[i]
            a_user_list=a_user_list+"\n User Surname:\t"
            a_user_list=a_user_list+user_surname[i]
            a_user_list=a_user_list+"\n\n"
        user_list_pano=Label(a_p_1,text=a_user_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
        user_list_pano.place(x=40, y=50,relwidth=0.45,relheight=0.7)
        c_i=c_i+5
    a_user_list=""
    for i in range(0,5,1):
        if i>=len(user_id):
            break
        else:
            a_user_list=a_user_list+" User id:\t\t"
            a_user_list=a_user_list+user_id[i]
            a_user_list=a_user_list+"\n User Name:\t"
            a_user_list=a_user_list+user_name[i]
            a_user_list=a_user_list+"\n User Surname:\t"
            a_user_list=a_user_list+user_surname[i]
            a_user_list=a_user_list+"\n\n"
    user_list_pano=Label(a_p_1,text=a_user_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
    user_list_pano.place(x=40, y=50,relwidth=0.45,relheight=0.7)
    
    Button(a_p_1, text='Next Page', bg='#F0F8FF', font=('arial', 12, 'normal'), command=next_page_u).place(x=279, y=340)    
    Button(a_p_1, text='About', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_u_m_i).place(x=500, y=100)    
    Button(a_p_1, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_back_1).place(x=40, y=340)    
    
    Label(a_p_1, text='User id:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=410, y=60)
    
    a_user_info=""
    a_user_info_lb=Label(a_p_1,text=a_user_info,justify=LEFT,anchor='w')
    a_user_info_lb.place(x=380, y=140,relwidth=0.42,relheight=0.475)
    
    a_user_tb=Entry(a_p_1)
    a_user_tb.place(x=490, y=63,relwidth=0.2)
    
    a_p_1.mainloop()
def admin_2_p():
    a_p_2 = Tk()
    a_p_2.geometry('720x400')
    a_p_2.configure(background='#ffe8be')
    a_p_2.title('System Guild')
    
    global c_i
    mission_dt=open("mission_dt.txt","r")
    need=mission_dt.readline()
    mission_num=int(need.replace("\n",""))
    mission_dt.close()
    c_i=7
    def a_back_2():
        a_p_2.destroy()
        admin_p()
    def a_m_m_i():
        mis_id_b=int(a_mis_tb.get())
        mis_id_b-=10000
        a_mis_info=""
        a_mis_info=a_mis_info+" Quest id:\t\t"
        a_mis_info=a_mis_info+mission_id[mis_id_b]
        a_mis_info=a_mis_info+"\n Quest Employer id:\t"
        a_mis_info=a_mis_info+mission_boss[mis_id_b]
        a_mis_info=a_mis_info+"\n Quest Employee id:\t"
        if int(mission_worker[mis_id_b])==-1:
            a_mis_info=a_mis_info+"This quest is pending"
        elif int(mission_worker[mis_id_b])==-2:
            a_mis_info=a_mis_info+"This quest is completed"
        else:
            a_mis_info=a_mis_info+mission_worker[mis_id_b]
        a_mis_info=a_mis_info+"\n Quest Type:\t\t"
        if int(mission_type[mis_id_b])==1:
            a_mis_info=a_mis_info+"Software"
        elif int(mission_type[mis_id_b])==2:
            a_mis_info=a_mis_info+"Hardware"
        elif int(mission_type[mis_id_b])==3:
            a_mis_info=a_mis_info+"Casual"
        else:
            a_mis_info=a_mis_info+"Special"
        a_mis_info=a_mis_info+"\n Quest Title:\t\t"
        a_mis_info=a_mis_info+mission_title[mis_id_b]
        a_mis_info=a_mis_info+"\n Quest Explanation:\t"
        a_m_exp=mission_explanation[mis_id_b]
        for i in range(28,len(a_m_exp),+60):
            a_m_exp = a_m_exp[:i]+"\n "+a_m_exp[i:]
        a_mis_info=a_mis_info+a_m_exp
        a_mis_info=a_mis_info+"\n Quest Reward:\t\t"
        a_mis_info=a_mis_info+mission_reward[mis_id_b]
        a_mis_info_lb=Label(a_p_2,text=a_mis_info,justify=LEFT,anchor='w')
        a_mis_info_lb.place(x=380, y=140,relwidth=0.42,relheight=0.475)
    def next_page_m():
        global c_i
        a_mis_list=""
        for i in range(c_i,c_i+7,1):
            if i==len(mission_id):
                c_i=-7
                break
            a_mis_list=a_mis_list+" Quest id:\t"
            a_mis_list=a_mis_list+mission_id[i]
            a_mis_list=a_mis_list+"\n Quest Title:\t"
            a_mis_list=a_mis_list+mission_title[i]
            a_mis_list=a_mis_list+"\n\n"
        a_mis_list_pano=Label(a_p_2,text=a_mis_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
        a_mis_list_pano.place(x=40, y=50,relwidth=0.45,relheight=0.7)
        c_i=c_i+7
    a_mis_list=""
    for i in range(0,7,1):
        if i>= int(mission_num):
            break
        else:
            a_mis_list=a_mis_list+" Quest id:\t"
            a_mis_list=a_mis_list+mission_id[i]
            a_mis_list=a_mis_list+"\n Quest Title:\t"
            a_mis_list=a_mis_list+mission_title[i]
            a_mis_list=a_mis_list+"\n\n"
    a_mis_list_pano=Label(a_p_2,text=a_mis_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
    a_mis_list_pano.place(x=40, y=50,relwidth=0.45,relheight=0.7)
    
    Button(a_p_2, text='Next Page', bg='#F0F8FF', font=('arial', 12, 'normal'), command=next_page_m).place(x=279, y=340)    
    Button(a_p_2, text='About', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_m_m_i).place(x=500, y=100)    
    Button(a_p_2, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_back_2).place(x=40, y=340)    
    
    Label(a_p_2, text='Mission id:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=400, y=60)
    
    a_mis_info=""
    a_mis_info_lb=Label(a_p_2,text=a_mis_info,justify=LEFT,anchor='w')
    a_mis_info_lb.place(x=380, y=140,relwidth=0.42,relheight=0.475)
    
    a_mis_tb=Entry(a_p_2)
    a_mis_tb.place(x=490, y=63,relwidth=0.2)
    
    a_p_2.mainloop()
def admin_3_p():
    a_p_3 = Tk()
    a_p_3.geometry('720x400')
    a_p_3.configure(background='#ffe8be')
    a_p_3.title('System Guild')
    
    global c_i
    c_i=4
    def a_back_3():
        a_p_3.destroy()
        admin_p()
    def a_me_m_i():
        if a_mes_tb.get().isnumeric()==False:
            messagebox.showinfo("Warning","Your input must be numbers only")
        else:
            if int(a_mes_tb.get())<0 or int(a_mes_tb.get())>len(message_id):
                messagebox.showinfo("Warning","Your input is not suitable try again")
            else:
                a_mes_info=""
                a_mes_info=a_mes_info+" Message Time-Date:\t"
                a_mes_info=a_mes_info+message_time[int(a_mes_tb.get())]
                a_mes_info=a_mes_info+" Message From:\t\t"
                a_mes_info=a_mes_info+message_id[int(a_mes_tb.get())]
                a_mes_info=a_mes_info+" Quest Explanation:\t"
                a_m_exp=message_text[int(a_mes_tb.get())]
                for i in range(48,len(a_m_exp),+73):
                    a_m_exp = a_m_exp[:i]+"\n "+a_m_exp[i:]
                a_mes_info=a_mes_info+a_m_exp
                a_mes_info_lb=Label(a_p_3,text=a_mes_info,justify=LEFT,anchor='w')
                a_mes_info_lb.place(x=260, y=140,relwidth=0.58,relheight=0.475)
    def next_page_me():
        global c_i
        a_mes_list=""
        for i in range(c_i,c_i+4,1):
            if i>=len(message_time):
                c_i=-4
                break
            else:
                a_mes_list=a_mes_list+" Message id:\t"
                a_mes_list=a_mes_list+str(i)
                a_mes_list=a_mes_list+"\n Message Date:\t"
                a_mes_list=a_mes_list+message_time[i][18:29]
                a_mes_list=a_mes_list+"\n Message Time:\t"
                a_mes_list=a_mes_list+message_time[i][:8]
                a_mes_list=a_mes_list+"\n Message From:\t"
                a_mes_list=a_mes_list+message_id[i]
                a_mes_list=a_mes_list+"\n\n"
        if a_mes_list!="":
            a_mes_list_pano=Label(a_p_3,text=a_mes_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
            a_mes_list_pano.place(x=40, y=50,relwidth=0.28,relheight=0.7)
        c_i=c_i+4
    a_mes_list=""
    for i in range(0,4,1):
        if i>=len(message_id):
            break
        a_mes_list=a_mes_list+" Message id:\t"
        a_mes_list=a_mes_list+str(i)
        a_mes_list=a_mes_list+"\n Message Date:\t"
        a_mes_list=a_mes_list+message_time[i][18:29]
        a_mes_list=a_mes_list+"\n Message Time:\t"
        a_mes_list=a_mes_list+message_time[i][:8]
        a_mes_list=a_mes_list+"\n Message From:\t"
        a_mes_list=a_mes_list+message_id[i]
        a_mes_list=a_mes_list+"\n\n"
    a_mes_list_pano=Label(a_p_3,text=a_mes_list,justify=LEFT,anchor='w',font=('arial', 7, 'normal'))
    a_mes_list_pano.place(x=40, y=50,relwidth=0.28,relheight=0.7)
    
    Button(a_p_3, text='Next Page', bg='#F0F8FF', font=('arial', 12, 'normal'), command=next_page_me).place(x=155, y=340)    
    Button(a_p_3, text='About', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_me_m_i).place(x=450, y=100)    
    Button(a_p_3, text='Back', bg='#F0F8FF', font=('arial', 12, 'normal'), command=a_back_3).place(x=40, y=340)    
    
    Label(a_p_3, text='Message id:', bg='#ffe8be', font=('arial', 12, 'normal')).place(x=350, y=60)
    
    a_mes_info=""
    a_mes_info_lb=Label(a_p_3,text=a_mes_info,justify=LEFT,anchor='w')
    a_mes_info_lb.place(x=260, y=140,relwidth=0.58,relheight=0.475)
    
    a_mes_tb=Entry(a_p_3)
    a_mes_tb.place(x=450, y=63,relwidth=0.2)
    
    a_p_3.mainloop()
entry_p()