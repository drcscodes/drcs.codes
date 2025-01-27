---
title: Loss Functions
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

## Loss Functions

Boom!

## Maximum Likelihood

5.1

In the 1950s, Hubel and Wiesel at Johns Hopkins, experimenting on cats, discovered the hierarchical nature of neurons in the visual cortex.

```{=latex}
\begin{center}
```
![](visual-cortex-layers.png){height="70%"}[^DLI]
```{=latex}
\end{center}
```

[^DLI]: [https://www.deeplearningillustrated.com](https://www.deeplearningillustrated.com)

## Machine Vision

In 1980 Kunihiko Fukushima proposed the *Neocognitron* architecture explicitly based on neuron layers in biological vision.

```{=latex}
\begin{center}
```
![](machine-vision-timeline.png){height="60%"}[^DLI]
```{=latex}
\end{center}
```

It took the success of LeCun and Bengio's *LeNet-5*, and later Krizhevsky and Stuskever's *AlexNet* to realize the full potential of a deeply layered machine vision model and firmly establish the supremacy of Deep Learning for machine vision.
