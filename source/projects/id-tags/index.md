# ID tags

Use a simple phenopype configuration to quickly (~1s per image) label hundreds or thousands of images with ID-tags inside them, and check the label by printing the entry onto a copy of the image. 

```{figure} output_id-tags.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

Many field ecologists rely on simply handwritten or computer-printed labels to assign the ID of collected individuals inside an image during a sampling campaign or when imaging many specimens in the lab. Thus, the first step before any downstream analyses of phenotypes should be to label all individuals to link the images to an existing database and identify duplicates. [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) like Google's Tesseract can be a powerful way to address this challenge.  However, especially in the case of handwritten or inconsistent labels, like the ones shown in the image above, the time needed to set up an OCR pipeline can be more time consuming than quickly labeling a few 1000 or even 10000 images. 
```{figure} https://www.luerig.net/posts/qr-codes/fig1.png
:width: 600px
:align: center

**ID tags inside a picture are essential for quantitative reproducible research!**
```

Given the time for implementation, and that there is always a small margin for error in even the best OCR pipelines, so images would have to be checked manually anyways, phenopype provide a simple solution: minimal interactivity, fast switching of images, and printing the output onto the original image. Experience has shown that even rather large datasets (~15000 images) can be labeled in a few hours or days, reducing the possibility for error to a minimum. 

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
Jupyter notebook <jupyter-notebook-1>
```

