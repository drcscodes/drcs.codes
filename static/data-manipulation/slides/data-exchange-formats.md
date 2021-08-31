#+TITLE: Data Exchange Formats
#+AUTHOR: Data Manipulation in Python
#+EMAIL:
#+DATE:
#+DESCRIPTION:
#+KEYWORDS:
#+LANGUAGE:  en
#+OPTIONS: H:2 toc:nil num:t
#+BEAMER_FRAME_LEVEL: 2
#+COLUMNS: %40ITEM %10BEAMER_env(Env) %9BEAMER_envargs(Env Args) %4BEAMER_col(Col) %10BEAMER_extra(Extra)
#+LaTeX_CLASS: beamer
#+LaTeX_CLASS_OPTIONS: [smaller]
#+LaTeX_HEADER: \usepackage{verbatim, multicol, tabularx,}
#+LaTeX_HEADER: \usepackage{amsmath,amsthm, amssymb, latexsym, listings, qtree}
#+LaTeX_HEADER: \lstset{frame=tb, aboveskip=1mm, belowskip=0mm, showstringspaces=false, columns=flexible, basicstyle={\scriptsize\ttfamily}, numbers=left, frame=single, breaklines=true, breakatwhitespace=true}
#+LaTeX_HEADER: \setbeamertemplate{footline}[frame number]
#+LaTeX_HEADER: \hypersetup{colorlinks=true,urlcolor=blue}
#+LaTeX_HEADER: \logo{\includegraphics[height=.75cm]{GeorgiaTechLogo-black-gold.png}}

* Data Exchange Formats

** Data Exchange Formats

- XML

  - A verbose textual representation of trees

- JSON

  - JavaScript Object notation -- like a Python ~dict~

** XML Format

[[../code/structured-files][people.xml]]:

#+BEGIN_SRC xml
<?xml version="1.0"?>

<people>
  <person>
    <firstName>Alan</firstName>
    <lastName>Turing</lastName>
    <professions>
      <profession>Computer Scientist</profession>
      <profession>Mathematician</profession>
      <profession>Computer Scientist</profession>
      <profession>Cryptographer</profession>
    </professions>
  </person>
  <person>
    <firstName>Stephen</firstName>
    <lastName>Hawking</lastName>
    <professions>
      <profession>Physicist</profession>
      <profession>Comedian</profession>
    </professions>
  </person>
</people>
#+END_SRC

** Parsing XML with ElementTree

Use Python's built-in [[https://docs.python.org/3/library/xml.etree.elementtree.html][ElementTree API]]


#+BEGIN_SRC python
In [17]: import xml.etree.ElementTree as ET

In [18]: root = ET.parse('people.xml')

In [21]: persons = root.findall("person")

In [24]: for person in persons:
    ...:     print(person.find("firstName").text, end="")
    ...:     print(person.find("lastName").text)
    ...:     for profession in person.find("professions"):
    ...:         print("\t", profession.text)
    ...:
AlanTuring
	 Computer Scientist
	 Mathematician
	 Computer Scientist
	 Cryptographer
StephenHawking
	 Physicist
	 Comedian
#+END_SRC

** JSON Format

Just like Python data structures except:

- double quotes -- " -- for all strings
- ~true~ and ~false~ boolean literals instead of ~True~ and ~False~
- ~null~ instead of ~None~

Here's the XML people example represented as JSON:

#+BEGIN_SRC python
{
  "people": {
    "person": [
      {
        "firstName": "Alan",
        "lastName": "Turing",
        "professions": {
          "profession": ["Computer Scientist", "Mathematician",
                         "Computer Scientist", "Cryptographer"]
         }
       },
       {
         "firstName": "Stephen",
         "lastName": "Hawking",
         "professions": {
           "profession": ["Physicist", "Comedian"]
         }
       }
    ]
  }
}
#+END_SRC

** Reading JSON

Use Python's built-in [[https://docs.python.org/3/library/json.html][JSON encoder and decoder]]

- Loading from a string:

#+BEGIN_SRC python
In [2]: json.loads('{"CS4400": ["CS1301","CS1315","CS1371"], "CS3600":["CS1332"]}')
Out[2]: {'CS3600': ['CS1332'], 'CS4400': ['CS1301', 'CS1315', 'CS1371']}
#+END_SRC

- Loading from a file (notice that you must provide a file object, not just a file name):

#+BEGIN_SRC python
In [8]: cat fall2017-breaks.json
{
    "2017-09-04": "Labor Day",
    "2017-10-09": "Fall Student Recess",
    "2017-10-09": "Fall Student Recess",
    "2017-11-22": "Student Recess",
    "2017-11-23": "Thanksgiving Break",
    "2017-11-24": "Thanksgiving Break"
}

In [9]: json.load(open('fall2017-breaks.json'))
Out[9]:
{'2017-09-04': 'Labor Day',
 '2017-10-09': 'Fall Student Recess',
 '2017-11-22': 'Student Recess',
 '2017-11-23': 'Thanksgiving Break',
 '2017-11-24': 'Thanksgiving Break'}
#+END_SRC

** Writing JSON

- Dumping to a string

#+BEGIN_SRC python
In [11]: prereqs = {'CS3600': ['CS1332'], 'CS4400': ['CS1301', 'CS1315', 'CS1371']}

In [12]: json.dumps(prereqs)
Out[12]: '{"CS3600": ["CS1332"], "CS4400": ["CS1301", "CS1315", "CS1371"]}'
#+END_SRC

- Dumping to a file (notice the write-mode file object):

#+BEGIN_SRC python
In [14]: json.dump(prereqs, open('prereqs.json', 'wt'))

In [15]: cat prereqs.json
{"CS3600": ["CS1332"], "CS4400": ["CS1301", "CS1315", "CS1371"]}
#+END_SRC
