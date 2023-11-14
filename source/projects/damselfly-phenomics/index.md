# Damselfly morphology

In this project, phenopype is used to place morphometric landmarks across the anterior half of threespine stickleback stained with alizarin red. 

```{figure} output_damselfly-phenomics.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background 

The common bluetail damselfly (*Ischnura elegans*) expresses remarkably stable female-limited colour polymorphisms across natural populations in Skane (Fig. 1). Females of *I. elegans* go through a series of abdominal colour changes during development, which results in three female colour morphs: one androchrome morph and two gynochrome morphs (infuscans and infuscans-obsoleta). One hypothesized mechanism thought to stabilize sexual polymorphisms in nature is correlational selection, which occurs when multiple traits (e.g. colouration, morphology or behavior) affect fitness in an interactive way

```{figure} damselfly-polymorphism.jpg
:width: 400px
:align: center
```
Frequency dependent sexual polymorphisms in Ischnura elegans. Females of *I. elegans* have three female colour morphs: A (androchrome = male mimicking), I (infuscans) and O (infuscans obsoleta). Selection on multiple traits, i.e., correlational selection, is hypothesized to stabilize morph frequencies over time.

To investigate correlational selection as a stabilizing agent for sexual polymorphisms, a comprehensive analysis of multivariate phenotypes is needed to understand the phenotypic consequences of correlational selection in polymorphic systems. To do so, shape and texture traits are extracted from a large dataset containing images of damselflies belonging to different populations in Skane - this work is conducted by [Prof. Erik Svensson and his group](https://portal.research.lu.se/en/persons/erik-svensson). 

The segmentation labels that are created with this phenopype configuration will be used to collect training data (from ~ 1500 imgs) to implement a convolutional neural network to perform semantic segmentation on the entire dataset (~ 20000 imgs). However, as an intermediate goal, shape and texture features are extracted to get a first glimpse of how well the collected multivariate, [phenomic data](https://www.frontiersin.org/articles/10.3389/fevo.2021.642774/full) fit the expectations.

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
```{button-link} https://osf.io/download/qjwne/
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

