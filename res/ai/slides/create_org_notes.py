#!/usr/bin/env python3

import argparse
import collections
import io
import os
import re
import string
import sys

template = string.Template(r"""#+TITLE: $title
#+SUBTITLE: $subtitle
#+AUTHOR: $author
#+INSTITUTE: $institute
#+EMAIL:
#+DATE:
#+DESCRIPTION: $title $subtitle
#+KEYWORDS:
#+LANGUAGE:  en
#+OPTIONS: H:2 toc:nil num:t org-image-max-width:5in org-image-align:center
#+LaTeX_COMPILER: lualatex
#+LaTeX_CLASS_OPTIONS: [smaller]
#+LaTeX_HEADER: \usepackage[margin=1in]{geometry}
#+LaTeX_HEADER: \usepackage{fontspec}
#+LaTeX_HEADER: \usepackage{verbatim, multicol, tabularx, multicol}
#+LaTeX_HEADER: \usepackage{amsmath,amsthm, amssymb, latexsym, listings, qtree}
#+LaTeX_HEADER: \lstset{frame=tb, aboveskip=1mm, belowskip=0mm, showstringspaces=false, columns=flexible, basicstyle={\scriptsize\ttfamily}, numbers=left, frame=single, breaklines=true, breakatwhitespace=true}
#+LaTeX_HEADER: \hypersetup{colorlinks=true,urlcolor=blue}
#+LaTeX_HEADER: \usepackage{polyglossia}
#+LaTeX_HEADER: \setdefaultlanguage[variant=US]{english}
""")


def make_argparser():
    parser = argparse.ArgumentParser(description='Create org-mode notes files from Pandoc Beamer md slides.')
    parser.add_argument("-f", "--input_file", dest="infile", required=True,
                        type=argparse.FileType('r', encoding='UTF-8'),
                        help="Markdown file containing Pandoc Beamer slides.")
    parser.add_argument("-o", "--output_file", dest="outfile", required=False,
                        type=argparse.FileType('w', encoding='UTF-8'),
                        default=sys.stdout,
                        help="Output file to which to write .")
    return parser

def process_header(args):
    try:
        # title, subtitle, author, institute = "", "", "", ""
        substitutions = collections.defaultdict(default_factory=lambda: "")
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
        print("ERROR: StopIteration while processing header")

def process_comment(args):
    try:
        while True:
            line = next(args.infile)
            if line.startswith("-->"):
                break
    except StopIteration:
        print("ERROR: StopIteration while processing comment")


def orgify(line):
    line = re.sub(r'^##','**', line)
    line = re.sub(r'\*\*(.+?)\*\*', r'*\1*', line)
    line = re.sub(r'!\[\]\((.+?)\)\{width="(.+?)%"\}',
                  r'#+attr_latex: :width 0.\2\\textwidth\n[[file:]1]]', line)
    line = re.sub(r'!\[\]\((.+?)\)\{height="(.+?)%"\}',
                  r'#+attr_latex: :height 0.\2\\textheight\n[[file:]1]]', line)
    return line

def main(args):
    print(f"Reading from {args.infile}")

    try:
        while True:
            line = next(args.infile)
            if line.startswith("---"):
                process_header(args)
            if line.startswith("<!--"):
                process_comment(args)
            else:
                print(orgify(line), end="", file=args.outfile)
    except StopIteration:
        print(f"Finished reading lines from {args.infile}")

    print(f"Writing to {args.outfile}")



if __name__=="__main__":
    parser = make_argparser()
    args = parser.parse_args(sys.argv[1:])
    main(args)
