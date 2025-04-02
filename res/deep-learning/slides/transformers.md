---
title: Transformers
author: CS 4277 Deep Learning
institute: Kennesaw State University
aspectratio: 1610
fontsize: 10pt
colorlinks: yes
urlcolor: blue
header-includes:
- |
  ```{=latex}
  \input{beamer-common}
  %\titlegraphic{\includegraphics[width = 1in]{chris-simpkins-headshot-320px}}
  \usepackage{framed}
  \usepackage{xcolor}
  \usepackage{tikz,pgfplots}
  \let\oldquote=\quote
  \let\endoldquote=\endquote
  \colorlet{shadecolor}{cyan!15}
  \renewenvironment{quote}{\begin{shaded*}\begin{oldquote}}{\end{oldquote}\end{shaded*}}
  ```
---

## Transformers

- Convolutional networks take advantage of the relatedness of nearby pixels in images to deal with the high dimensionality of image data.
- Text data is also high-dimensional with much redundancy that can be exploited, e.g., most instance of `dog` have the same meaning.

Problems: text sequences vary in length and cannot easily be resized.

Consider:

> - Please do not cut all my hair off.

shortened to:

> - Cut all my hair off.

## Processing Text Data

The restaurant refused to serve me a ham sandwich because it only cooks vegetarian food. In the end, they just gave me two slices of bread. Their ambiance was just as good
as the food and service.

## Dot-Product Self-Attention

Recall that NN layer $\bm{f}(\bm{x})$ takes $D \times 1$ input $\bm{x}$, applies linear transformation to input then passes result to activation function:

$$
\bm{f}(\bm{x}) = \text{ReLU}(\bm{\beta} + \bm{\Omega x})
$$

A self-attention block $\bm{sa(\cdot)}$ takes $N$ inputs.
