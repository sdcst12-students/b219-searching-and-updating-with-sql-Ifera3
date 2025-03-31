#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

def changeData(id,updateColum,newData,table='owners'): # defalt table is owners, changes data at specifide ID
    query = f"UPDATE {table} SET {updateColum} = '{newData}' WHERE id = {id};"
    cursor.execute(query)

def lookForOwner(serchColum,serchData): # prints all entrys that mach given data
    query = f"SELECT * FROM owners WHERE {serchColum} = '{serchData}';"
    cursor.execute(query)
    result = cursor.fetchall()
    for entry in result: #iterats throgh results
        print(f"ID         : {entry[0]}\nFirst Name : {entry[1]}\nLast Name  : {entry[2]}\nPhone Num  : ({str(entry[3])[0:3]}) {str(entry[3])[3:6]}-{str(entry[3])[6:10]}\nEmail      : {entry[4]}\nAdress     : {entry[5]}\nCity       : {entry[6]}\nPostal Code: {entry[7]}\n")

def interFace():
    id = 0
    enterID = ''
    while enterID != "A" and enterID != "B":# only excepts A or B
        enterID = input("A: enter ID    B: Find ID from other Owner info\n>") # dose the user know the ID
        enterID = enterID.capitalize()
        enterID = enterID.strip()
    if enterID == 'A':# enter known ID
        while not enterID.isdigit():
            enterID = input("Enter the ID\n>")
        id = int(enterID)
    elif enterID == 'B':# Find unknown ID from Known info
        colum = ''
        while colum != "A" and colum != "B" and colum != "C" and colum != "D" and colum != "E" and colum != "F" and colum != "G":
            colum = input("what type of info are you surching? A: First Name B: Last Name C: Phone Number D: Email E: Adress F: City G: Postalcode\n>")
            colum = colum.capitalize()
            colum = colum.strip()
        # firstName, lastName, phoneNum, email, adress, city, or postalcode
        if colum == "A":
            colum = "firstName"

interFace()
"""
changeData(1,"firstName","T")
lookForOwner('firstName',"T")
query = 'SELECT * FROM owners;'
cursor.execute(query)
print(cursor.fetchall())
"""