import xml.etree.ElementTree as et
import sqlite3
import sys

def insert(curs, first, last, prof):
    curs.execute('insert into person (first_name, last_name, profession) '
                     +'values (?, ?, ?)',
                 (first, last, prof))

if __name__=='__main__':
    # read xml file
    people = et.parse(sys.argv[1])
    # connect to database
    conn = sqlite3.connect("people.sqlite3")
    # for each person from xml file
    for person in people.findall("person"):
        # insert person into database
        insert(conn.cursor(),
               person.find("firstName").text,
               person.find("lastName").text,
               person.find("profession").text)
    conn.commit()
