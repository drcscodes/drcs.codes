---
title: Artlificial Intelligence
subtitle: Planning
author: Christopher Simpkins
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

## Classical Planning

Classical planning is defined as the task of finding a sequence of actions to accomplish a
goal in a discrete, deterministic, static, fully observable environment.

PDDL: Planning Domain Definition Language

## PDDL

Action schema
precondition
effect
Example:
```{=latex}
\begin{align*}
& Action(Fly(p,from,to),\\
& \hspace{.1in} PRECOND:At(p,from) \land Plane(p) \land Airport(from) \land Airport(to)\\
& \hspace{.1in} EFFECT: \neg At(p,from) \land At(p,to))
\end{align*}
```

Ground (variable-free) action:

```{=latex}
\begin{align*}
& Action(Fly(P1,SFO,JFK), \\
& \hspace{.1in} PRECOND:At(P1,SFO) \land Plane(P1) \land Airport(SFO) \land Airport(JFK) \\
& \hspace{.1in} EFFECT: \neg At(P1,SFO) \land At(P1,JFK))
\end{align*}
```

## Air Cargo Transport

```{=latex}
\begin{center}
```
![](aima-fig-11_01-pddl-air-cargo.pdf){height="70%"}
```{=latex}
\end{center}
```

## Spare Tire

```{=latex}
\begin{center}
```
![](aima-fig-11_02-pddl-spare-tire.pdf){height="70%"}
```{=latex}
\end{center}
```

## Blocks World

```{=latex}
\begin{center}
```
![](aima-fig-11_03-blocks-world-diagram.pdf){height="70%"}
```{=latex}
\end{center}
```

## Blocks World

```{=latex}
\begin{center}
```
![](aima-fig-11_04-pddl-blocks-world.pdf){height="70%"}
```{=latex}
\end{center}
```

## Forward and Backward State Space Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_05-forward-backward-search.pdf){height="70%"}
```{=latex}
\end{center}
```

## Heuristics for Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_06-ignore-delete-state-spaces.pdf){height="70%"}
```{=latex}
\end{center}
```

## Hierarchical Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_07-high-level-action-refinements.pdf){height="70%"}
```{=latex}
\end{center}
```

## Hierarchical Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_08-hierarchical-search-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Reachable Sets

```{=latex}
\begin{center}
```
![](aima-fig-11_09-schematic-reachable-sets.pdf){height="70%"}
```{=latex}
\end{center}
```

## Goal Acievement

```{=latex}
\begin{center}
```
![](aima-fig-11_10-goal-achievement.pdf){height="70%"}
```{=latex}
\end{center}
```

## Angelic Search

```{=latex}
\begin{center}
```
![](aima-fig-11_11-angelic-search-algorithm.pdf){height="70%"}
```{=latex}
\end{center}
```

## Online Planning

```{=latex}
\begin{center}
```
![](aima-fig-11_12-action-monitoring.pdf){height="70%"}
```{=latex}
\end{center}
```

## Resource Constraints

```{=latex}
\begin{center}
```
![](aima-fig-11_13-pddl-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```

## Temporal Constraints

```{=latex}
\begin{center}
```
![](aima-fig-11_14-temporal-constraints-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```

## Job-Schop Scheduling Solutions

```{=latex}
\begin{center}
```
![](aima-fig-11_15-solution-job-shop-scheduling.pdf){height="70%"}
```{=latex}
\end{center}
```
