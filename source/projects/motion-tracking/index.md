# Motion tracking

Use the motion tracking module of phenopype to record movement of a prey population (isopods) in response to a stickleback, and create movement profiles of individuals using the trackpy library. 

```{figure} output_motion-tracking.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

This example features analysis of predator-prey interactions of one threespine stickleback (*Gasterosteus aculeatus*) and 20 benthic isopods (*Asellus aquaticus*). The goal is to extract movement trajectories of both species in response to each other, to see if isopods are reacting to the fish, and the other way round. At the same time, isopod pigmentation is measured in every frame to measure whether the fish has preferences for a particular phenotype (dark vs. light pigmentation, large bodied individuals). An animation of all detected trajectories with the given settings can be found on vimeo: 

```{vimeo} 283075068
:align: center
```
<https://vimeo.com/283075068>

The workflow with videos is a bit different than for images: 

1. Create `motion_tracker` class
2. Tie in a video stream
3. Attach a `tracking_method` (in this case, one for isopods and one for the fish)
4. Set global detection settings
5. Run tracking (watch it or go drink a coffee)
6. Extract the coordinates of the detection, and use [trackpy](https://soft-matter.github.io/trackpy) to calculate the trajectories


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
```{button-link} https://osf.io/download/qsuh7/
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

