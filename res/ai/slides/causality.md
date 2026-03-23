---
title: Artificial Intelligence
subtitle: Causality
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


## Correlation Does Not Imply Causation

```{=latex}
\centering
\includegraphics[
    height=.6\textheight,
    alt={XKCD cartoon in which a student, after taking a statistics class, is unable to state whether the class caused him to stop believing that correlation implies causation.}]
    {correlation.png}\footnote{\url{https://xkcd.com/552/}}
```

## Nicholas Cage and Pool Deaths

The number of movies that star Nicolas Cage in a year is positively correlated with the number of pool deaths in that year.

```{=latex}
\centering
\includegraphics[
    height=.5\textheight,
    alt={Picture of Nicolas Cage and a pool full of people.}]
    {nicolas-cage-equals-pool-deaths.png}
```

## Ice Cream and Shark Attacks

::: {.columns}
::: {.column width="50%"}

```{=latex}
\centering
\includegraphics[
    height=.5\textheight,
    alt={Picture of Shark's ice cream shop.}]
    {sharks-ice-cream-shop.png}
```

:::
::: {.column width="50%"}

```{=latex}
\centering
\includegraphics[
    height=.5\textheight,
    alt={Plot showing correlation between ice cream sales and shark attacks.}]
    {ice-cream-shark-attacks-correlation.png}
```

\vspace{.25in}
:::
::::

We know that ice cream doesn't cause shark attacks (right?), but perhaps there's something deeper.


## Where there's fire there's smoke.

Smoke and Fire are correlated -- we tend to see them together.  We can represent the full joint distribution over these variables with a Bayesian network.

::: {.columns}
::: {.column width="50%"}

Say we choose the ordering $Fire, Smoke$.  Then we could use the Bayes net on the right and represent the full joint distribution as:

```{=latex}
\[
P(Smoke, Fire) = P(Smoke) P(Fire \mid Smoke)
\]
```

We learned earlier that using a Causal topological ordering gives us a more efficient representation.

:::
::: {.column width="50%"}

```{=latex}
\centering
\vspace{.25in}
\begin{tikzpicture}

\node[draw, shape=ellipse](smoke) at (2, 2){Smoke};
\node[draw, shape=ellipse](fire) at (2, 0){Fire};

\draw[->] (smoke) to (fire);

\end{tikzpicture}
\vspace{.25in}
```

:::
::::

## Where there's smoke there's fire.

::: {.columns}
::: {.column width="50%"}

Say we choose the ordering $Smoke, Fire$.  Then we could use the Bayes net on the right and represent the full joint distribution as:

```{=latex}
\[
P(Fire, Smoke) = P(Fire) P(Smoke \mid Fire)
\]
```

We learned earlier that while using a Causal topological ordering gives us a more efficient representation, any ordering gives us a valid representation of the full joint distribution.

- But does this network pass the smoke test?

:::
::: {.column width="50%"}

```{=latex}
\centering
\vspace{.25in}
\begin{tikzpicture}

\node[draw, shape=ellipse](smoke) at (2, 0){Smoke};
\node[draw, shape=ellipse](fire) at (2, 2){Fire};

\draw[<-] (smoke) to (fire);

\end{tikzpicture}
\vspace{.25in}
```

:::
::::

## Causality Exists

::: {.columns}
::: {.column width="50%"}

We know that this is true:

```{=latex}
\centering
\vspace{.25in}
\begin{tikzpicture}

\node[draw, shape=ellipse](smoke) at (2, 2){Smoke};
\node[draw, shape=ellipse](fire) at (2, 0){Fire};

\draw[->] (smoke) to (fire);

\end{tikzpicture}
\vspace{.25in}
```

:::
::: {.column width="50%"}

and this is not true:

```{=latex}
\centering
\vspace{.25in}
\begin{tikzpicture}

\node[draw, shape=ellipse](smoke) at (2, 2){Smoke};
\node[draw, shape=ellipse](fire) at (2, 0){Fire};

\draw[<-] (smoke) to (fire);

\end{tikzpicture}
\vspace{.25in}
```

:::
::::

But probability theory and Bayes nets cannot represent this causal knowledge.

## Probabilistic Causal Models

Causal networks are a restricted class of Bayesian networks which requires a causal topological ordering.




## Example: Generating a Sample from Sprinkler Bayes Net

:::: {.columns}
::: {.column width="60%"}

We have intervened with do $Sprinkler$, so the link from $Season$ to $Sprinkler$ is removed and $Sprinkler=true$, or $P(Sprinkler=true) = 1$.

:::
::: {.column width="45%"}

```{=latex}
\begin{center}
\includegraphics[
    height=.5\textheight,
    alt={Wet grass Causal network with Season influencing Rain and Sprinkler, Rain and Sprinkler both influencing WetGrass, and WetGrass influencing both GrassShiny and ShoesWet.  We have intervened with do Sprinkler, so the link from Season to Sprinkler is removed and Sprinkler=true, or P(Sprinkler=true) = 1.}
    ]
    {x110b-wet-grass-causal-net-do-sprinkler.png}
\end{center}
```

:::
::::
