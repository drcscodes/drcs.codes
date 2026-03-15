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


## Causality


```{=latex}
\begin{center}
\includegraphics[
    height=.5\textheight,
    alt={Wet grass Bayes net with Season influencing Rain and Sprinkler, Rain and Sprinkler both influencing WetGrass, and WetGrass influencing both GrassShiny and ShoesWet}
    ]
    {x110a-wet-grass-bayes-net.png}
\end{center}
```


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
