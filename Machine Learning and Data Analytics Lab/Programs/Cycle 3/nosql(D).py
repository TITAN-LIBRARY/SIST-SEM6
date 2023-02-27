# MongoDB
from pymongo import MongoClient
from tkinter import *
from tkinter import ttk

ws = Tk()

ws.title("Student Registration Form")
ws.geometry("400x400")
ws['bg'] = '#0ff'


def insert():
    ins = Toplevel()

    name = StringVar()
    regno = IntVar()
    mail = StringVar()
    phone = IntVar()
    tencgpa = DoubleVar()
    twncgpa = DoubleVar()
    addr = StringVar()

    ins.title("Update Window")
    ins.geometry('800x900')
    ins['bg'] = '#0A9'

    def run():
        addr = h1.get('1.0', 'end-1c')
        db = MongoClient()
        data = {'name': name.get(), "Regno": regno.get(), "Email": mail.get(), "Phoneno": phone.get(
        ), "10thCGPA": tencgpa.get(), "12thcgpa": twncgpa.get(), "Address": addr}
        student = db["student"]
        details = student["details"]
        details.insert_one(data)

        def dis(db):
            for i in db:
                print(i)
        dis(details.find())
        db.close()
        print(name.get(), regno.get(), mail.get(),
              phone.get(), tencgpa.get(), twncgpa.get(), addr)
    Label(ins, text='Registration Form', font=('Arial', 20)).grid(
        row=0, column=1, pady=20, padx=100)
    a = Label(ins, text="Name", font=('Arial', 12), width=10).grid(
        row=1, column=0, padx=10, pady=10)
    a1 = Entry(ins, width=100, textvariable=name).grid(
        row=1, column=1, padx=20, pady=30, ipady=3)

    b = Label(ins, text="Register no.", font=('Arial', 12),
              width=10).grid(row=2, column=0, padx=20, pady=30)
    b1 = Entry(ins, width=100, textvariable=regno).grid(
        row=2, column=1, padx=20, pady=30, ipady=3)

    c = Label(ins, text="Email Id.", font=('Arial', 12),
              width=10).grid(row=3, column=0, padx=20, pady=30)
    c1 = Entry(ins, width=100, textvariable=mail).grid(
        row=3, column=1, padx=20, pady=30, ipady=3)
    d = Label(ins, text="Phone No.", font=('Arial', 12),
              width=10).grid(row=4, column=0, padx=20, pady=30)
    d1 = Entry(ins, width=100, textvariable=phone).grid(
        row=4, column=1, padx=20, pady=30, ipady=3)
    e = Label(ins, text="10th CGPA", font=('Arial', 12),
              width=10).grid(row=5, column=0, padx=20, pady=30)
    e1 = Entry(ins, width=100, textvariable=tencgpa).grid(
        row=5, column=1, padx=20, pady=30, ipady=3)
    f = Label(ins, text="12th CGPA", font=('Arial', 12),
              width=10).grid(row=6, column=0, padx=20, pady=30)
    f1 = Entry(ins, width=100, textvariable=twncgpa).grid(
        row=6, column=1, padx=20, pady=30, ipady=3)
    h = Label(ins, text="Address", font=('Arial', 12), width=10).grid(
        row=7, column=0, padx=20, pady=30)
    h1 = Text(ins, width=50, height=2)
    h1.grid(row=7, column=1, padx=0, pady=5)

    ttk.Button(ins, text="Submit", command=run).grid(
        row=8, column=1, pady=5, ipady=0, ipadx=2)
    ins.mainloop()


def display():
    det = Toplevel()
    det.title("DISPLAY Window")
    det.geometry('800x800')
    det['bg'] = '#0A9'
    Label(det, text='Database', font=('Arial', 20)).grid(
        row=0, column=1, pady=20)

    tb = Text(det, width=50, height=30, background="#fff")
    tb.grid(row=1, column=1, pady=10, padx=20)
    try:
        db = MongoClient()
        student = db["student"]
        details = student["details"]

        def dis(db):
            for i in db:
                tb.insert(INSERT, '{\n')
                for j in i.items():
                    tb.insert(INSERT, str(' '*3)+str(j)+'\n')
                tb.insert(INSERT, '}\n')

        dis(details.find())
        db.close()
    except:
        tb.insert(INSERT, "DISPLAY FAILED\n")
        db.close()
    det.mainloop()


def delete():
    det = Toplevel()
    regno = IntVar()

    def run():
        try:
            db = MongoClient()
            student = db["student"]
            details = student["details"]
            details.delete_one({'Regno': regno.get()})
            tb.insert(INSERT, "DELETED Successfully\n")
            db.close()
        except:
            tb.insert(INSERT, "DELETION FAILED\n")
    det.title("Update Window")
    det.geometry('800x800')
    det['bg'] = '#0A9'
    Label(det, text='Delete Form', font=('Arial', 20)).grid(
        row=0, column=1, pady=20)

    a = Label(det, text="Register no.", font=('Arial', 12),
              width=10).grid(row=1, column=0, padx=20, pady=30)
    a1 = Entry(det, width=50, textvariable=regno).grid(
        row=1, column=1, padx=20, pady=30, ipady=3)
    ttk.Button(det, text="Submit", command=run).grid(
        row=8, column=1, pady=10, ipady=5, ipadx=2)
    tb = Text(det, width=30, height=5, background="#fff")
    tb.grid(row=9, column=1, pady=10)
    det.mainloop()


labeltit = Label(text='Registration Options', font=20)
labeltit.pack(side=TOP, pady=30)

runblc = Button(ws, text='INSERT', width=20, height=2, command=insert)
runblc.pack(side=TOP, pady=10)

rnveblc = Button(ws, text='DISPLAY', width=20, height=2, command=display)
rnveblc.pack(side=TOP, pady=10)

deletebttn = Button(ws, text='DELETE', width=20, height=2, command=delete)
deletebttn.pack(side=TOP, pady=10)

button_exit = Button(ws, text="Exit", command=exit, width=20, height=2)

button_exit.pack(side=TOP, padx=10)

ws.mainloop()
