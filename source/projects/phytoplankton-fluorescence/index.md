# Phytoplankton fluorescence and shape



```{figure} output_phytoplankton-fluorescence.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

A plate reader creates four images of the same set of objects: bright field gray scale images, and three different fluoresccence channels to represent different photopigments. All four images show the same objects, but with different pixel intensities. We will use the contour outline from the brightfield images, which are processed with the high-throughput workflow, as a stencil to extract texture information from the same coordinates in the fluorescence channels.

```{figure} phytoplankton-fluorescence_stencil.jpg
---
width: 600px
---
Each sample includes four images: 1 brightfield (top) and 3 fluorescence measurements (black, bottom). Due to different pigments, not all spcecies are visible in each image, because of different emission spectra. For example, the two long string shaped cells marked with the green circles only occur in two of the fluorescence channels, but not the third one or the brightfield. 
```

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
```{button-link} https://osf.io/download/dqnpr/
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

