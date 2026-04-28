#!/usr/bin/env python3

import argparse
import os
import sys


def make_argparser():
    parser = argparse.ArgumentParser(description='Create org-mode notes files from Pandoc Beamer md slides.')
    parser.add_argument("-f", "--input_file", dest="infile", required=True,
                        help="Markdown file containing Pandoc Beamer slides.")
    parser.add_argument("-o", "--output_file", dest="outfile", required=False,
                        help="Output file to which to write .")
    return parser


def main(args):
    args.template_file = os.path.join(args.template_dir,
                                      "syllabus-template.html.jinja2")
    args.output = f"{args.prefix}syllabus.html"
    print(f"Writing syllabus to {args.output}")
    render_syllabus.main(args)

    args.template_file = os.path.join(args.template_dir,
                                      "schedule-template.html.jinja2")
    args.output = f"{args.prefix}schedule.html"
    print(f"Writing schedule to {args.output}")
    render_schedule.main(args)


if __name__=="__main__":
    parser = make_argparser()
    args = parser.parse_args(sys.argv[1:])
    main(args)
