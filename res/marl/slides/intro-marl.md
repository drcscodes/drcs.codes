---
title: Introduction to Mult-Agent Reinforcement Learning
author: Christopher Simpkins
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

##


```{=latex}
\begin{center}
```
![](bishop-dl-fig2.2.pdf){height="40%"}
```{=latex}
\end{center}
```

[^DLFC2]: Follows Chapter 2 of [Deep Learning Foundations and Concepts](https://www.bishopbook.com)

## Joint Probability

:::: {.columns}
::: {.column width="60%"}

Let $X$ and $Y$ be *random* (a.k.a. *stochastic*) variables and

- $\{x_i\}_{i=1}^L$
- $\{y_j\}_{j=1}^M$
- $N$ trials in which we sample $X$ and $Y$
- $n_{ij}$ is number of trials in which $X=x_i$ and $Y=y_j$
- $c_i$ is the number of trials in which $X=x_i$, for all $y$s
- $r_j$ is the number of trials in which $Y=y_j$, for all $x$s

Then the joint probability of observing $x_i$ and $y_j$ is

$$
p(X=x_i, Y=y_j)=\frac{n_{ij}}{N}
$$

We can visualize this event with the grid diagram on the right.  Note that we're always observing events where both random variables have values, e.g., when we screen a person for cancer we're observing a joint event of two random variables: the test result and the actual existence of cancer.

:::
::: {.column width="45%"}

```{=latex}
\begin{center}
```
![](bishop-dl-fig2.4.pdf){width="100%"}
```{=latex}
\end{center}
```

:::
::::
