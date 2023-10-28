#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebook: counting  isopods
# 
# First, download and unzip the data [from osf.org](https://files.de-1.osf.io/v1/resources/rxubv/providers/osfstorage/65394dd4282745120cb86bcc/?zip=), as well as the yaml template [from GitHub]().
# 
# Then assign the root directory of your phenopype project (usually nested within a folder "phenopype" is good practice), the directory with the downloaded images, and the template 

# In[2]:


import phenopype as pp
import os

## project name directory
root_dir = r"phenopype/isopod-counting"

## directory with images  
image_dir = "data/isopod-counting"

## template
template = "template_isopod-counting.yaml"


# In[3]:


proj = pp.Project(root_dir)


# In[9]:


## add all isopod-images from the data folder
proj.add_files(image_dir = image_dir, include="isopods", mode="link")

## add the config template; provide a tag
proj.add_config(template_path=template, tag="v1", overwrite=True)


# Now, add a reference, like this:
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/measure-reference.gif)
#         
# </div>
# </center>

# In[ ]:


## set the project-wide reference. the reference has its own tag, in case your project uses multiple reference cards
proj.add_reference(reference_image_path= os.path.join(image_dir,"isopods1.jpg"), reference_tag="iso-scale")


# Now, run the project as 

# In[ ]:


for path in proj.dir_paths:
    pp.Pype(path, tag="v1")


# Changing `blocksize` and `constant` on the thresholding algorithm has a great effect on the result. This becomes evident when looking at the binarized image, which is a great way to assess effectivness of the thresholding procedure. You can create such images directly in the `Pype` routine, by selecting `canvas: mod` in `- select_canvas`
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/thresholding.jpg)
#     
# </div>
# </center>

# In[ ]:


## collect results and store in folder "<project-root>/results/annotations"
proj.collect_results("v1", "annotations", "annotations")


# In[ ]:


## display results
import ipyplot ## install with `pip install ipyplot`

canvas_list = []
for path in proj.dir_paths:
    canvas_list.append(pp.load_image(os.path.join(path, "canvas_v1.jpg"), mode="rgb"))

ipyplot.plot_images(canvas_list, img_width=500)


# In[ ]:




