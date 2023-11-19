# Counting isopods

In this project the goal is to measure measure phenotypic distributions of several specimens of isopods (*Asellus aquaticus*) using the threshold algorithm. We also use image registration to find a reference card and automatically size and color-correct the image.

```{figure} output_isopod-counting.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

This workflow was used for a master's project where we quickly needed to measure the phenotypic distribution (pigmentation as gray scale, and size) before adding multiple batches of live isopods to a predation experiment. Since the isopods were alive and were needed for the experiment, we didn't use a macro-lens but the default wide angle lens.

```{image} ../_assets/images/camera_stand.jpg
:width: 500px
:align: center
```

Details about the imaging gear and protocol can be found a [blog entry on my personal website](https://www.luerig.net/posts/high-throughput-imaging/#1---camera-stand-suitable-for-live-organisms). We photographed the isopods on a camera stand using a computer controlled Canon EOS 750d DLSR with a 15-45mm lens and LED light panels for better illumination. Imaging each batch took about 20-30 seconds, and processing in phenopype roughly 30 seconds per image. 


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
```{button-link} https://osf.io/download/wrm84/
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

