# Introduction

## Background

This workflow was used for a master's project where we quickly needed to measure the phenotypic distribution (pigmentation as grayscale, and size) before adding multiple batches of live isopods to a predation experiment. Since the isopods were alive and were needed for the experiment, we didn't use a macro-lens but the default wide angle lens.

In this project the goal is to measure measure phenotypic distributions of several specimens of isopods (*Asellus aquaticus*) using the threshold algorithm. We also use image registration to find a reference card and automatically size and color-correct the image.


## Imaging setup

Details about the imaging gear and protocol can be found a [blog entry on my personal website](https://www.luerig.net/posts/high-throughput-imaging/#1---camera-stand-suitable-for-live-organisms). We photographed the isopods on a camera stand using a computer controlled Canon EOS 750d DLSR with a 15-45mm lens and LED light panels for better illumination. Imaging each batch took about 20-30 seconds.  

```{image} _assets/camera_stand.jpg
:width: 500px
:align: center
```

## Processing time in phenopype

Roughly 30 seconds per image.
