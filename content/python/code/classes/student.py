class Student:

    # Note that each method must have a first parameter named 'self'.
    # self is used to refer to an instance of the class from within
    # the class definition.

    # This is the class's constructor.  It is called whenever
    # you create a new object of this class.
    def __init__(self, id, name, exams):
        # If we leave off the self. on the left side, we're not
        # creating attributes, a.k.a. instance variables
        self.id = id
        self.name = name
        self.exams = exams

    # This method 'overrides' the defulat string representation
    # provided by Python.
    def __str__(self):
        # Notice that we must use self. when referring to attributes
        return 'new' + self.name + ', ' + str(self.id) + ', ' + 'Exams: ' + \
            ','.join([str(i+1) + ': ' + str(score)
                          for i, score in enumerate(self.exams)])

    def exam(self, number):
        if (number < 1) or (number > len(self.exams)):
            msg = 'Exam number must be in range [1, '+str(len(self.exams))+']'
            raise ValueError(msg)
        return self.exams[number - 1]

    def average(self):
        return sum(self.exams) / len(self.exams)

    def add_exam(self, score):
        self.exams.append(score)

    def change_score(self, exam_number, new_score):
        self.exams[exam_number] = new_score

    def adjust_score(self, exam_number, adjustment):
        exams[exam_number - 1] += adjustment

print("I'm at the top level of the student module");

if __name__=="__main__":
    print("Also top level of student,but in a __name__=='__main__' block.");
