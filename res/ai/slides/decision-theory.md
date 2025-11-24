---
title: Artificial Intelligence
subtitle: Decision Theory (AIMA 16.5-16.7)
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
    ```
---

## Syntax of Decision Networks

:::: {.columns}
::: {.column width="70%"}

- Chance nodes (ovals) represent random variables, like in Bayesian networks.

    - Agent could be uncertain about the construction cost, level of air traffic, potential for litigation, and Safety, Quietness, Frugality variables, each of which also depends on the site chosen.
    - Each chance node has a conditional distribution indexed by state of its parent nodes.
    - Parent nodes can include decision nodes and chance nodes.
    - Each current-state chance node could be part of a large Bayesian network for assessing construction costs, air traffic levels, or litigation potentials.

```{=latex}
\vspace{.1in}
```

:::
::: {.column width="35%"}

```{=latex}
\begin{center}
```
![](aima-fig-16_06-decision-network-airport-siting.pdf)
```{=latex}
\end{center}
```

:::
::::

<!-- Single column so left-aligns with content above -->

:::: {.columns}
::: {.column width="95%"}

- Decision nodes (rectangles) represent action choice points.

    - $AirportSite$ action can take a different value for each candidate site.
    - The choice influences the safety, quietness, and frugality of the solution.
    - For simple decisions, we have a single decision node.

- Utility nodes, .a.k.a. value nodes, (diamonds) represent the agent's utility function.

    - Utility node's parents are all variables describing outcomes directly affecting utility.
    - Utility node has description of the agent's utility as a function of parent attributes.
    - Description could be a tabulation of the function, or a parameterized additive or linear function of the attribute values.
    - For now, assume function is deterministic -- given values of its parent variables, value of utility node is fully determined.

:::
::: {.column width="10%"}

:::
::::

## Semantics of Decision Networks

:::: {.columns}
::: {.column width="60%"}

1. Set the evidence variables for the current state.

2. For each possible value of the decision node:

    - (a) Set the decision node to that value.
    - (b) Calculate the posterior probabilities for the parent nodes of the utility node, using a standard probabilistic inference algorithm.
    - (c) Calculate the resulting utility for the action.

3. Return the action with the highest utility.

:::
::: {.column width="45%"}

```{=latex}
\begin{center}
```
![](aima-fig-16_06-decision-network-airport-siting.pdf)
```{=latex}
\end{center}
```

:::
::::


<!--

## Simplified Decision Network for Airport Siting

```{=latex}
\begin{center}
```
![](aima-fig-16_07-decision-network-airport-siting-simplified.pdf)
```{=latex}
\end{center}
```

## Value of Information

```{=latex}
\begin{center}
```
![](aima-fig-16_08-value-of-information.pdf)
```{=latex}
\end{center}
```

## Information Gathering Agent

```{=latex}
\begin{center}
```
![](aima-fig-16_09-information-gathering-agent-algorithm.pdf)
```{=latex}
\end{center}
```

## Decision Network for Ice Cream

```{=latex}
\begin{center}
```
![](aima-fig-16_10-decision-networks-ice-cream.pdf)
```{=latex}
\end{center}
```

## Off Switch Game

```{=latex}
\begin{center}
```
![](aima-fig-16_11-off-switch-game.pdf)
```{=latex}
\end{center}
```

-->
