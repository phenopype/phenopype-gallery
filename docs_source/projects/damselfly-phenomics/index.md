# Damselfly morphology

Here the goal is to great two sets of annotations for images of the common bluetail damselfly (*Ischnura elegans*): first, segment the insect body (without wings and legs), and then, further divide the segmentation mask of the body into 4 body parts (head, pronotum, thorax, abdomen). I will also demonstrate the use of the trained model, which makes the segmentation process much faster!  

```{figure} output_damselfly-phenomics.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background 

The common bluetail damselfly (*Ischnura elegans*) expresses remarkably stable female-limited color polymorphisms across natural populations in Skane (Fig. 1). Females of *I. elegans* go through a series of abdominal color changes during development, which results in three female color morphs: one androchrome morph and two gynochrome morphs (infuscans and infuscans-obsoleta). One hypothesized mechanism thought to stabilize sexual polymorphisms in nature is correlational selection, which occurs when multiple traits (e.g. coloration, morphology or behavior) affect fitness in an interactive way

```{figure} damselfly-polymorphism.jpg
:width: 400px
:align: center
```

After segmenting the different body parts with the trained models (one for the whole body, and one for the body parts) I use phenopype to collect large arrays of shape and texture features from all images in the dataset. With these data I will visualize the different morphs in multidimensional trait space (=morphospace) and explore how discrete or continuous the color polymorphism really is, and how strongly variation in texture traits is related to variation in shape traits. After the paper is submitted for review I will make the segmentation model available, so this workflow will become AI-enabled and free to use for everyone. 

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

