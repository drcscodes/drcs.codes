#!/usr/bin/env python3

import argparse
import fileinput
import re
import string
import sys


template = string.Template(r"""#+TITLE: $title
#+SUBTITLE: $subtitle
#+AUTHOR: $author
#+INSTITUTE: $institute
#+EMAIL:
#+DATE: $institute
#+DESCRIPTION: $title $subtitle
#+KEYWORDS:
#+LANGUAGE:  en
#+OPTIONS: H:2 toc:nil num:t org-image-max-width:5in org-image-align:center
#+LaTeX_COMPILER: lualatex
#+LaTeX_HEADER: \usepackage[margin=1in]{geometry}
#+LaTeX_HEADER: \usepackage{fontspec}
#+LaTeX_HEADER: \usepackage{verbatim, multicol, tabularx,}
#+LaTeX_HEADER: \usepackage{amsmath, amsthm, amssymb, stmaryrd, latexsym, bm, listings, qtree}
#+LaTeX_HEADER: \usepackage{framed}
#+LaTeX_HEADER: \usepackage{xcolor,colortbl}
#+LaTeX_HEADER: \usepackage{media9}
#+LaTeX_HEADER: \usepackage[export]{adjustbox}
#+LaTeX_HEADER: \usepackage{algorithm}
#+LaTeX_HEADER: \usepackage[noend]{algpseudocode}
#+LaTeX_HEADER: \usepackage{tikz,pgfplots}
#+LaTeX_HEADER: \usetikzlibrary{shapes.geometric}
#+LaTeX_HEADER: \let\oldquote=\quote
#+LaTeX_HEADER: \let\endoldquote=\endquote
#+LaTeX_HEADER: \colorlet{shadecolor}{cyan!15}
#+LaTeX_HEADER: \renewenvironment{quote}{\begin{shaded*}\begin{oldquote}}{\end{oldquote}\end{shaded*}}
#+LaTeX_HEADER: % From https://tex.stackexchange.com/questions/7032/good-way-to-make-textcircled-numbers
#+LaTeX_HEADER: \newcommand*\circled[1]{\tikz[baseline=(char.base)]{\node[shape=circle,draw,inner sep=2pt] (char) {#1};}}
#+LaTeX_HEADER: \DeclareMathOperator*{\argmin}{arg\!min}
#+LaTeX_HEADER: \DeclareMathOperator*{\argmax}{arg\!max}
#+LaTeX_HEADER: \lstset{frame=tb, aboveskip=1mm, belowskip=0mm, showstringspaces=false, columns=flexible, basicstyle={\scriptsize\ttfamily}, numbers=left, frame=single, breaklines=true, breakatwhitespace=true}
#+LaTeX_HEADER: \hypersetup{colorlinks=true,urlcolor=blue}
#+LaTeX_HEADER: \usepackage{polyglossia}
#+LaTeX_HEADER: \setdefaultlanguage[variant=US]{english}
""")


def make_argparser():
    parser = argparse.ArgumentParser(description='Create org-mode notes files from Pandoc Beamer md slides.')
    parser.add_argument("-f", "--input_file", dest="infile", required=True,
                        type=str,
                        help="Markdown file containing Pandoc Beamer slides.")
    parser.add_argument("-o", "--output_file", dest="outfile", required=False,
                        type=argparse.FileType('w', encoding='UTF-8'),
                        default=sys.stdout,
                        help="Output file to which to write .")
    return parser

def process_header(args):
    try:
        substitutions = {} # pythonsucks = collections.defaultdict(default_factory=lambda: "")
        substitutions["title"] = "Artificial Intelligence"
        substitutions["subtitle"] = "Artificial Intelligence"
        substitutions["author"] = "Christopher Simpkins"
        substitutions["institute"] = "Kennesaw State University"
        while True:
            line = next(args.infile)
            if line.lower().startswith("title"):
                substitutions["title"] = line.split(":")[1].strip()
            if line.lower().startswith("subtitle"):
                substitutions["subtitle"] = line.split(":")[1].strip()
            if line.lower().startswith("author"):
                substitutions["author"] = line.split(":")[1].strip()
            if line.lower().startswith("institute"):
                substitutions["institute"] = line.split(":")[1].strip()
            if line.startswith("---"):
                break
        header = template.substitute(substitutions)
        print(header, end="", file=args.outfile)
    except StopIteration:
        print(f"ERROR: StopIteration in header at line {args.infile.filelineno()}: {line}", file=sys.stderr)

def process_comment(args):
    try:
        while True:
            # Consume lines without printing to output
            line = next(args.infile)
            if line.startswith("-->"):
                break
    except StopIteration:
        print(f"ERROR: StopIteration in HTML comment at line {args.infile.filelineno()}: {line}",
              file=sys.stderr)


def orgify(line):
    line = re.sub(r'^##','**', line)
    line = re.sub(r'\*\*(.+?)\*\*', r'*\1*', line)
    line = re.sub(r'`(\w+?)`', r'~\1~', line)
    line = re.sub(r'!\[\]\((.+?)\)\{width="(.+?)%"\}',
                  r'#+attr_latex: :width 0.\2\\textwidth\n[[file:\1]]', line)
    line = re.sub(r'!\[\]\((.+?)\)\{height="(.+?)%"\}',
                  r'#+attr_latex: :height 0.\2\\textheight\n[[file:\1]]', line)
    line = re.sub(r'!\[\]\((.+?)\)',
                  r'[[file:\1]]', line)
    line = re.sub(r'\[(.+?)\]\((.+?)\)',
                  r'[[\2][\1]]', line)

    if match := re.match(r'^\[.+?\]:', line):
        fn = line[:match.end()]
        note = line[match.end()+1:]
        line = f"{fn} {orgify(note.strip())}\n"
    if line.startswith(">"):
        line = f"#+begin_quote\n{line[1:]}#+end_quote\n"
    if line.startswith("```") or line.startswith(":::"):
        line = "\n"
    return line

def process_image(args, line):
    match = re.match(r'!\[(.*?)\]\((.+?)\)', line)
    alt: str = match.group(1)
    fname: str = match.group(2)

    if alt == "":
        alt = fname[:-4].replace("-", " ")

    # print(f"#+attr_latex: :alt {alt} :width 0.5\linewidth\n[[file:{fname}]]",
    #       file=args.outfile)

    if "height" in line:
        print(f"#+latex: \\includegraphics[alt={{{alt}}},height=1in]{{{fname}}}",
              file=args.outfile)
    else:
        print(f"#+latex: \\includegraphics[alt={{{alt}}},width=0.75\\linewidth]{{{fname}}}",
              file=args.outfile)


def process_latex_block(args):
    try:
        while True:
            line = next(args.infile)
            if line.startswith("```"):
                break
            elif (r"\begin{center}" in line) or (r"\end{center}" in line):
                line = "\n"
            print(line, end="", file=args.outfile)
    except StopIteration:
        print(f"ERROR: StopIteration in LaTeX code block at line {args.infile.filelineno()}: {line}", file=sys.stderr)


def process_python_block(args):
    print("#+begin_src python", file=args.outfile)
    try:
        while True:
            line = next(args.infile)
            if line.startswith("```"):
                break
            print(line, end="", file=args.outfile)
        print("#+end_src", file=args.outfile)
    except StopIteration:
        print(f"ERROR: StopIteration in Python code block at line {args.infile.filelineno()}: {line}", file=sys.stderr)


def process_equation(args):
    print(r"\begin{equation*}", file=args.outfile)
    try:
        while True:
            line = next(args.infile)
            if line.startswith("$$"):
                break
            print(line, end="", file=args.outfile)
        print(r"\end{equation*}", file=args.outfile)
    except StopIteration:
        print(f"ERROR: StopIteration in equation at line {args.infile.filelineno()}: {line}", file=sys.stderr)


def main(args):
    print(f"Reading from {args.infile}")
    try:
        while True:
            line: str = next(args.infile)
            if line.startswith("---"):
                process_header(args)
            elif line.startswith("<!--"):
                process_comment(args)
            elif line.casefold().startswith("```{=latex}"):
                process_latex_block(args)
            elif line.casefold().startswith("```python"):
                process_python_block(args)
            elif line.startswith("$$"):
                process_equation(args)
            elif line.startswith("!["):
                process_image(args, line)
            else:
                print(orgify(line), end="", file=args.outfile)
    except StopIteration:
        print(f"Finished reading lines from {args.infile}", file=sys.stderr)

    print(f"Writing to {args.outfile}")



if __name__=="__main__":
    parser = make_argparser()
    args = parser.parse_args(sys.argv[1:])
    args.infile = fileinput.FileInput(args.infile)
    main(args)
