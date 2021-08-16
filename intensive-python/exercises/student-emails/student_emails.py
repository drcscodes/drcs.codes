import csv

def main(args):
    with open(args[1], 'r') as fin:
        for member in csv.DictReader(fin):
            if member['Role'] == 'Student':
                fname = member['Name'].split(",")[1].strip()
                lname = member['Name'].split(",")[0].strip()
                name = "{} {}".format(fname, lname)
                print("{} <{}>".format(name, member['Email Address'].strip()))

if __name__=='__main__':
    import sys
    main(sys.argv)
