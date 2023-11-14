# Worm length

In this project, the length of california blackworms (*Lumbriculus variegatus*) is measured in 6 well plates, which are detected automatically with the Hough Transform algorithm in `detect_mask`.

```{figure} output_worm-length.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

## Background

Body length is a commonly measured trait. However, live animals are typically not well behaved in front of camera: typically the body is not aligned straight, which makes length measure difficult and sometimes time consuming. Some computer vision can help here, such as [skeletonization](https://en.wikipedia.org/wiki/Topological_skeleton) for an acurate semi automatic approach, and polyline drawing for a less acurate, manual aproach. phenopype's `detect_mask` can automatically detect geometric objects using [Hough transformation](https://en.wikipedia.org/wiki/Hough_transform). It takes a while to specific the right parameters for the circle detection - this configuration proved to be useful for the 6-well plates in the images (already preset in `gallery_project_7.yaml` in the template repo):

```python
- detect_mask:
    ANNOTATION: {type: mask, id: a, edit: overwrite}
    shape: circle
    circle_args: {max_radius: 300, min_radius: 220, param2: 90, param1: 100, min_dist: 400}
    resize: 0.5
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
```{button-link} https://osf.io/download/u7n83/
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

