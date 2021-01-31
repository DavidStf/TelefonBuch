from tkinter import *
import csv
from tkinter import messagebox

phonelist = []
def ReadCSVFile():
	global header
	with open('StudentData.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			phonelist.append(row)
	set_select()		
	print(phonelist)

def WriteInCSVFile(phonelist):
	with open('StudentData.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in phonelist:
			writeobj.writerow(row)


def WhichSelected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Bitte Name auswählen")
	else:
		return int(select.curselection()[0])
		


def AddDetail():
	if E_name.get()!="" and E_last_name.get()!="" and E_contact.get()!="":
		phonelist.append([E_name.get()+' '+E_last_name.get(),E_contact.get()])
		print(phonelist)
		WriteInCSVFile(phonelist)
		set_select()
		EntryReset()
		messagebox.showinfo("Bestätigung", "Succesfully Add New Contact")
		
	else:
		messagebox.showerror("Error", "Bitte Information eingeben")

def UpdateDetail():
	if E_name.get() and E_last_name.get() and E_contact.get():
		phonelist[WhichSelected()] = [ E_name.get()+' '+E_last_name.get(), E_contact.get()]
		WriteInCSVFile(phonelist)
		messagebox.showinfo("Bestätigung", "Erfolgreich aktualisiert")
		EntryReset()
		set_select()

	elif not(E_name.get()) and not(E_last_name.get()) and not(E_contact.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Bitte ausfüllen")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Bitte wählen sie den Namen aus und\n drücken Sie auf Load button")
		else:
			message1 = """Um die ganze Information zu laden \n 
						  wähle Load button\n.
						  """
			messagebox.showerror("Error", message1)

def EntryReset():
	E_name_var.set('')
	E_last_name_var.set('')
	E_contact_var.set('')


def DeleteEntry():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Bestätigung','Wollen Sie wirklich den Kontakt löschen\n Welcher Sie ausgewählt haben')
		if result==True:
			del phonelist[WhichSelected()]
			WriteInCSVFile(phonelist)
			set_select()
	else:
		messagebox.showerror("Error", 'Bitte Kotakt auswählen !')

def LoadEntry():
    name, phone = phonelist[WhichSelected()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in phonelist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")



#Graische Dartelung
window = Tk()
window.geometry('750x600')
window.title('Telefonbuch')
Frame1 = LabelFrame(window,text="Daten des Kontakts eingeben")
Frame1.grid(padx=55,pady=85)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)

l_name = Label(Inside_Frame1,text="Name")
l_name.grid(row=0,column=0,padx=5,pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1,width=30, textvariable=E_name_var)
E_name.grid(row=0,column=1,padx=5,pady=5)

l_last_name= Label(Inside_Frame1,text="NachName")
l_last_name.grid(row=1,column=0,padx=5,pady=5)
E_last_name_var= StringVar()
E_last_name = Entry(Inside_Frame1,width=30,textvariable=E_last_name_var)
E_last_name.grid(row=1,column=1,padx=5,pady=5)

l_contact= Label(Inside_Frame1,text="Kontact")
l_contact.grid(row=2,column=0,padx=5,pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1,width=30,textvariable=E_contact_var)
E_contact.grid(row=2,column=1,padx=5,pady=5)

Frame2 = Frame(window)
Frame2.grid(row=2,column=0,padx=15,pady=15,sticky=E)

Add_button = Button(Frame2,text="Einfügen",width=15,bg="#6B69D6",fg="#FFFFFF",command=AddDetail)
Add_button.grid(row=3,column=0,padx=8,pady=8)

Update_button = Button(Frame2,text="Ändern",width=15,bg="#6B69D6",fg="#FFFFFF",command=UpdateDetail)
Update_button.grid(row=3,column=1,padx=8,pady=8)


Reset_button = Button(Frame2,text="Zurücksetzen",width=15,bg="#6B69D6",fg="#FFFFFF",command=EntryReset)
Reset_button.grid(row=3,column=2,padx=8,pady=8)


DisplayFrame = Frame(window)
DisplayFrame.grid(row=0,column=2,padx=15,pady=0)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#282923",fg="#38d94b",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=S+W)




ActionFrame = Frame(window)
ActionFrame.grid(row=1,column=2,padx=15,pady=15,sticky=N)

Delete_button = Button(ActionFrame,text="Löschen",width=15,bg="#D20000",fg="#FFFFFF",command=DeleteEntry)
Delete_button.grid(row=1,column=2,padx=5,pady=15,sticky=S)

Loadbutton = Button(ActionFrame,text="Einblenden",width=15,bg="#6B69D6",fg="#FFFFFF",command=LoadEntry)
Loadbutton.grid(row=1,column=3,padx=5,pady=5)






ReadCSVFile()


	

window.mainloop()