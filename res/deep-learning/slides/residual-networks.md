---
title: Residual Networks
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

## Residual Networks

- Conv nets improve by adding more layers, but only to a point

## Sequential Processing

Recall that a 3-layer network can be defined by:

```{=latex}
\begin{align*}
\bm{h}_1 &= \bm{f}_1(\bm{x}, \bm{\phi}_1)\\
\bm{h}_2 &= \bm{f}_2(\bm{h}_1, \bm{\phi}_2)\\
\bm{h}_3 &= \bm{f}_3(\bm{h}_2, \bm{\phi}_3)\\
\bm{y}   &= \bm{f}_4(\bm{h}_3, \bm{\phi}_4)
\end{align*}
```

where each $\bm{\phi}_k$ includes the weights, $\bm{\Omega}$, and biases, $\bm{\beta}$ in Layer $k$.
