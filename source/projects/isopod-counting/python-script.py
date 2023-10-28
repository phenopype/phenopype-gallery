#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebook: counting  isopods

# First, if you haven't already done so, download the images and unzip them to the same folder as this notebook. Then import phenopype and assign some directoy and file names: 

# In[1]:


import phenopype as pp
import os

root_dir = r"phenopype"                ## project root dir
image_dir = "images"                   ## folder with images
template = "template-config.yaml"      ## image processing instructions


# Now, create a phenopype project, and add images and config:

# In[2]:


proj = pp.Project(root_dir)


# In[3]:


proj.add_files(image_dir = image_dir)
proj.add_config(template_path=template, tag="v1")


# Add a project-wide size and color reference that will be detected in the images:
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/measure-reference.gif)
#         
# </div>
# </center>

# In[4]:


## set the project-wide reference. the reference has its own tag, in case your project uses multiple reference cards
proj.add_reference(reference_image_path=os.path.join(image_dir,"isopods1.jpg"), reference_tag="iso-scale")


# Finally, loop through the images of the project with the `Pype` class. First, create a mask around all specimens, then edit any errors to the contours if necessary:
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/draw-mask.gif)
#         
# </div>
# </center>

# In[5]:


for path in proj.dir_paths:
    pp.Pype(path, tag="v1")


# Some comments on the settings: changing `blocksize` and `constant` on the threshold algorithm has a great effect on the result. This becomes evident when looking at the binarized image, which shows increasing blocksizes. You can inspect the binary images yourself by selecting `canvas: mod` in `- select_canvas`
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/thresholding.jpg)
#     
# </div>
# </center>

# Once you're done, collect the results 

# In[6]:


## collect results and store in folder "<project-root>/results/annotations"
proj.collect_results("v1", "annotations", "annotations")


# In[ ]:



