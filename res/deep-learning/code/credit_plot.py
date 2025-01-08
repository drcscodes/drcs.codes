#!/usr/bin/env/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def intercepts(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    m = (y2 - y1) / (x2 - x1)
    # y - y1 = m(x - x1)
    y_intercept = (m * x1) - y1
    x_intercept = ((m * x1) - y1) / m
    return [0, x_intercept], [y_intercept, 0]

def main(args):
    credit = pd.read_csv("credit.csv")
    fig, ax = plt.subplots(1, 1)
    ax.set_title("Credit Data")
    ax.set_xlim(left = 0, right = np.max(credit["age"])+10)
    ax.set_ylim(bottom = 0, top = np.max(credit["income"])+10)
    ax.set_xlabel("age")
    ax.set_ylabel("income")
    ax.scatter(x=credit[credit["approve"] == 1]["age"],
               y=credit[credit["approve"] == 1]["income"], marker="+", color="green")
    ax.scatter(x=credit[credit["approve"] == -1]["age"],
               y=credit[credit["approve"] == -1]["income"], marker="_", color="red")
    #ax.plot([0, 200], [80, 0], "-b")
    fig.savefig("credit-scatter.png")
    ax.plot([0, 144.4], [95.5, 0], "-b")
    fig.savefig("credit-scatter-separator.png")
    xs, ys = intercepts((29, 65), (73, 33))
    ax.plot([29, ], [65

if __name__=="__main__":
    main(sys.argv)
