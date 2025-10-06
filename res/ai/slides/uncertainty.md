---
title: Artificial Intelligence
subtitle: Uncertainty
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

## Acting Under Uncertainty

Logical agents maintain a belief state and generate contingency plans that account for every possibility.  This breaks down for nontrivial problems due to:

- Exhaustivity of belief state, which must contain all possible states, even unlikely states.
- Exhaustivity of contingency plan, which must account for every possible, however unlikely, action outcome.
- Unsatisfiabilty.  There may be no guranteed plan to achieve the goal.  If we must actu anyway, how do we choose the best plan?
- Qualification problem.  The closed-world assumption allows us to simplify logical environment specifications for simple domains, but real-world domains contain far more detail which must be accounted for.

Rational decision under uncertainty depends on:

- relative importance of goals,
- likelihood of achieving goals, and
- degree to which goals can be achieved.

## From Logic to Probability Theory

Consider:

$Toothacke \implies Cavity$

Not all patients with toothaches have cavities.  How about:

$Toothache \implies Cavity \lor GumProblem \lor Abscess \dots$

We'd need large list after the dots.  Try causal direction:

$Cavity \implies Toothache$

But not all cavities hurt.  Logic fails to deal with complex domains like medical diagonosis due to:

- **Exhaustivity** (laziness).  Too many antecedents or consequents to list.
- **Theoretical ignorance**. Rare to have complete logical theory of nontrivial domain.
- **Practical ignorance**.  Even with a complete domain theory, hard to measure all the necessary inputs (medical tests, etc.)

We need to deal with uncertain knowledge, with **degrees of belief**.  For that, we use probability theory.

## Probability Theory as Knowledge Representation

- Ontological commitments of logic and probability theory same:

    - World composed of facts that do or do not hold in any particular case.

- Epistemological commitments differ:

    - Logic assigns true, false, or no opinion to each sentence.
    - Probability theory assignesnumerical degree of belief between 0 (for sentences that are certainly false) and 1 (certainly true) to each sentence.

Probability theory solves the qualification problem by summarizing the uncertainty stemming from our laziness and ignorance.

## What do probabilities mean?

![](neo-architect-prob-dist-screens.png)

## Probabilities are about our uncertain knowledge.


"80% chance (probability 0.8) patient with a toothache has a cavity."

- Out of all the situations that are indistinguishable from the current situation *as far as our knowledge goes*, the patient will have a cavity in 80% of them.
- Belief could come from statistical data, or domain theory, or combination of sources.

> There is no uncertainty in the actual world.  The patient either has a cavity or does not. Probabilities refer to our knowledge of the world state, not the actual world state.

If our knowledge changes, e.g., we find out patient has history of gum disease, we make a different statement.

"Given patient has a history of gum disease and a toothache, 40% chance patient has gum disease."

## Rational Decisions

How do we choose between different plans that acheive the goal?

- Each plan has a likelihood of success, e.g.:

    - Plan A has a 95% chance of achieving a goal state.

- Each plan may lead to goal states with different outcomes, each of which is a goal state.

    - An **outcome** is a completely specified state.

Elements of outcomes are more or less desirable -- more or less *useful* -- to a given agent:

- utility: the quality of being useful.

Utility theory associates a utility value with each possible outcome, which induces a preference ordering over outcomes.

> An agent is rational if and only if it chooses the action that yields the highest expected utility, averaged over all the possible outcomes of the action.

## Decision-Theoretic Agents

```{=latex}
\begin{center}
Decision theory = probability theory + utility theory
```
![](aima-fig-12_01-dt-agent-algorithm.pdf)
```{=latex}
\end{center}
```

Each action, $a$, leads to a probability distribution over outcomes, or "result states":

```{=latex}
$$
\sum_{s \in S} Pr(s) = 1
$$
```

And each outcome state has a utility.  A rational decision-theoretic agent chooses the action that maximize expected utility, that is:

```{=latex}
$$
\argmax_{a} \sum_{s \in S} Pr(s) U(s)
$$
```

## Probability Models

In logic we have satisfiabilty: $M(\alpha)$ is the set of all possible worlds in which sentence $\alpha$ is true.

In probability theory the set of possible worlds is a **sample space**, which must be mutually exclusive and exhaustive.


```{=latex}
$$
0 \le Pr(\omega) \le 1 \text{ for every } \omega \text{ and } \sum_{\omega \in \Omega} Pr(\omega) = 1
$$
```

An **event** is a set of possible worlds, e.g., "probability two dice sum to 6."

A **proposition** is an event expressed in a formal language; specifically, for each proposition, the corresponding set contains just those possible worlds in which the proposi- tion holds.

The probability associated with a proposition is defined to be the sum of the probabilities of the worlds in which it holds:

$$
\text{For any proposition } \phi, Pr(\phi) = \sum_{\omega \in \phi} Pr(\omega)
$$

## Prior and Conditional Probabilities

Unconditional or Prior probabilities

Conditional or posterior probabilities

$$
Pr(a | b) = \frac{Pr(a \land b)}{Pr(b)}
$$

Product rule

$$
Pr(a \land b) = Pr(a | b) Pr(b)
$$

## Probability Assertions

Factored representaiton

Random variables

Probability distribution

probability density function



## Joint Probability Distributions

## Probability Axioms



## Agent Beliefs Bets


```{=latex}
\begin{center}
```
![](aima-fig-12_02-agent-bets.pdf)
```{=latex}
\end{center}
```

## Inference Using Full Joint Distributions


```{=latex}
\begin{center}
```
![](aima-fig-12_03-full-joint-toothache.pdf)
```{=latex}
\end{center}
```

## Factoring Joint Distibutions Using Independence


```{=latex}
\begin{center}
```
![](aima-fig-12_04-factoring-independence.pdf)
```{=latex}
\end{center}
```


## Uncertain Reaasoning in the Wumpus World


```{=latex}
\begin{center}
```
![](aima-fig-12_05-wumpus-query.pdf)
```{=latex}
\end{center}
```

## MOdel Checking in the Uncertain WUmpus WOrld


```{=latex}
\begin{center}
```
![](aima-fig-12_06-wumpus-models.pdf)
```{=latex}
\end{center}
```
