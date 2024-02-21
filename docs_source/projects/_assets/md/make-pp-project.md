## Make phenopype project

Create a phenopype project (remember, `Project` is used to both create new projects, and load existing ones). Different phenopype projects can be useful, e.g., to process different batches of images from field seasons, perspectives, etc,. It makes sense to create them side by side in a subfolder, which I call "phenopype". Thus, my research projects often have the following directory structure (just my way of working - this is really totally up to you):

```{code-cell}
my-project
    data                       # processed data (e.g., tables)
    data_raw                   # raw data (images, videos, etc.)
    phenopype                  # phenopype projects
    phenopype_templates        # phenopype .yaml config templates
    scripts                    # python, R, etc.
    [...]                      # manuscripts, figures, literature, etc.
```