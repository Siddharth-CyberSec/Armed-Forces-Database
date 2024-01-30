#backend
import sqlite3

def ArmyData():
    con=sqlite3.connect("armydb.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Soldier_ID text,Soldier_Name text,Rank text,DoJ text,DoB text,DoR text,Battalion text,Gender text)")
    con.commit()
    con.close()
    
def AddArmyRec(Soldier_ID,Soldier_Name,Rank,DoJ,DoB,DoR,Battalion,Gender):
    con=sqlite3.connect("armydb.db")   
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)",(Soldier_ID,Soldier_Name,Rank,DoJ,DoB,DoR,Battalion,Gender))
    con.commit()
    con.close()

def ViewArmyData():
    con=sqlite3.connect("armydb.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteArmyRec(id):    
    con=sqlite3.connect("armydb.db")   
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchArmyData(Soldier_ID="",Soldier_Name="",Rank="",DoJ="",DoB="",DoR="",Battalion="",Gender=""):  
    con=sqlite3.connect("armydb.db") 
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE Soldier_ID=? OR Soldier_Name=? OR Rank=? OR DoJ=? OR DoB=? OR DoR=? OR Battalion=? OR Gender=?",(Soldier_ID,Soldier_Name,Rank,DoJ,DoB,DoR,Battalion,Gender))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateArmyData(Soldier_ID="",Soldier_Name="",Rank="",DoJ="",DoB="",DoR="",Battalion="",Gender=""): 
    con=sqlite3.connect("armydb.db")   
    cur=con.cursor()
    cur.execute("UPDATE book SET Soldier_ID=?,Soldier_Name=?,Rank_Date=?,DoJ=?,DoB=?,DoR=?,Battalion=?,Gender=?, WHERE id=?",(Soldier_ID,Soldier_Name,Rank,DoJ,DoB,DoR,Battalion,Gender))
    con.commit()
    con.close()

