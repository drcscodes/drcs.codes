import sqlite3
import xml.etree.ElementTree as et

def insert_person(conn, first_name, last_name, profession):
    curs = conn.cursor()
    curs.execute("insert into person (first_name, last_name, profession) values (?, ?, ?)",
      (first_name, last_name, profession))
    conn.commit()

def person_from_element(element):
    first = element.find('firstName').text
    last = element.find('lastName').text
    prof = element.find('profession').text
    return first, last, prof

if __name__=="__main__":
    conn = sqlite3.connect('people.sqlite3')
    people = et.parse('people.xml')
    for element in people.findall("person"):
        first, last, prof = popdb.person_from_element(element)
        popdb.insert_person(conn, first, last, prof)

