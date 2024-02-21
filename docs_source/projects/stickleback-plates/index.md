# Stickleback armor plates

In this project, the number, area and shape of armor plating is measured as a continuous trait using a combination of `threshold`, `watershed` and `edit_contour`.

```{figure} output_stickleback-plates.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

Variation in continuous phenotypic traits like shape or area of certain structures are difficult to quantify in a discrete fashion, e.g. with landmarks, because they are too complex or have no underlying assumption of homology. 

Here, stickleback armor plates and their shape features are detected in a two-step process. First, a mask was set around the posterior region that contains the plates, which is then tresholded. Due to the red staining, the "red channel" contains highest signal-to-noise-ratio, and is thus used (specified in `threshold`). Then, the watershed algorithm is applied to the specified region to erode the area between the plates, which produces another binary image (fed to `detect_contour`). Remaining plate-overlap is removed with the `edit_contour` tool, and `detect_contour` is used a once more to determine the final plate boundaries. 

In the second step, the configuration file is modified to add `compute_shape_featues`, followed by a "silent run" `feedback=False`. By running this second step only after the initial plate separation, the first step with the actual plate segmentation can be run much faster: depending on the number of objects in the image, `compute_shape_featues` can be quite computationally intensive, so running it after the final contours have been detected will speed things up. This is a useful approach also for other scenarios.

The `watershed` algorithm, which helps to separate detected objects into "peaks of wanted information" and "valleys of unwanted information", is explained here: https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html 

**NOTE:** These are the same images as in https://www.phenopype.org/gallery/project_2/ - reference detection and ID-entry are shown there and thus skipped here.


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
```{button-link} https://osf.io/download/rt3z7/
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

