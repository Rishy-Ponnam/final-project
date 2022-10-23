import sqlite3
conn = sqlite3.connect("college.db")
from random import randint,randrange
from datetime import date

c = conn.cursor()

lastNames = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Johnsen","Davis","Rodrigo","Jones","Minter","Harrold","James","Petersen","Richards","Valentino","Estona","Bergara","Morris","Madej","Yang","Simons","Keltermen","Traceyt","Ali","Corfield","Habers","Ruth","Sky","Stewart","Peters"]
maleNames = ["James","John","Olajide","Micheal","Richard","David","William","DennisTheMenace","Harry","Peter","Peter","Joemama","Jack","Terry","Jimmy","Jason","Harvey","Ryan","Garold","Jacob","Nick","Ericson","Stephen","Jonathan","Larry","Justin","Scott","Frank","Fernando","Raymond","Gregory","Benjamin","Sam","Patrick","Alex"]
femaleNames = ["Mary","Patricia","Linda","Barbara","Elizabeth","Jennifer","Karen","Judy","Irene","Jane","Lori","Judy","Ruby","Lois","Tina","Emma","Olivia","Ava","Isabella","Sophia","Mia","Amelia","Charlotte","Abigail","Emily","Arlene","Maureen","Collen","Allison","Tamara","Joy","Georgia","Constance","Lillie","Claudia"]
names = [maleNames,femaleNames]
subject = ["Math","Physics","Computers","Economics","English"]
genders = ["M","W"]
students = []

for i in range(30):
    lastName = lastNames[randint(0,31)]
    gender = randint(0,1)
    firstName = names[gender][randint(0,34)]
    gender = genders[gender]
    age = randint(18,25)
    birthday = date((2001 - age), randint(1,12), randint(1,28)).isoformat()
    subject = subject[randint(0,4)]
    student = (i,firstName,lastName,birthdate,age,gender,subject)
    print(student)
    students.append(student)

c.execute('''DROP TABLE students''')

c.execute('''CREATE TABLE students
             (id integer primary key autoincrement, firstname text, lastname text, birthday text, age integer, gender text, subject text)''')

c.executemany('INSERT INTO students VALUES (?,?,?,?,?,?,?)', students)

conn.commit()

conn.close()
