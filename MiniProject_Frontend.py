#Frontend

from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

class Army:
	def __init__(self, root):
		self.root=root
		self.root.title("ARMED FORCES DBMS")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="aqua")

		Soldier_Name=StringVar()
		Soldier_ID=StringVar()
		Rank=StringVar()
		DoJ=StringVar()
		DoB=StringVar()
		DoR=StringVar()
		Battalion=StringVar()
		Gender=StringVar()

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("ARMED FORCES DBMS", "Are you sure???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtSoldier_ID.delete(0,END)
			self.txtSoldier_Name.delete(0,END)
			self.txtRank.delete(0,END)
			self.txtDoJ.delete(0,END)
			self.txtDoB.delete(0,END)
			self.txtDoR.delete(0,END)
			self.txtBattalion.delete(0,END)
			self.txtGender.delete(0,END)

		def adddata():
			if(len(Soldier_ID.get())!=0):
				MiniProject_Backend.AddArmyRec(Soldier_ID.get(),Soldier_Name.get(),Rank.get(),DoJ.get(),DoB.get(),DoR.get(),Battalion.get(),Gender.get())
				ArmyList.delete(0,END)
				ArmyList.insert(END,(Soldier_ID.get(),Soldier_Name.get(),Rank.get(),DoJ.get(),DoB.get(),DoR.get(),Battalion.get(),Gender.get()))

		def disdata():
			ArmyList.delete(0,END)
			for row in MiniProject_Backend.ViewArmyData():
				ArmyList.insert(END, row, str(""))

		def armyrec(event):
			global sd
			searcharmy=ArmyList.curselection()[0]
			sd=ArmyList.get(searcharmy)

			self.txtSoldier_ID.delete(0,END)
			self.txtSoldier_ID.insert(END,sd[1])
			self.txtSoldier_Name.delete(0,END)
			self.txtSoldier_Name.insert(END,sd[2])
			self.txtRank.delete(0,END)
			self.txtRank.insert(END,sd[3])
			self.txtDoJ.delete(0,END)
			self.txtDoJ.insert(END,sd[4])
			self.txtDoB.delete(0,END)
			self.txtDoB.insert(END,sd[5])
			self.txtDoR.delete(0,END)
			self.txtDoR.insert(END,sd[6])
			self.txtBattalion.delete(0,END)
			self.txtBattalion.insert(END,sd[7])
			self.txtGender.delete(0,END)
			self.txtGender.insert(END,sd[8])

		def deldata():
			if(len(Soldier_ID.get())!=0):
				MiniProject_Backend.DeleteArmyRec(sd[0])
				clcdata()
				disdata()

		def searchdb():
			ArmyList.delete(0,END)
			for row in MiniProject_Backend.SearchArmyData(Soldier_ID.get(),Soldier_Name.get(),Rank.get(),DoJ.get(),DoB.get(),DoR.get(),Battalion.get(),Gender.get()):
				ArmyList.insert(END, row, str(""))

		def updata():
			if(len(Soldier_ID.get())!=0):
				MiniProject_Backend.DeleteArmyRec(sd[0])
			if(len(Soldier_ID.get())!=0):
				MiniProject_Backend.AddArmyRec(Soldier_ID.get(),Soldier_Name.get(),Rank.get(),DoJ.get(),DoB.get(),DoR.get(),Battalion.get(),Gender.get())
				ArmyList.delete(0,END)
				ArmyList.insert(END,(Soldier_ID.get(),Soldier_Name.get(),Rank.get(),DoJ.get(),DoB.get(),DoR.get(),Battalion.get(),Gender.get()))

		#Frames
		MainFrame=Frame(self.root, bg="aqua")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="orange", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ARMED FORCES DBMS", bg="orange", fg="green")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="orange", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="orange", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="orange", relief=RIDGE, font=('Arial', 20, 'bold'), text="Soldier Info_\n", fg="green")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="orange", relief=RIDGE, font=('Arial', 20, 'bold'), text="Soldier Details_\n", fg="green")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblSoldier _ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Soldier ID:", padx=2, pady=2, bg="orange", fg="green")
		self.lblSoldier_ID.grid(row=0, column=0, sticky=W)
		self.txtSoldier_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Soldier_ID, width=39, bg="aqua", fg="green")
		self.txtSoldier_ID.grid(row=0, column=1) 

		self.lblSoldier_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Soldier Name:", padx=2, pady=2, bg="orange", fg="green")
		self.lblSoldier_Name.grid(row=1, column=0, sticky=W) 
		self.txtSoldier_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Soldier_Name, width=39, bg="aqua", fg="green")
		self.txtSoldier_Name.grid(row=1, column=1)

		self.lblRank=Label(DFrameL, font=('Arial', 18, 'bold'), text="Rank:", padx=2, pady=2, bg="orange", fg="green")
		self.lblRank.grid(row=2, column=0, sticky=W) 
		self.txtRank=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Release_Date, width=39, bg="aqua", fg="green")
		self.txtRank.grid(row=2, column=1)

		self.lblDoJ=Label(DFrameL, font=('Arial', 18, 'bold'), text="Date of Joining:", padx=2, pady=2, bg="orange", fg="green")
		self.lblDoJ.grid(row=3, column=0, sticky=W) 
		self.txtDoJ=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Director, width=39, bg="aqua", fg="green")
		self.txtDoJ.grid(row=3, column=1)

		self.lblDoB=Label(DFrameL, font=('Arial', 18, 'bold'), text="Date of Birth:", padx=2, pady=2, bg="orange", fg="green")
		self.lblDoB.grid(row=4, column=0, sticky=W) 
		self.txtDoB=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Cast, width=39, bg="aqua", fg="green")
		self.txtDoB.grid(row=4, column=1)

		self.lblDoR=Label(DFrameL, font=('Arial', 18, 'bold'), text="Date of Retirement:", padx=2, pady=2, bg="orange", fg="green")
		self.lblDoR.grid(row=5, column=0, sticky=W) 
		self.txtDoR=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Budget, width=39, bg="aqua", fg="green")
		self.txtDoR.grid(row=5, column=1)

		self.lblBattalion=Label(DFrameL, font=('Arial', 18, 'bold'), text="Battalion:", padx=2, pady=2, bg="orange", fg="green")
		self.lblBattalion.grid(row=6, column=0, sticky=W) 
		self.txtBattalion=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Duration, width=39, bg="aqua", fg="green")
		self.txtBattalion.grid(row=6, column=1)

		self.lblGender=Label(DFrameL, font=('Arial', 18, 'bold'), text="Gender:", padx=2, pady=2, bg="orange", fg="green")
		self.lblGender.grid(row=7, column=0, sticky=W) 
		self.txtGender=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="aqua", fg="green")
		self.txtGender.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		ArmyList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="aqua", fg="green", yscrollcommand=sb.set)
		ArmyList.bind('<<ListboxSelect>>', armyrec)
		ArmyList.grid(row=0, column=0, padx=8)
		sb.config(command=ArmyList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=Army(root)
	root.mainloop()
