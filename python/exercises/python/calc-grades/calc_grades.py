#!/usr/bin/env python3.6

# Note: this sample solution is written to be efficient, so it reads
# one line at a time, writes output one line at a time, and calculates
# summary averages using running sums and counts. You may find it
# easier to read the whole input file into a Python data structure and
# perform simple data structure manipulations.

import argparse
import csv
import statistics as stats
import sys

def make_argparser():
    parser = argparse.ArgumentParser(description='Calculate course grades.')
    parser.add_argument("-i", "--input-file", dest="infile", required=True,
                        help="Input CSV file containing student names and item scores.")
    parser.add_argument("-o", "--output-file", dest="outfile", required=True,
                        help="Output CSV file for score and grade calculations.")
    return parser

def calc_grade(scores):
    avg = stats.mean(scores)
    return (avg,
            "A" if avg >= 90 else
            "B" if avg >= 80 else
            "C" if avg >= 70 else
            "D" if avg >= 60 else
            "F")

if __name__=="__main__":
    parser = make_argparser()
    args = parser.parse_args(sys.argv[1:])
    with open(args.infile, 'r') as infile, open(args.outfile, 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = reader.__next__()
        header.append("Average")
        header.append("Grade")
        writer.writerow(header)
        item_sums = [0] * (len(header) - 2)
        item_counts = [0] * (len(header) - 2)
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for line in reader:
            scores = [float(score) for score in line[1:]]
            avg, grade = calc_grade(scores)
            writer.writerow(line + [f"{avg:.2f}", grade])
            item_sums = [item_sum + score for item_sum, score in zip(item_sums, scores)]
            item_counts = [count + 1 for count in item_counts]
            grade_counts[grade] = grade_counts[grade] + 1
        avg_line = ["Averages"] +\
                   [f"{(sum / count):.2f}" for sum, count in zip(item_sums, item_counts)] +\
                   ["NA"]
        writer.writerow(avg_line)
        for grade in ["A", "B", "C", "D", "F"]:
            print(f"Number of {grade}s: {grade_counts[grade]}")
        gpa = (4 * grade_counts["A"] +
               3 * grade_counts["B"] +
               2 * grade_counts["C"] +
               grade_counts["D"]) / sum(grade_counts.values())
        print(f"Class GPA: {gpa:.2f}")
