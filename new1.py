from tkinter import *
from tkinter import messagebox
root = Tk()
index=0
root.title("IPL")

def addrecord(event):
	global index
	file=open('textfile.txt','a')
	file.write(entry1.get()+'\t'+entry2.get()+'\t'+entry3.get()+'\t'+entry4.get()+'\t'+entry5.get()+'\t'+entry6.get()+'\n')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	messagebox.showinfo('Alert','Team added!')
	file.close()

def removerecord(event):
	file=open('textfile.txt','r')
	lines=file.readlines()
	file.close()
	file=open('textfile.txt','w')
	for line in lines:
		com=line.split()
		if com[0]!=entry1.get():
			file.write(line)
	messagebox.showinfo('Alert','Team deleted!')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.close()


def updaterecord(event):
	file=open('textfile.txt','r')
	lines=file.readlines()
	file.close()
	file=open('textfile.txt','w')
	for line in lines:
		com=line.split()
		if com[0]==entry1.get():
			file.write(entry1.get()+'\t'+entry2.get()+'\t'+entry3.get()+'\t'+entry4.get()+'\t'+entry5.get()+'\t'+entry6.get()+'\n')
			messagebox.showinfo('Title','Team updated')
		else:
			file.write(line)
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.close()

def nextrecord(event):
	file=open('textfile.txt','r')
	global index
	index=index+1
	file.seek(index)
	try:
		c=file.readlines()
		xyz = c[index]
		l=list(xyz.split())
		entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
		entry1.insert(0,l[0]);entry2.insert(0,l[1]);entry3.insert(0,l[2]);entry4.insert(0,l[3]);entry5.insert(0,l[4]);entry6.insert(0,l[5]);
	except:
		messagebox.showinfo("Title", "")
	file.close()


def prevrecord(event):
	file=open('textfile.txt','r')
	global index
	index=index-1
	
	try:
		file.seek(index)
		c=file.readlines()
		xyz = c[index]
		l=list(xyz.split())
		entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
		entry1.insert(0,l[0]);entry2.insert(0,l[1]);entry3.insert(0,l[2]);entry4.insert(0,l[3]);entry5.insert(0,l[4]);entry6.insert(0,l[5]);
	except:
		messagebox.showinfo("Title", "no more records")
	file.close()

def reset(event):
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');


def firstrecord(event):
	file=open('textfile.txt','r')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.seek(0)
	k=file.readline()
	k=k.split()
	entry1.insert(0,k[0]);entry2.insert(0,k[1]);entry3.insert(0,k[2]);entry4.insert(0,k[3]);entry5.insert(0,k[4]);entry6.insert(0,k[5]);
	file.close()

def lastrecord(event):
	file=open('textfile.txt','r')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	for i in file:
		k=i
	k=k.split()
	entry1.insert(0,k[0]);entry2.insert(0,k[1]);entry3.insert(0,k[2]);entry4.insert(0,k[3]);entry5.insert(0,k[4]);entry6.insert(0,k[5]);
	file.close()
	
label1=Label(root,text='Sno')
label1.grid(row=6,column=0)

label2=Label(root,text='Team Name')
label2.grid(row=7,column=0)

label3=Label(root,text='Total Matches')
label3.grid(row=8,column=0)

label4=Label(root,text='Won')
label4.grid(row=9,column=0)

label5=Label(root,text='Lost')
label5.grid(row=10,column=0)

label6=Label(root,text='Points')
label6.grid(row=11,column=0)

entry1=Entry(root)
entry1.grid(row=6,column=2)

entry2=Entry(root)
entry2.grid(row=7,column=2)

entry3=Entry(root)
entry3.grid(row=8,column=2)

entry4=Entry(root)
entry4.grid(row=9,column=2)

entry5=Entry(root)
entry5.grid(row=10,column=2)

entry6=Entry(root)
entry6.grid(row=11,column=2)

button1=Button(root,text='Add team')
button1.bind('<Button-1>',addrecord)
button1.grid(row=12,column=0)

button2=Button(root,text='Remove team')
button2.bind('<Button-1>',removerecord)
button2.grid(row=12,column=1)



button4=Button(root,text='Update team')
button4.bind('<Button-1>',updaterecord)
button4.grid(row=12,column=2)

button5=Button(root,text='>')
button5.bind('<Button-1>',nextrecord)
button5.grid(row=13,column=2)

button6=Button(root,text='<')
button6.bind('<Button-1>',prevrecord)
button6.grid(row=13,column=1)


button7=Button(root,text='>>')
button7.bind('<Button-1>',lastrecord)
button7.grid(row=13,column=3)

button8=Button(root,text='<<')
button8.bind('<Button-1>',firstrecord)
button8.grid(row=13,column=0)

button9=Button(root,text='Reset')
button9.bind('<Button-1>',reset)
button9.grid(row=12,column=3)



root.mainloop()
	
