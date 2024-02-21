# phenopype gallery

Welcome to the phenopype gallery! It's purpose is to showcase a range of image-analysis-problems that can be solved with phenopype. To get started, read the general [instructions](instructions), then check out the projects below: each project comes with a jupyter notebook, and some toy data to reproduce the shown results. Data and code are available for download, and as read-only html version. 

If you found a bug in the package or any of these materials, please report it through the [issue tracker](https://github.com/phenopype/phenopype/issues) in the main phenopype repo on GitHub.

::::{grid} 3
::::{grid-item}
:::{card}
**✨ = AI-enabled projects**
:::
:::
::::



---

# Projects

## Labeling

Add text labels for classes and IDs to whole images and objects within

::::{grid} 3
:gutter: 2

:::{grid-item-card} ID tags
:link: projects/id-tags/index
:img-top: _assets/images/thumbs/id-tags.jpg

- rapid manual labeling of IDs
:::


:::{grid-item-card} QR-codes  
:link: projects/qr-codes/
:img-top: _assets/images/thumbs/qr-codes.jpg

- automatic detection of QR codes
- manual labeling of unsuccessful detections
:::

::::

## Landmarks

Manual and automatic placement of landmarks, pseudo-landmarks and other annotations for geometric morphometrics

::::{grid} 3
:gutter: 2

:::{grid-item-card} Stickleback landmarks
:link: projects/stickleback-landmarks/
:img-top: _assets/images/thumbs/stickleback-landmarks.jpg

- place landmarks on stained stickleback
- automatic size correction
+++
*Gasterosteus aculeatus*
:::

::::


## Object detection and counting

Detecting many small objects against a uniform background for counting, and collect some simple traits from each object 

::::{grid} 3
:gutter: 2

:::{grid-item-card} Fluorescence traits in algae
:link: projects/phytoplankton-fluorescence/
:img-top: _assets/images/thumbs/phytoplankton-fluorescence.jpg

- cell segmentation and counting
- extraction of shape and pattern traits from individual cells
+++
Phytoplankton communities
:::

:::{grid-item-card} Isopod counting
:link: projects/isopod-counting/
:img-top: _assets/images/thumbs/isopod-counting.jpg

- count small critters 
- quantify size and pigmentation 
- automatic size/color correction
+++
*Asellus aquaticus*
:::

:::{grid-item-card} Snail counting
:link: projects/snail-counting/
:img-top: _assets/images/thumbs/snail-counting.jpg

- count small freshwater snails
- measure size and pigmentation
+++
*Potamopyrgus antipodarum*
:::

:::{grid-item-card} ✨ Cichlid teeth
:link: projects/cichlid-teeth/
:img-top: _assets/images/thumbs/cichlid-teeth.jpg

- segment teeth against dark and light backgrounds 
- extract shape features
+++
Chichlid communities
:::

:::{grid-item-card} Measure worm length
:link: projects/worm-length/
:img-top: _assets/images/thumbs/worm-length.jpg

- find circles (well plates) in images
- detect worm within circle, and measure length
+++
*Lumbriculus variegatus*
:::

::::

## Phenomics

Collect high dimensional traits from single specimens in high resolution images, e.g., tangible and abstract shape and color pattern / texture features

::::{grid} 3
:gutter: 2

:::{grid-item-card} Stickleback armor plate measurement
:link: projects/stickleback-landmarks/
:img-top: _assets/images/thumbs/stickleback-plates.jpg

- thresholding of armor plates
- extract size and shape
+++
*Gasterosteus aculeatus*
:::

:::{grid-item-card} ✨ Damselfly morphology
:link: projects/damselfly-phenomics/
:img-top: _assets/images/thumbs/damselfly-phenomics.jpg

- create training data
- segment the whole body and body parts using deep learning
- extract shape and texture traits from each part
+++
*Ischnura elegans*
:::

::::


## Video analysis

Tracking of individuals from videos with a static background

::::{grid} 3
:gutter: 2

:::{grid-item-card} Motion tracking
:link: projects/motion-tracking/
:img-top: _assets/images/thumbs/motion-tracking.jpg

- mapping out predator-prey interactions between isopods and fish
+++
*Gasterosteus aculeatus* + *Asellus aquaticus*
:::

::::


```{toctree}
:maxdepth: 1
:hidden:
:caption: Internal links

instructions
projects/index
sandbox/index
```

