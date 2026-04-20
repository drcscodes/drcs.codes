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


## From Logic to Probability Theory

Consider:

$$
Toothacke \implies Cavity
$$

Not all patients with toothaches have cavities.  How about:

$$
Toothache \implies Cavity \lor GumProblem \lor Abscess \dots
$$

We'd need large list after the dots.  Try causal direction:

$$
Cavity \implies Toothache
$$

But not all cavities hurt.  Logic fails to deal with complex domains like medical diagonosis due to:

- **Exhaustivity** (laziness).  Too many antecedents or consequents to list.
- **Theoretical ignorance**. Rare to have complete logical theory of nontrivial domain.
- **Practical ignorance**.  Even with a complete domain theory, hard to measure all the necessary inputs (medical tests, etc.)

We need to deal with uncertain knowledge, with **degrees of belief**.  For that, we use probability theory.

## What do probabilities mean?

![](neo-architect-prob-dist-screens.png)

## Probabilities are about our uncertain knowledge.

"80% chance (probability 0.8) patient with a toothache has a cavity."

- Out of all the situations that are indistinguishable from the current situation *as far as our knowledge goes*, the patient will have a cavity in 80% of them.
- Belief could come from statistical data, or domain theory, or combination of sources.

> There is no uncertainty in the actual world.  The patient either has a cavity or does not. Probabilities refer to our knowledge of the world state, not the actual world state.

If our knowledge changes, e.g., we find out patient has history of gum disease, we make a different statement.

"Given patient has a history of gum disease and a toothache, 40% chance patient has gum disease."

## Decision-Theoretic Agents

> Decision theory = probability theory + utility theory

```{=latex}
\begin{center}
```
![](aima-fig-12_01-dt-agent-algorithm.pdf){height="30%"}
```{=latex}
\end{center}
```

Each action, $a$, leads to a probability distribution over outcomes, or "result states":

```{=latex}
$$
P(\text{RESULT}(a) = s') = \sum_{s \in S} P(s) P(s' \mid s, a)
$$
```

And each outcome state has a utility.  A rational decision-theoretic agent chooses the action that maximize expected utility, that is:

```{=latex}
$$
\argmax_{a} \sum_{s' \in S} P(\text{RESULT}(a) = s') U(s')
$$
```

## Propositions and Events

An **event**, which we denote with $\phi$ here, is a set of possible worlds, some subset of $\Omega$, or set of $\omega$, e.g., the event "doubles" contains the 6 boxed elements $\omega$:

```{=latex}
\footnotesize
\begin{tabular}{cccccc}
\boxed{(1, 1)} & (2, 1) & (3, 1) & (4, 1) & (5, 1) & (6, 1)\\
(1, 2) & \boxed{(2, 2)} & (3, 2) & (4, 2) & (5, 2) & (6, 2)\\
(1, 3) & (2, 3) & \boxed{(3, 3)} & (4, 3) & (5, 3) & (6, 3)\\
(1, 4) & (2, 4) & (3, 4) & \boxed{(4, 4)} & (5, 4) & (6, 4)\\
(1, 5) & (2, 5) & (3, 5) & (4, 5) & \boxed{(5, 5)} & (6, 5)\\
(1, 6) & (2, 6) & (3, 6) & (4, 6) & (5, 6) & \boxed{(6, 6)}\\
\end{tabular}
\normalsize
```

<!--

## THIS IS COMMENTED OUT

foo

bar

## THIS IS ALSO COMMENTED OUT

baz

bang

-->


## Analysis of Medical Screening Example

:::: {.columns}
::: {.column width="30%"}


```{=latex}
\begin{align*}
P(C=1)     &= \frac{1}{100} \\
P(C=0)     &= \frac{99}{100}\\
P(T=1 \mid C=1) &= \frac{90}{100}\\
P(T=0 \mid C=1) &= \frac{10}{100}\\
P(T=1 \mid C=0) &= \frac{3}{100} \\
P(T=0 \mid C=0) &= \frac{97}{100}
\end{align*}
```

:::
::: {.column width="70%"}

If we screen someone, probability that they test positive (notice use of product rule: $P(a, b) = P(a \mid b) P(b)$ and rule 2nd Kolmogorov axiom $P(x \lor y) = P(x) + P(y) - P(x \land y)$):

```{=latex}
\vspace{-.1in}
\begin{align*}
P(T=1) &= P(T=1 \mid C=0)P(C=0) + P(T=1 \mid C=1)P(C=1)\\
       &= \frac{3}{100} \times \frac{99}{100} + \frac{90}{100} \times \frac{1}{100}\\
       &= \frac{387}{10,000}\\
       &= .0387
\end{align*}
```

If someone tests positive, probability they have cancer :

```{=latex}
\vspace{-.1in}
\begin{align*}
P(C=1 \mid T=1) &= \frac{P(T=1 \mid C=1)P(C=1)}{P(T=1)}\\
           &= \frac{90}{100} \times \frac{1}{100} \times \frac{10,000}{387} \\
           &= \frac{90}{387}\\
           &\approx 0.23
\end{align*}
```

:::
::::
