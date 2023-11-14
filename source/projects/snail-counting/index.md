# Counting snails

In this project thresholding and watershed algorithms are applied to count freshwater snails, and moreover, shape and pigmentation are quantified with `compute_shape_features` and `compute_texture_features`.

```{figure} output_snail-counting.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

Just like in the example before, segmentation and feature detection are a two-step process. First, a mask is set around tray, the reference is set manually (the detection algorithm only works on reference cards with clear boundaries, and not on "continuous" mm-paper), and then thresholding and watershed algorithm are applied. Remaining overlap is removed with the `edit_contour` tool, and `detect_contour` is used a once more to determine the final specimen contours. 

In the second step, the configuration file is modified to add `compute_shape_featues` and `compute_texture_features`, followed by a "silent run" `feedback=False`. 

For more information regarding this procedure also check in https://www.phenopype.org/gallery/example_5/.


## Jupyter notebooks

::::{grid} 3
:gutter: 2

:::{grid-item-card} Jupyter notebook
:link: jupyter-notebook-1
Read a static html render of a jupyter notebook
:::

::::


## Downloads

::::{grid} 3
:gutter: 2

:::{grid-item-card} Project materials
Download data, scripts, and template
+++
```{button-link} https://osf.io/download/wat2s/
:color: primary
:outline:
:expand:

Download
```
:::

::::


```{toctree}
:hidden:
Jupyter notebook <jupyter-notebook-1>
```

