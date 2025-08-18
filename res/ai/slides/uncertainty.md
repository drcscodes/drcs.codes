---
title: Uncertainty
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

## Farva

```{=latex}
\begin{center}
\includemedia[
    width=0.6\linewidth,height=0.6\linewidth,
    activate=pageopen,
    transparent,
    addresource=../../ChrisSimpkinsIsAChickenF.mp4,
    flashvars={
      source=../../ChrisSimpkinsIsAChickenF.mp4     % same path as in addresource!
     &loop=false           % loop video
     &scaleMode=letterbox % preserve aspect ratio
    }
  ]{}{VPlayer.swf}
\end{center}
```

## Acting Under Uncertainty

Belief state

qualification problem

rational decision

## From Logic to Uncertainty

Problems:
- exhaustivity
- theoretical ignorance
- practical ignorance

degree of belief

probability theory

ontological commitments

epistemological commitments


Probabilities refer to our knowledge of the world state, not the actual world state.

## Rational Decisions

Outcomes

Preferences

utility: the quality of being useful.
Utility theory: quantitative representation of preferences
associate a utility with each possible outcome, which induces a preference ordering


Decision theory

Maximum expected utility

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

Sample space

event probabilities

```{=latex}
$$
0 \le Pr(\omega) \le 1 \text{ for every } \omega \text{ and } \sum_{\omega \in \Omega} Pr(\omega) = 1
$$
```
