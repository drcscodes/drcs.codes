---
title: Artificial Intelligence
subtitle: Adversarial Search
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

## Games

Economy

Pruning

Evaluation function

## Two-Player Zero-Sum Games

- $S_0$: The initial state, which specifies how the game is set up at the start.

- $ToMove(s)$: The player whose turn it is to move in state s.

- $Actions(s)$: The set of legal moves in state s.

- $Result(s, a)$: The transition model, which defines the state resulting from taking ac- Transition model tion a in state s.

- $IsTerminal(s)$: A terminal test, which is true when the game is over and false Terminal test otherwise. States where the game has ended are called terminal states. Terminal state

- $Utility(s,p)$: A utility function (also called an objective function or payoff function), which defines the final numeric value to player p when the game ends in terminal state s.  In chess, the outcome is a win, loss, or draw, with values 1, 0, or 1/2.2 Some games have a wider range of possible outcomes—for example, the payoffs in backgammon range from 0 to 192.

## title

```{=latex}
\begin{center}
```
![](aima-fig-05_01-tic-tac-toe-game-tree.pdf)
```{=latex}
\end{center}
```

## Optimal Decisions in Games

Minimax search

Ply

Minimax value

$$
Minimax(s) =
\begin{cases}
Utility(s,MAX)                              & \text{if } IsTerminal(s) \\
max_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MAX \\
min_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MIN
\end{cases}
$$

Minimax Decision

## Minimax Game Tree

```{=latex}
\begin{center}
```
![](aima-fig-05_02-two-ply-game-tree.pdf)
```{=latex}
\end{center}
```

A two-ply game tree.

- $\triangle$ nodes are "MAX nodes," --  MAX’s turn to move.
- $\triangledown$ nodes are "MIN nodes."
- Terminal nodes show the utility values for MAX.
- Other nodes are labeled with their minimax values.
- MAX’s best move at the root is $a_1$, because it leads to the state with the highest minimax value.
- MIN’s best reply is $b_1$, because it leads to the state with the lowest minimax value.

## Minimax Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-05_03-minimax-algorithm.pdf)
```{=latex}
\end{center}
```

## Analysis of Minimax

- Time complexity: $O(b^m)$
- Space complexity:

    - $O(bm)$ if generates all actions at once
    - $O(m)$ if generates actions one at a time

Chess has an average branching factor of 35 and an average game has a depth of 80.

- $O(b^m) = 35^80 \sim 10^123$ states

## Multiplayer Games

Instead of single value, vector of values

alliances

## Three Player Game Tree

```{=latex}
\begin{center}
```
![](aima-fig-05_04-three-player-three-ply-game-tree.pdf)
```{=latex}
\end{center}
```

The first three ply of a game tree with three players (A, B, C). Each node is labeled with values from the viewpoint of each player. The best move is marked at the root.

## Alpha-Beta Pruning


```{=latex}
\begin{center}
```
![](aima-fig-05_05-f-alpha-beta-tree.pdf){height="40%"}
```{=latex}
\end{center}
```

```{=latex}
\begin{align*}
Minimax(root) &= max(min(3,12,8),min(2,x,y),min(14,5,2)) \\
              &= max(3,min(2,x,y),2) \\
              &= max(3,z,2) \text{ where } z = min(2,x,y) \le 2 \\
              &= 3.
\end{align*}
```

## Alpha-Beta Calculation Stages

```{=latex}
\begin{center}
```
![](aima-fig-05_05-game-tree-calculation-stages.pdf){height="90%"}
```{=latex}
\end{center}
```


## Alpha Beta

:::: {.columns}
::: {.column width="50%"}

```{=latex}
\begin{center}
```
![](aima-fig-05_06-general-alpha-beta-pruning.pdf)
```{=latex}
\end{center}
```

If $m$ or $m'$ is better than $n$ for Player, we will never get to $n$ in play.

:::
::: {.column width="50%"}

- $\alpha$ = the value of the best (i.e., highest-value) choice we have found so far at any choice point along the path for MAX.

    - Think: $\alpha$ = "at least."

- $\beta$ = the value of the best (i.e., lowest-value) choice we have found so far at any choice point along the path for MIN.

    - Think: $\beta$ = "at most."

:::
::::

## Alpha-Beta Search Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-05_07-alpha-beta-algorithm.pdf){height="90%"}
```{=latex}
\end{center}
```

## Move Ordering

Section 6.2.4

## Heuristic Alpha-Beta Tree Search

$$
Minimax(s) =
\begin{cases}
Utility(s,MAX)                              & \text{if } IsTerminal(s) \\
max_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MAX \\
min_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MIN
\end{cases}
$$


## Static Evaluation Functions


Weighted linear evaluation functions:

$$
Eval(s) = w_1 f_1(s) + w_2 f_2(s) + \cdots + w_n f_n(s) = \sum _{i=1}^n w_i f_i(s),
$$

- Each $f_i$ is a feature of the position such as "number of white bishops."
- Each $w_i$ is a weight saying how important that feature is.

## Chess Configuration Examples

```{=latex}
\begin{center}
```
![](aima-fig-05_08-chess-positions.pdf)
```{=latex}
\end{center}
```

- (a) Black has an advantage of a knight and two pawns, which should be enough to win the game.
- (b) White will capture the queen, giving it an advantage that should be strong enough to win.

## Cutting Off Search

In alpha-beta search algorithm, replace lines with $IsTerminal(state)$ with

$$
\textbf{if } game.IsCutoff(state, depth) \textbf{ then return } game.Eval(state, player), null
$$

quiescent positions

quiescence

## Horizon Effect

```{=latex}
\begin{center}
```
![](aima-fig-05_09-chess-horizon-effect.pdf)
```{=latex}
\end{center}
```

## Monte Carlo Tree Search (MCTS)

Two major weaknesses of heuristic alpha-beta tree search:

- Can't handle high branching factors. Go has a branching factor that starts at 361, which means alpha–beta search would be limited to only 4 or 5 ply.

- Can't always define a good static evaluation function.  E.g., in Go material value is not a strong indicator and most positions are in flux until the endgame.

...

## Exploration/Exploitation Tradoff in MCTS

- Selection: Starting at the root of the search tree, we choose a move (guided by the selection policy), leading to a successor node, and repeat that process, moving down the tree to a leaf. Figure 6.10(a) shows a search tree with the root representing a state where white has just moved, and white has won 37 out of the 100 playouts done so far. The thick arrow shows the selection of a move by black that leads to a node where black has won 60/79 playouts. This is the best win percentage among the three moves, so selecting it is an example of exploitation. But it would also have been reasonable to select the 2/11 node for the sake of exploration—with only 11 playouts, the node still has high uncertainty in its valuation, and might end up being best if we gain more information about it. Selection continues on to the leaf node marked 27/35.

- Expansion: We grow the search tree by generating a new child of the selected node; Figure 6.10(b) shows the new node marked with 0/0. (Some versions generate more than one child in this step.)

- Simulation: We perform a playout from the newly generated child node, choosing moves for both players according to the playout policy. These moves are not recorded in the search tree. In the figure, the simulation results in a win for black.

- Back-propagation: We now use the result of the simulation to update all the search tree nodes going up to the root. Since black won the playout, black nodes are incremented in both the number of wins and the number of playouts, so 27/35 becomes 28/36 and 60/79 becomes 61/80. Since white lost, the white nodes are incremented in the number of playouts only, so 16/53 becomes 16/54 and the root 37/100 becomes 37/101.

## MCTS Iteration

```{=latex}
\begin{center}
```
![](aima-fig-05_10-mcts-iteration.pdf)
```{=latex}
\end{center}
```

## MCTS Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-05_11-mcts-algorithm.pdf)
```{=latex}
\end{center}
```

## MCTS Selectoin Policy

$$
UCB1(n) = \frac{U(n)}{N(n)} + C \times \sqrt{ \frac{\log N (PARENT(n))}{N(n)} }
$$

## title

```{=latex}
\begin{center}
```
![](aima-fig-05_12-backgammon-position.pdf)
```{=latex}
\end{center}
```

## title

```{=latex}
\begin{center}
```
![](aima-fig-05_13-backgammon-game-tree.pdf)
```{=latex}
\end{center}
```

## title

```{=latex}
\begin{center}
```
![](aima-fig-05_14-order-preserving-transformation.pdf)
```{=latex}
\end{center}
```

## title

```{=latex}
\begin{center}
```
![](aima-fig-05_15-krk-checkmate.pdf)
```{=latex}
\end{center}
```

## title

THe end.
