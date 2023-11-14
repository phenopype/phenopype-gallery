# Cichlid teeth

This example demonstrates how shape features of fish teeth are extracted from images containing single and multiple microscope images. Two separate phenopype projects are shown here: one with a single tooth and and one for multiple teeth per each image. 

```{figure} output_cichlid-teeth.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```
4) Install the fastSAM plugin for phenopype:


- get repo: `git clone https://github.com/CASIA-IVA-Lab/FastSAM`
- `cd FastSAM`
- ~~pip install -r requirements.txt~~ `# not needed if torch is installed separately`
- install CLIP: `pip install git+https://github.com/openai/CLIP.git`



## Background

These are single-tooth images where the background is sometimes brighter than the teeth, sometimes darker, and also somewhat noisy. The challenges here lie in preventing unwanted objects from being detected (e.g. the checkered paper and sediment bits). This makes it hard for signal processing, but the SAM algorithm is very good at detecting edges, so it should be able to deal with this variation. We need to load the fastSAM repo to the Python path before loading phenopype so it is recognized and the plugin properly loaded.

```{figure} cichlid-jaw.jpg
:width: 400px
:align: center
```

## Jupyter notebooks

::::{grid} 3
:gutter: 2

:::{grid-item-card} Jupyter notebook 1 (single tooth)
:link: jupyter-notebook-1
Read a static html render of a jupyter notebook
:::

:::{grid-item-card} Jupyter notebook 2 (multile teeth)
:link: jupyter-notebook-2
Read a static html render of a jupyter notebook
:::

::::


## Downloads

::::{grid} 3
:gutter: 2

:::{grid-item-card} Project materials
Download data, scripts, and template
+++
```{button-link} https://osf.io/download/gakh3/
:color: primary
:outline:
:expand:

Download
```
:::

::::
```{toctree}
:hidden:
Jupyter notebook 1 <jupyter-notebook-1>
Jupyter notebook 2 <jupyter-notebook-2>
```
