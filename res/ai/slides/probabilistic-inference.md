---
title: Artificial Intelligence
subtitle: Probabilistic Inference
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

## Exact Inference in Bayesian Networks (AIMA 13.3)

Most common task in probabilistic inference: compute the *posterior probability* of a set of **query variables** given some **event** represented as a set of **evidence variables**.

:::: {.columns}
::: {.column width="70%"}

Notation:

- Query variable: $X$
- Set of evidence variables: $\bm{E} = \{E_1, \dots, E_m\}$
- Particular observed event: $\bm{e}$
- Hidden (nonevidence, nonquery) variables: $\bm{Y} = \{Y_1, \dots, Y_l\}$
- Typical query: $Pr(X \mid e)$

Example:

- $X$ is the boolean random variable $Burglary$
- $\bm{E} = \{JohnCalls, MaryCalls\}$
- $\bm{e} = \{JohnCalls = true, MaryCalls = true\}$
- $\bm{Y} = \{EarthQuake, Alarm\}$

:::
::: {.column width="35%"}


```{=latex}
\begin{center}
```
![](aima-fig-13_02-bayes-net-alarm.pdf)
```{=latex}
\end{center}
```

:::
::::

$$
Pr(Buglary \mid JohnCalls = true, MaryCalls = true) = <0.284, 0.716>.
$$


## Inference by Enumeration

Recall that we can use the full joint distribution to answer any query:

$$
Pr(X | \bm{e}) = \alpha Pr(X, \bm{e}) = \alpha \sum_y Pr(X, \bm{e}, \bm{y}) \tag{12.9}
$$


And that a Bayes net completely represents the full joint distribution, so we can reduce the computation of a joint to:

$$
Pr(x_1, \dots, x_n) = \prod_{i=1}^n Pr( x_i | parents(X_i)) \tag{13.2}
$$

Using these two equations we can enumerate the appropriate probabilities to calculate the answer to any probabilistic query.

- In particular, we can get the answer by computing sums of products of conditional probabilities from a Bayes net.

## Example: $Pr(Burglary \mid JohnCalls=true, MaryCalls=true)$.

Using abbreviations and substituting into Eq 12.9 above ($e$ and $a$ are hidden):

```{=latex}
\[
Pr(B \mid j, m) = \alpha Pr(B, j, m) = \alpha \sum_e \sum_a Pr(B, j, m, e, a)
\]
```

Then we substitute Eq 13.2 for $Pr(B, j, m, e, a)$ to get (onyly showing Burglary=true):

```{=latex}
\vspace{-.1in}
\begin{align*}
Pr(b \mid j, m) &= \alpha \sum_e \sum_a Pr(b) Pr(e) Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a) \tag{1}\\
                &= \alpha Pr(b) \sum_e \sum_a Pr(e) Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a) \tag{2}\\
                &= \alpha Pr(b) \sum_e Pr(e) \sum_a Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a) \tag{3}
\end{align*}
\vspace{-.1in}
```

1. Substitute Eq 13.2 for $Pr(B, j, m, e, a)$
2. Pull out $Pr(b)$ from summations because it doesn't depend on the other variable and is thus a constant in all the summation terms.
3. Pull out $Pr(e)$ from the summation over the $a$ values because each value of $e$ doesn't depend on the other variables in the summation over the $a$ values and is thus a constant in the summation terms over the values of $a$.

Steps 2 and 3 above reduce the complexity of the computation from $O(n2^n)$ to $O(2^n)$.

## Caclulation of $Pr(b \mid j, m)$

:::: {.columns}
::: {.column width="70%"}

Substiting the values from the CPTs in the Bayes net into
$$
\alpha Pr(b) \sum_e Pr(e) \sum_a Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a)
$$

we get the expression tree:

```{=latex}
\begin{center}
```
![](aima-fig-13_10-prob-expression-tree.pdf){height="60%"}
```{=latex}
\end{center}
```


:::
::: {.column width="40%"}

```{=latex}
\begin{center}
```
![](aima-fig-13_02-bayes-net-alarm.pdf){height="40%"}
```{=latex}
\end{center}
```

:::
::::


## Enumeration Algorithm

The ENUMERATION-ASK algorithm evaluates these expression trees using depth-first, left-to-right recursion.

```{=latex}
\begin{center}
```
![](aima-fig-13_11-bayes-net-enumeration-algorithm.pdf)
```{=latex}
\end{center}
```

Unfortunately, its time complexity is $O(s^n)$.  But we can improve it ...

## Repeated Calculations

Notice that the subexpressions for the products $Pr(j \mid a) Pr(m \mid a)$ and $Pr(j \mid \neg a) Pr(m \mid \neg a)$ are computed twice, once for each value of $E$.

```{=latex}
\begin{center}
```
![](aima-fig-13_10-prob-expression-tree.pdf)
```{=latex}
\end{center}
```

## Variable Elimination

The enumeration algorithm can be improved substantially by eliminating repeated calculations.

- Idea:  do the calculation once and save the results for later use.
- This is a form of dynamic programming.
- Several versions of this approach; variable elimination algorithm is simplest.

Variable elimination works by evaluating expressions such as

$$
Pr(b \mid j, m) = \alpha Pr(b) \sum_e Pr(e) \sum_a Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a) \tag{13.5}
$$

in right-to-left order (that is, bottom up in the expression tree), storing intermediate results, and only doing summations for portions of the expression that depend on the variable.

## Example: Variable Elimination in Burglary Network

First, annotate the **factor**s in the expression for the network:

$$
Pr(B \mid j, m) =
\alpha \underbrace{Pr(B)}_{\bm{f}_1(B)}
\sum_e
\underbrace{Pr(e)}_{\bm{f}_2(E)}
\sum_a
\underbrace{Pr(a \mid B, e)}_{\bm{f}_3(A,B,E)}
\underbrace{Pr(j \mid a)}_{\bm{f}_4(A)}
\underbrace{Pr(m \mid a)}_{\bm{f}_5(A)}
$$

- Each factor is a matrix indexed by the values of its argument variables.
- Notice that the factors for $Pr(j \mid a)$ and $Pr(m | a)$ do not include $j$ and $m$.  This is because the values of $j$ and $m$ ($JohnCalls=true$ and $MaryCalls-true$) are fixed by the query.

So the factors are:

:::: {.columns}
::: {.column width="50%"}

$$
\bm{f}_1(B) =
\begin{bmatrix}
Pr(b) \\
Pr(\neg b)
\end{bmatrix}
=
\begin{bmatrix}
0.001 \\
0.999
\end{bmatrix}
$$

:::
::: {.column width="50%"}

$$
\bm{f}_2(E) =
\begin{bmatrix}
Pr(e) \\
Pr(\neg e)
\end{bmatrix}
=
\begin{bmatrix}
0.002 \\
0.998
\end{bmatrix}
$$

:::
::::

```{=latex}
\vspace{.2in}
```

:::: {.columns}
::: {.column width="50%"}

$$
\bm{f}_4(A) =
\begin{bmatrix}
Pr(j \mid a) \\
Pr(j \mid \neg a)
\end{bmatrix}
=
\begin{bmatrix}
0.090 \\
0.05
\end{bmatrix}
$$

:::
::: {.column width="50%"}

$$
\bm{f}_5(A) =
\begin{bmatrix}
Pr(m \mid a) \\
Pr(m \mid \neg a)
\end{bmatrix}
=
\begin{bmatrix}
0.070 \\
0.01
\end{bmatrix}
$$

:::
::::


```{=latex}
\vspace{.2in}
```

$\bm{f}_3(A, B, E)$ is a little more complicated ...

## $\bm{f}_3(A, B, E)$

$$
Pr(B \mid j, m) =
\alpha \underbrace{Pr(B)}_{\bm{f}_1(B)}
\sum_e
\underbrace{Pr(e)}_{\bm{f}_2(E)}
\sum_a
\underbrace{Pr(a \mid B, e)}_{\bm{f}_3(A,B,E)}
\underbrace{Pr(j \mid a)}_{\bm{f}_4(A)}
\underbrace{Pr(m \mid a)}_{\bm{f}_5(A)}
$$

$\bm{f}_3(A, B, E)$ is a $2 \times 2 \times 2$ matrix (or a rank-3 tensor).  Here's one way to think about it:

- First index with $A$, yielding two $2 \times 2$ submatrices (one for each of the two values of $A$).
- Rows of each submatrix is indexed by $B$ and columns by $E$.
- The entries in the submatrices are the values of $Pr(A \mid B, E)$

:::: {.columns}
::: {.column width="60%"}
$$
\bm{f}_{3}^{(a)} (B, E) =
\begin{bmatrix}
Pr(a \mid b,e) & Pr(a \mid b, \neg e) \\
Pr(a \mid \neg b, e) & Pr(a \mid \neg b, \neg e)
\end{bmatrix}
=
\begin{bmatrix}
0.95 & 0.94\\
0.29 & 0.001
\end{bmatrix}
$$

$$
\bm{f}_{3}^{(\neg a)} (B, E) =
\begin{bmatrix}
Pr(\neg a \mid b,e) & Pr(\neg a \mid b, \neg e) \\
Pr(\neg a \mid \neg b, e) & Pr(\neg a \mid \neg b, \neg e)
\end{bmatrix}
=
\begin{bmatrix}
0.05 & 0.06\\
0.71 & 0.999
\end{bmatrix}
$$

:::
::: {.column width="40%"}

```{=latex}
\includegraphics[width=0.75\textwidth, right]{aima-fig-13_02-bayes-net-alarm.pdf}
```

:::
::::

## Factorized Query

From our original query:

$$
Pr(b \mid j, m) = \alpha Pr(b) \sum_e Pr(e) \sum_a Pr(a \mid b, e) Pr(j \mid a) Pr(m \mid a) \tag{13.5}
$$

We annotated the factors:


$$
Pr(B \mid j, m) =
\alpha \underbrace{Pr(B)}_{\bm{f}_1(B)}
\sum_e
\underbrace{Pr(e)}_{\bm{f}_2(E)}
\sum_a
\underbrace{Pr(a \mid B, e)}_{\bm{f}_3(A,B,E)}
\underbrace{Pr(j \mid a)}_{\bm{f}_4(A)}
\underbrace{Pr(m \mid a)}_{\bm{f}_5(A)}
$$

And now we substitute the factor expressions for the original expresions so we can manipulate the factors using the **pointwise product** operation, denoted with $\times$ here:

$$
Pr(B \mid j, m) =
\alpha \bm{f}_1(B) \times \sum_e \bm{f}_2(E) \times \sum_a \bm{f}_3(A,B,E) \times \bm{f}_4(A) \times \bm{f}_5(A)
$$

Now we are ready to evaluate the expression ...

## Expression Evaluation

First, sum out A from the pointwise product of $\bm{f}_3(A,B,E)$, $\bm{f}_4(A)$, and $\bm{f}_5(A)$ yielding a new $2 \times 2$ factor, $\bm{f}_6(B,E)$:

```{=latex}
\vspace{-.2in}
\begin{align*}
\bm{f}_6(B,E) &= \sum_a \bm{f}_3(A,B,E) \times \bm{f}_4(A) \times \bm{f}_5(A) \\
              &= (\bm{f}_3(a,B,E) \times \bm{f}_4(a) \times \bm{f}_5(a)) + (\bm{f}_3(\neg a,B,E) \times \bm{f}_4(\neg a) \times \bm{f}_5(\neg a))
\end{align*}
\vspace{-.2in}
```

Now the query expression is $Pr(B \mid j, m) =
\alpha \bm{f}_1(B) \times \sum_e \bm{f}_2(E) \times \bm{f}_6 (B, E)$

Next, sum out $E$ from the product of $\bm{f}_2 (E)$ and $\bm{f}_6 (B, E)$, yielding a new factor $\bm{f}_7 (B)$:

```{=latex}
\vspace{-.2in}
\begin{align*}
\bm{f}_7(B) &= \sum_e \bm{f}_2(E) \times \bm{f}_6(B, E) \\
            &= \bm{f}_2(e) \times \bm{f}_6(B, e) + \bm{f}_2(\neg e) \times \bm{f}_6(B, \neg e)
\end{align*}
\vspace{-.1in}
```

Which leaves our final form of the query: $Pr(B \mid j, m) =\alpha \bm{f}_1(B) \times \bm{f}_7(B)$

This expression can be evaluated by taking the pointwise product and normalizing the result.

## Operations on Factors

Two basic operations in variable elimination:

1. the pointwise product operation, and
3. summing out hidden variables from products of factors.


## Pointwise Product Example

The pointwise product of two factors $\bm{f}$ and $\bm{g}$ yields a new factor $\bm{h}$ whose variables are the union of the variables in $\bm{f}$ and $\bm{g}$ and whose elements are given by the product of the corresponding elements in the two factors.

If we have $X, Y, Z$ boolean variables, then here's the result of pointwise product $\bm{f}(X, Y) \times \bm{g}(Y, Z) = \bm{h}(X, Y, Z)$:

```{=latex}
\vspace{-.2in}
\begin{center}
```
![](aima-fig-13_12-pointwise-multiplication.pdf){height="50%"}
```{=latex}
\end{center}
```

## Summing out Variables

Summing out a variable from a product of factors is done by adding up the submatrices
formed by fixing the variable to each of its values in turn. For example, to sum out $X$ from
$h(X,Y,Z)$, we write

```{=latex}
\begin{align*}
\bm{h}_2 (Y, Z) &= \sum_x \bm{h}(X, Y, Z)\\
                &= \bm{h}(x, Y, Z) + \bm{h}(\neg x, Y, Z) \\
&=
\begin{bmatrix}
.06 & .24 \\
.42 & .28
\end{bmatrix}
+
\begin{bmatrix}
.18 & .72 \\
.06 & .04
\end{bmatrix} \\
&=
\begin{bmatrix}
.24 & .96 \\
.48 & .32
\end{bmatrix}
\end{align*}
```

## Variable Elimination Algorithm

With these two basic operations, we can implement the variable elimination algorithm:

```{=latex}
\begin{center}
```
![](aima-fig-13_13-bayes-net-variable-elimination-algorithm.pdf)
```{=latex}
\end{center}
```

Notes about the `order` function:

- Any ordering works, some orderings lead to more efficient algorithms.
- No tractable algorithm for determining optimal ordering.
- One heuristic: eliminate whichever variable minimizes the size of the next factor to be contructed.
- General rule: every variable that is not an ancestor of a query variable or evidence variable is irrelevant to the query.

## Complexity of Exact Inference in Polytrees

Notice that the Alarm Bayes net is **singly connected**, a.k.a., a **polytree**:

- there is at mose one undirected path between any two nodes in the network.

```{=latex}
\begin{center}
```
![](aima-fig-13_02-bayes-net-alarm.pdf){height="40%"}
```{=latex}
\end{center}
```

The time and space complexity of polytrees is linear in the size of the network.

- Size of network is defined as number of CPT entries.
- If $|parents(X_i)| \le c, \forall i \in n$ for some constant $c$ and number of nodes $n$, then complexity is also linear in number of nodes.


## Complexity of Exact Inference in Multiply-connected Networks

Now consider **multiply-connected** networks such as the car insurance network:

```{=latex}
\begin{center}
```
![](aima-fig-13_09-bayes-net-car-insurance.pdf){height="50%"}
```{=latex}
\end{center}
```

- Variable elimination can have exponential worst-case time and space complexity in multiply-connected networks.
- *Since inference in Bayes nets includes inference in propositional logic as a special case, Bayes net inference is **NP-hard***.

<!--

## Reducing SAT Problems to Bayes Nets

```{=latex}
\begin{center}
```
![](aima-fig-13_14-bayes-net-3cnf.pdf)
```{=latex}
\end{center}
```

## Clustering Algorithms

aka join trees.

```{=latex}
\begin{center}
```
![](aima-fig-13_15-lawn-routine-clustered-bayes-net.pdf)
```{=latex}
\end{center}
```

-->

## Approximate Inference for Bayesian Networks

## Direct Sampling Methods

## Prior Sampling Algorithm

```{=latex}
\begin{center}
```
![](aima-fig-13_16-bayes-net-prior-sample-algorithm.pdf)
```{=latex}
\end{center}
```

## Rejection Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_17-bayes-net-rejection-sampling-algorithm.pdf)
```{=latex}
\end{center}
```

## Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_18-bayes-net-likelihood-weighting-algorithm.pdf)
```{=latex}
\end{center}
```

## Rejection vs. Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_19-performance-plot-rejection-sampling-likelihood-weighting.pdf)
```{=latex}
\end{center}
```

## Markov Chain Monte Carlo (MCMC) Algorithms

Instead of generating each sample from scratch, MCMC algorithms generate a sample by making a random change to the preceding sample. Think of an MCMC algorithm as being in a particular current state that specifies a value for every variable and generating a next state by making random changes to the current state.

## Gibbs Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_20-bayes-net-gibbs-sampling-algorithm.pdf)
```{=latex}
\end{center}
```

## Markov Chains

```{=latex}
\begin{center}
```
![](aima-fig-13_21-markov-chain.pdf)
```{=latex}
\end{center}
```

## Gibbs Sampling vs. Importance Sampling

```{=latex}
\begin{center}
```
![](aima-fig-13_22-performance-plots-gibbs-sampling-likelihood-weighting.pdf)
```{=latex}
\end{center}
```
