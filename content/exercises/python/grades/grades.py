from pprint import pprint
import statistics as stats

super_grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]

def aslists(grades):
    gdict = {}
    for line in grades[1:]:
        student = line[0]
        gs = []
        for g in line[1:]:
            gs.append(float(g))
        gdict[student] = gs
    return gdict

def asdicts(grades):
    gdict = {}
    for line in grades[1:]:
        student = line[0]
        gs = {}
        for i, g in enumerate(line[1:]):
            label = grades[0][i + 1]
            gs[label] = float(g)
        gdict[student] = gs
    return gdict

def stud_means(grades):
    mdict = {}
    for stud, grades in grades.items():
        mdict[stud] = stats.mean(grades)
    return mdict

def stud_means2(grades):
    return {stud: stats.mean(grades) for stud, grades in grades.items()}

if __name__ == '__main__':
    pprint(aslists(super_grades))
    pprint(asdicts(super_grades))
    pprint(stud_means(aslists(super_grades)))
    pprint(stud_means2(aslists(super_grades)))
