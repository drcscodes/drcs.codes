import sqlite3
import xml.etree.ElementTree

def insert_person(db_conn, first_name, last_name, profession):
    curs = db_conn.cursor()
    curs.execute("insert into person (first_name, last_name, profession) values (?, ?, ?)",
                 (first_name, last_name, profession))
    db_conn.commit()

def person_data_from_element(element):
    first = element.find("firstName").text
    last = element.find("lastName").text
    profession = element.find("profession").text
    return first, last, profession

if __name__ == "__main__":
    conn = sqlite3.connect("people.sqlite3")
    people = xml.etree.ElementTree.parse("people.xml")
    persons = people.findall("person")
    for element in persons:
        first, last, profession = person_data_from_element(element)
        insert_person(conn, first, last, profession)

