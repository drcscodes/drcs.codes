---
title: Problem Solving
author: Artificial Intelligence
institute: Christopher Simpkins
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

## Problem-Solving Agents

- Goal formulation
- Problem formulation
- Search
- Execution

open-loop vs. closed-lop

## Search Problems and Solutions

Search problem:

- A set of **states**, which we call a **state space**.
- **Initial state**
- A set of **goal states**
- Sets of **actions** available in each state, `ACTION(s)`

    - `ACTION(Arad) = {ToSibiu, ToTimisoara, ToZerind}`

- A **transition model**, `RESULT(s, a)`

    - `RESULT(Arad, ToZerind) = Zerind`

- An **action cost function**, `ACTION-COST(s, a, s')` or $c(s, a, s')$ which returns the cost of executing action $a$ in state $s$ and reaching state $s'$.

## Solution

- A solution is a path from the start state to the a goal state.
- An optimal solution is a solution with lowest cost among all solutions.

```{=latex}
\begin{center}
```
![](aima-fig-03_01-romania.pdf)
```{=latex}
\end{center}
```

## Vacuum State Space Graph

```{=latex}
\begin{center}
```
![](aima-fig-03_02-vacuum-state-space-graph.pdf)
```{=latex}
\end{center}
```

## Agents

```{=latex}
\begin{center}
```
![](aima-fig-03_03-eight-puzzle.pdf)
```{=latex}
\end{center}
```

## Search Algorithms

- Search tree

## Searching State Space

```{=latex}
\begin{center}
```
![](aima-fig-03_04-arad-bucharest-partial-trees.pdf)
```{=latex}
\end{center}
```

## Search Tree Expansion

```{=latex}
\begin{center}
```
![](aima-fig-03_05-search-tree-expansion.pdf)
```{=latex}
\end{center}
```

## Separation Property of Graph Search

```{=latex}
\begin{center}
```
![](aima-fig-03_06-separation-property-graph-search.pdf)
```{=latex}
\end{center}
```

- (a) Only root expanded.
- (b) Top frontier node expanded.
- (c) Remaining successors of root expanded in clockwise order.

## Best-First Search Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-03_07-best-first-search-algorithm.pdf)
```{=latex}
\end{center}
```

## Search Data Structures

Node:

- `node.STATE`: the state to which the node corresponds;
- `node.PARENT`: the node in the tree that generated this node;
- `node.ACTION`: the action that was applied to the parent’s state to generate this node;
- `node.PATH-COST`: the total cost of the path from the initial state to this node. In math- ematical formulas, we use g(node) as a synonym for PATH-COST.

Frontier:

- `IS-EMPTY(frontier)` returns true only if there are no nodes in the frontier.
- `POP(frontier)` removes the top node from the frontier and returns it.
- `TOP(frontier)` returns (but does not remove) the top node of the frontier.
- `ADD(node, frontier)` inserts node into its proper place in the queue.

Queues used in search algorithms:

- A **priority queue** first pops the node with the minimum cost according to some evaluation function, f . It is used in best-first search.
- A **FIFO queue** or first-in-first-out queue first pops the node that was added to the queue first; we shall see it is used in breadth-first search.
- A **LIFO queue** or last-in-first-out queue (also known as a stack) pops first the most recently added node; we shall see it is used in depth-first search.

## Redundant Paths

Repeated states

cycles

redundant paths

graph search

tree-like search

## Measuring Problem-Solving Performance

- Completeness: Is the algorithm guaranteed to find a solution when there is one, and to correctly report failure when there is not?
- Cost optimality: Does it find a solution with the lowest path cost of all solutions?
- Time complexity: How long does it take to find a solution? This can be measured in seconds, or more abstractly by the number of states and actions considered.
- Space complexity: How much memory is needed to perform the search?

## Uninformed Search Strategies

Strategy:


## Breadth-First Search

```{=latex}
\begin{center}
```
![](aima-fig-03_08-bfs-binary-tree.pdf)
```{=latex}
\end{center}
```
```{=latex}
\begin{center}
```
![](aima-fig-03_09-bfs-algorithm.pdf)
```{=latex}
\end{center}
```

## Dijkstra's Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-03_10-sibiu-bucharest.pdf)
```{=latex}
\end{center}
```

## Depth-First Search

```{=latex}
\begin{center}
```
![](aima-fig-03_11-dfs-progress.pdf)
```{=latex}
\end{center}
```

## Depth-Limited Search and Iterative Deepening Search

```{=latex}
\begin{center}
```
![](aima-fig-03_12-depth-limited-iterative-deepening-algorithms.pdf)
```{=latex}
\end{center}
```

## Progression of Iterative Deepening Search

```{=latex}
\begin{center}
```
![](aima-fig-03_13-iterative-deepening-progress.pdf)
```{=latex}
\end{center}
```

## Bidirectional Best-First Search

```{=latex}
\begin{center}
```
![](aima-fig-03_14-bidirectional-best-first-search-algorithm.pdf)
```{=latex}
\end{center}
```

## Comparing Uninformed Search Algorithms

```{=latex}
\begin{center}
```
![](aima-fig-03_15-uninformed-search-comparisons.pdf)
```{=latex}
\end{center}
```
