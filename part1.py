#!Python 3

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

query = """create table if not exists owners (
    ID integer primary key autoincrement,
    firstName tinytext,
    lastName tinytext,
    phoneNum tinyint,
    email tinytext,
    adress tinytext,
    city tinytext,
    postalcode tinytext);"""
cursor.execute(query)

query = """create table if not exists pets (
    ID integer primary key autoincrement,
    name tinytext,
    type tinytext,
    breed tinytext,
    birthdate date,
    ownerID integer);"""
cursor.execute(query)

query = """create table if not exists visits (
    ID integer primary key autoincrement,
    ownerID integer,
    petID integer,
    details mediumtext,
    cost integer,
    paid integer);"""
cursor.execute(query)

#cursor.execute("PRAGMA table_info(Owners)")
#print(cursor.fetchall())

def addCustomer():
    fname = input("First name of new customer: ")
    lname = input("Last name of new customer: ")
    phoneNum = ''
    while not phoneNum.isdigit():
        phoneNum = input("Phone number of new customer: ")
        phoneNum = phoneNum.replace(' ','')
        phoneNum = phoneNum.replace('-','')
        phoneNum = phoneNum.replace('(','')
        phoneNum = phoneNum.replace(')','')
    phoneNum = int(phoneNum)
    email = input("Email adress of new customer: ")
    adress = input("Adress of new customer: ")
    city = input("City of new customer: ")
    postalcode = input("Postalcode of new customer: ")
    look = (f"'{lname}'",phoneNum,f"'{email}'",f"'{adress}'",f"'{city}'",f"'{postalcode}'")
    columns = ('lastName','phoneNum','email','adress','city','postalcode')
    for i in range(6):
        others = surchTalbe(look[i],'Owners',f"ID",columns[i])
        #print(others)
        if others != []:
            print(f"Customer with the same {columns[i]} of {look[i]} already exsists with IDs : ", end = '')
            for id in others:
                print(f"{id[0]} ", end='')
            con = input("\nDo you wish to add the new customer (y or n): ")
            if con == 'y':
                break
            else:
                return
    query = f"insert into owners (firstName,lastName,phoneNum,email,adress,city,postalcode) values ('{fname}','{lname}',{phoneNum},'{email}','{adress}','{city}','{postalcode}');"
    cursor.execute(query)
    #cursor.execute("select * from owners;")
    #print(cursor.fetchall())

def surchTalbe(surchIteam, table, find = "*", column = "ID"):
    query = f"select {find} from {table} where {column} = {surchIteam};"
    #print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def frontEndSurch():
    columntable = {"owners":"ID or firstName, lastName, phoneNum, email, adress, city, or postalcode","pets":"ID, name, type, breed, birthdate, ownerID","pisits":"ID, ownerID integer, petID, details, cost, paid"}
    table = input('What able would you like to surch Owners, Pets, or Visits: ').lower()
    iteam = input('What are you surching for: ')
    column = input(f"What column is '{iteam}' founf in {columntable[table]}: ")
    find = input(f"What columns would you like returned {columntable[table]}: ")
    result = surchTalbe(f"'{iteam}'", table, find, column)
    for i in result:
        print(i)

addCustomer()
connection.commit()
'''
addCustomer()
frontEndSurch()
#print(surchTalbe(1,"Owners",find='ID,phoneNum',column="phoneNum"))
'''