"""
Broken axis for morphologically distinct groups
================================================

_thumb: .45, .5

*Iris setosa* has petals 1–2 cm long — roughly half the length of
*I. versicolor* and *I. virginica* (3–7 cm). Plotting all three species
on a single x-axis either compresses the setosa cluster or wastes
most of the axis range. A broken x-axis shows each cluster at full
resolution while making the morphological discontinuity explicit.
"""
import seaborn as sns

sns.set_theme(style="ticks")
iris = sns.load_dataset("iris")

g = sns.BrokenAxes(
    xlims=[(0.8, 2.3), (2.7, 7.2)],
    width_ratios=[1, 3],
    wspace=0.08,
)
g.plot(
    sns.scatterplot,
    data=iris,
    x="petal_length",
    y="petal_width",
    hue="species",
    s=60,
    alpha=0.85,
    legend_ax=g.ax_right,
)
g.set_axis_labels("Petal length (cm)", "Petal width (cm)")
g.fig.set_size_inches(9, 4)
