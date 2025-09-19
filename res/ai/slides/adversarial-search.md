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

**Competitive environments**, in which two or more agents have conflicting goals, give rise to **adversarial search** problems.

Three approaches to dealing with multiagent environments:

1. With a large number of agents, consider aggregates of agents as an **economy**, e.g., supply-demand relationships, without predicting actions of any individual agents.

2. Consider adversarial agents as just a part of the environment—a part that makes the environment nondeterministic. But if we model the adversaries in the same way that, say, rain sometimes falls and sometimes doesn’t, we miss the idea that our adver- saries are actively trying to defeat us, whereas the rain supposedly has no such intention.

3. Explicitly model the adversarial agents with the techniques of adversarial game-tree search.

This lesson deals with the third approach.

## From Game Theory to Adversarial AI

In game theory, games like Chess and Go are deterministic, two-player, turn-taking, perfect information, zero-sum games.

| Game Theory         | AI                   |
|---------------------|----------------------|
| Perfect information | Fully observable     |
| Player              | Agent                |
| Move                | Action               |
| Position            | State                |
| Payoff/Score        | Utility/Reward/Value |

In AI we commonly study two-player zero sum games, in which the "score" for one agent is the negative of the other agent's, i.e., they add to zero.

> Note: in Chess tournaments draws award each player scores of $\frac{1}{2}$, but in an AI chess playing algorithms you can use +1, -1, and 0.  Alternatively, you can model chess as a "constant sum" game with scores of 1, 0, or $\frac{1}{2}$.

## Two-Player Zero-Sum Games

Two players: MAX and MIN.  MAX moves first.

A game can be formally defined with the following elements:

- $S_0$: The initial state, which specifies how the game is set up at the start.

- $ToMove(s)$: The player whose turn it is to move in state $s$, MAX or MIN.

- $Actions(s)$: The set of legal moves in state $s$.

- $Result(s, a)$: The transition model, which defines the state resulting from taking action $a$ in state $s$.

- $IsTerminal(s)$: A terminal test, which is true when the game is over and false otherwise. States where the game has ended are called terminal states.

- $Utility(s,p)$: A utility function (also called an objective function or payoff function), which defines the final numeric value to player $p$ when the game ends in terminal state $s$.  In chess, the outcome is a win, loss, or draw, with values 1, 0, or 1/2. Some games have a wider range of possible outcomes—for example, the payoffs in backgammon range from 0 to 192.

## Tic-Tac-Toe Game Tree

```{=latex}
\begin{center}
```
![](aima-fig-05_01-tic-tac-toe-game-tree.pdf){height="70%"}
```{=latex}
\end{center}
```

Tic-tac-toe is relatively small -- fewer than $9!= 362,880$ terminal nodes with only 5,478 distinct states.

## Optimal Decisions in Games

- MAX searches for a sequence of actions leading to a win.
- MIN searches for a sequence of actions leading to a loss for MAX.
- So MAX's stratregy is a contingfency plan dependent on MIN's responses.
- We could use AND-OR search, but we'll study a more general approach: **minimax search**.

Minimax search generates a game tree with moves for both MAX and MIN

- At each MAX node, choose from actions $a \in Actions(s)$ with maximum value relative to MAX.
- At each MIN node, choose from actions $b \in Actions(s)$ with minimum value relative to MAX.
- One move by one player is called a **ply**.  A ply for MAX plus the response ply for MIN constitute a game move.

## Minimax Decision

- Given a game tree, the optimal strategy can be determined by working out the **minimax value** of each state in the tree, which we write as $Minimax(s)$.

- The minimax value is the utility (for MAX) of being in that state, assuming that both players play optimally from there to the end of the game. The minimax value of a terminal state is just its utility.

$$
Minimax(s) =
\begin{cases}
Utility(s,MAX)                              & \text{if } IsTerminal(s) \\
max_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MAX \\
min_{a \in Actions(s)} Minimax(Result(s,a)) & \text{if } ToMove(s) = MIN
\end{cases}
$$

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
- MAX’s best move at the root is $a_1$, because it leads to state with highest minimax value.
- MIN’s best reply is $b_1$, because it leads to the state with the lowest minimax value.

## Minimax Algorithm

:::: {.columns}
::: {.column valign="top" width="30%"}

- Recurse through MIN and MAX plies of the game tree to leaf nodes.
- Back up minimax values through the tree.
- Choose branch with highest minimax value.

:::
::: {.column valign="top" width="70%"}

```{=latex}
\begin{center}
```
![](aima-fig-05_03-minimax-algorithm.pdf)
```{=latex}
\end{center}
```

:::
::::

## Analysis of Minimax

- Time complexity: $O(b^m)$
- Space complexity:

    - $O(bm)$ if generates all actions at once
    - $O(m)$ if generates actions one at a time

Chess has an average branching factor of 35 and an average game has a depth of 80.

- $O(b^m) = 35^80 \approx 10^123$ states

Clearly, minimax won't work for Chess.  We'll make two modifications to minimax that makes games like Chess tractable.

<!--
## Multiplayer Games

Instead of single value, vector of values.

- For three players $A, B, C$, a vector $<v_A, v_B, v_C>$ at each node.

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
-->

## Alpha-Beta Pruning

Number of game states is exponential in depth of tree, so we have to **prune** branches of the tree to make searching it tractable.

```{=latex}
\begin{center}
```
![](aima-fig-05_05-f-alpha-beta-tree.pdf){height="30%"}
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

In other words, the value of the root and hence the minimax decision are independent of the values of the leaves x and y, and therefore they can be pruned.

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

:::: {.columns}
::: {.column valign="top" width="40%"}

- Updates the values of $\alpha$ and $\beta$ as it goes along
- Prunes the remaining branches at a node (i.e., terminates the recursive call) as soon as the value of the current node is known to be worse than the current $\alpha$ for MAX, or $\beta$ for MIN.

:::
::: {.column valign="top" width="60%"}


```{=latex}
\begin{center}
```
![](aima-fig-05_07-alpha-beta-algorithm.pdf)
```{=latex}
\end{center}
```

:::
::::

## Heuristic Alpha-Beta Tree Search

Alpha-beta search helps, but it is still highly dependent on move ordering.  So we need more help in limiting search.

- We define a **heuristic evaluation function** that evaluates a static position.
- We replace the terminal test with a cutoff test and use the heuristic evaluation function to determine the node's value.

$$
HMinimax(s, d) =
\begin{cases}
Eval(s,MAX)                                        & \text{if } IsCutoff(s, d) \\
max_{a \in Actions(s)} HMinimax(Result(s,a), d+1) & \text{if } ToMove(s) = MAX \\
min_{a \in Actions(s)} HMinimax(Result(s,a), d+1) & \text{if } ToMove(s) = MIN
\end{cases}
$$


## Static Evaluation Functions

A heuristic evaluation function $Eval(s,p)$ returns an estimate of the expected utility of state $s$ to player $p$, just as the heuristic functions of Chapter 3 return an estimate of the distance to the goal.

- For terminal states, $Eval(s,p) = Utility(s,p)$.
- For nonterminal states, the evaluation must be somewhere between a loss and a win: $Utility(loss,p) \le Eval(s,p)  \le Utility(win,p)$.

A popular form of hueristic evaluation function is a weighted linear evaluation function:

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

In alpha-beta search algorithm, keep track of depth so you can cut off at a particular depth and replace lines with $IsTerminal(state)$ with

$$
\textbf{if } game.IsCutoff(state, depth) \textbf{ then return } game.Eval(state, player), null
$$

Best to apply cutoff quiescent positions, that is, positions that don't contain a killer move that would radically change the value of the position.  Adding this to the $IsCutoff$ function is called **quiescence search**.


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

- Selection: Starting at the root of the search tree, we choose a move (guided by the selection policy), leading to a successor node, and repeat that process, moving down the tree to a leaf.

- Expansion: We grow the search tree by generating a new child of the selected node.

- Simulation: We perform a playout from the newly generated child node, choosing moves for both players according to the playout policy. These moves are not recorded in the search tree. In the next slide, the simulation results in a win for black.

- Back-propagation: We now use the result of the simulation to update all the search tree nodes going up to the root. Since black won the playout, black nodes are incremented in both the number of wins and the number of playouts, so 27/35 becomes 28/36 and 60/79 becomes 61/80. Since white lost, the white nodes are incremented in the number of playouts only, so 16/53 becomes 16/54 and the root 37/100 becomes 37/101.

## MCTS Iteration

```{=latex}
\begin{center}
```
![](aima-fig-05_10-mcts-iteration.pdf){height="50%"}
```{=latex}
\end{center}
```

- (a) We select moves, all the way down the tree, ending at the leaf node marked 27/35 (for 27 wins for black out of 35 playouts).
- (b) We expand the selected node and do a simulation (playout), which ends in a win for black.
- (c) The results of the simulation are back-propagated up the tree.

## MCTS Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-05_11-mcts-algorithm.pdf)
```{=latex}
\end{center}
```

## MCTS Selection Policy

$$
UCB1(n) = \frac{U(n)}{N(n)} + C \times \sqrt{ \frac{\log N (PARENT(n))}{N(n)} }
$$

<!--

## Stochastic Games

```{=latex}
\begin{center}
```
![](aima-fig-05_12-backgammon-position.pdf)
```{=latex}
\end{center}
```

## Expectiminimax

$$
ExpectiMinimax(s) =
\begin{cases}
Utility(s,MAX)                           & \text{if } IsTerminal(s) \\
max_{a} ExpectiMinimax(Result(s,a))      & \text{if } ToMove(s) = MAX \\
min_{a} ExpectiMinimax(Result(s,a))      & \text{if } ToMove(s) = MIN \\
\sum_r Pr(r) ExpectiMinimax(Result(s,a)) & \text{if } ToMove(s) = CHANCE
\end{cases}
$$


## Backgammon Game Tree

```{=latex}
\begin{center}
```
![](aima-fig-05_13-backgammon-game-tree.pdf)
```{=latex}
\end{center}
```

## Evaluation Functions for Games of Chance

```{=latex}
\begin{center}
```
![](aima-fig-05_14-order-preserving-transformation.pdf)
```{=latex}
\end{center}
```

## Partially Observable Games

```{=latex}
\begin{center}
```
![](aima-fig-05_15-krk-checkmate.pdf)
```{=latex}
\end{center}
```

## Errors in Heuristic Minimax Search

```{=latex}
\begin{center}
```
![](aima-fig-05_16-heuristic-minimax-errors.pdf)
```{=latex}
\end{center}
```

- If evaluation function is 100% correct, right branch is correct.
- If evaluation function has random error with $\sigma = 5$, left is better 71% of the time because one of the four right-hand leaves will dip below 99.
- If evaluation function has random error with $\sigma = 2$, left is better 58% of the time.


## Closing Thoughts

The game playing algorithms we considered here have limitations that we will address in furture lessons.

- Vulnerability to errors in the heuristic function. (See Previous slide.)
- Sometimes there is a single clearly best move, but Alpha-beta and MCTS waste computation by calculating values of many legal moves.

    - Better to employ metareasoning about the utility of node expansion -- only expand nodes likely to lead to a better move.

- Alpha-beta and MCTS reason about individual moves.  Humans reason abstractly, selectively forming plausible plans to acheive (intermediate) goals, e.g., trapping the opponent's queen.

    - We will learn about such approaches when we study **planning**.

- Alpha-beta (and MCTS when depth-limited) rely on human-crafted evaluation functions.

    - Programs like AlphaZero[^AlphaZero] need only the rules of the game to learn how to play at superhuman levels.


[^AlphaZero]: https://arxiv.org/pdf/1712.01815

-->
