# QR codes

In this project, phenopype is used to automatically detect QR codes placed in images. There are several options to manually add the information where the procedure failed.

```{figure} output_qr-codes.jpg
:width: 600px
:align: center
```

```{include} ../../_assets/md/get-started.md
```

## Background

Depending on their size/version and the error correction level, [QR codes](https://www.qrcode.com/en/codes/) can store surprising amounts of data: the largest version (40) can store up to 4296 alphanumeric characters (for comparison: a scientific abstract of 220 words contains on average 1500 characters). Even a [micro QR code ](https://www.qrcode.com/en/codes/microqr.html) can store up to 21 alphanumeric or 35 numeric characters. Additionally, QR codes include finder-patterns that help computer vision algorithms to detect the code inside images, an error-correction-patterns that make sure that the contained data gets decoded correctly.

```{figure} qr_codes.png
:width: 400px
:align: center
```

All this makes QR codes highly suitable to encode information in scientific images! The images used in this project were supplemented with QR code tags generated in Python - see my [blogpost on this](https://www.luerig.net/posts/qr-codes/). In case the detection fails (for this project in around 15 images out of 1300), there are several options to label the remaining manually: either by setting `enter_manually: True`, or by finding the images where detection failed, and processing them separately.

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
```{button-link} https://osf.io/download/jdmu6/
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
