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

```{=latex}
\begin{center}
```
![](aima-fig-03_01-romania.pdf){height="60%"}
```{=latex}
\end{center}
```

- In this lesson we consider a *state* to be our location in one of these cities.
- A *goal* is a state in which we are located in a particular city.

This is the essence of problem solving: transforming a current state into a goal state.  The first family of algorithms we'll study for problem solving are *search* algorithms.


## Problem Solving Process

To solve a problem, we

- Formulate a **goal**, e.g., "reach Bucharest"
- Formulate the **problem** as a set of states and actions that move us from one state to another.

    - Problem is a **model** -- an *abstract* mathematical description.
    - Abstraction is essence and ignorance.
    - Key skill in problem formulation is finding the right **level of abstraction**.

- **Search** the possible sequences of action in our problem model that transforms our state from the current state to the goal state.  A sequence of actions that gets us to the goal state is called a *solution*.  May be many; pick one.
- **Execute** the actions in the solution.

## Open-Loop vs. Closed-Loop

- In an **open-loop** system the agent gets no feedback, i.e., sensor input, after executing an action.

    - If the agent's model is perfect and actions are deterministic, then the agent can operate in an open-loop fashion, simply executing the actions in the solution one after the other.

- In a **closed-loop** system gets sensory feedback after every action, so it can check whether the action had the expected effect.

    - If the environment is partially observable or actions are nondeterministic, closed-loop control is necessary.
    - Say the agent executes to `ToSibiu` action but ends up in `Zerind`.  Closed-loop feedback will alert the agent to this fact so it can re-plan.

## Search Problems and Solutions

A search problem consists of:

- A set of **states**, which we call a **state space**.
- **Initial state**
- A set of **goal states**.

    - Typically use an `IS-GOAL(s)` predicate function to identify goal states.

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
![](aima-fig-03_01-romania.pdf){height="60%"}
```{=latex}
\end{center}
```
- How many paths are there from `Arad` to `Bucharest`?
- What is/are the solutions to the `Arad-to-Bucharest` problem (assume perfect information -- fully observable, known dynamics, and deterministic actions)?

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
![](aima-fig-03_04-arad-bucharest-partial-trees.pdf){height="90%"}
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
