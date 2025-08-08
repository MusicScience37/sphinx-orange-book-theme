---
file_format: mystnb
---

# Test of myst-nb, myst-parser in md file

## Simple calculation

```{code-cell}
1 + 1
```

## Use of plotly package

```{code-cell}
import plotly.express
import plotly.graph_objects

fig = plotly.express.line(x=[1, 2, 3], y=[3, 5, 4])
fig.show(renderer="notebook_connected")
```

## Math equations

$$
\exp(i\pi) = -1
$$

An inline equation: $\sqrt{2} = 1.414213562$

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

$$
\|\bm{a}\|^2 + \|\bm{b}\|^2 = \|\bm{c}\|^2
$$

## Directive

```{note}
Test of `note` directive.
```
