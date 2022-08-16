from flask import Flask, request, render_template
import csv, os

app = Flask(__name__)

@app.route('/')
def index():
    courses = []
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            course_term = file.split('.')[0]
            course, term = course_term.split('_')
            courses.append((course, term))
    print(courses)
    return render_template('index.html.jinja2', courses=courses)

@app.route('/grades/<course>/<term>')
def gradebook(course, term):
    file_name = course + "_" + term + '.csv'
    rows = []
    with open(file_name, 'r') as fin:
        reader = csv.reader(fin)
        for record in reader:
            rows.append(record)
    return render_template('grades.html.jinja2', course=course, term=term, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
