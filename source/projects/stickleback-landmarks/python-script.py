#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebook: place landmarks on stickleback

# First, if you haven't already done so, download the images and unzip them to the same folder as this notebook. Then import phenopype and assign some directoy and file names: 

# In[1]:


import phenopype as pp
import os

root_dir = r"phenopype"                ## project root dir
image_dir = "images"                   ## folder with images
template = "template-config.yaml"      ## image processing instructions


# In[3]:


proj = pp.Project(project_name)


# In[5]:


## add all stickleback-images from the data folder, but exclude the two that don't belong to the series 
proj.add_files(image_dir = image_dir, include="stickle", exclude=["side","top"])


# In[6]:


## add the config template; provide a tag
proj.add_config(template_path=template_path, tag="v1", overwrite=True)


# Add a project-wide size and color reference that will be detected in the images:
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/measure-reference.gif)
#         
# </div>
# </center>

# In[8]:


## set the project-wide reference. the reference has its own tag, in case your project uses multiple reference cards
proj.add_reference(reference_image_path= os.path.join(image_dir,"stickleback_side.jpg"), reference_tag="stickle-scale")


# Finally, loop through the images of the project with the `Pype` class and place the landmarks. You can modify, for instance, point size and colour for the landmarks while adding them (or before adding the template). Note that point characteristics need to be changed separately for setting the landmarks and visualizing them (this goes for all GUI-annotations like masks, lines, etc.).
# 
# <center>
# <div style="width:600px; text-align: left">
#     
# ![](_assets/place-landmarks.gif)
#     
# </div>
# </center>

# In[9]:


## run image processing
for path in proj.dir_paths:
    pp.Pype(path, tag="v1")


# In[10]:


## collect results and store in folder "<project-root>/results/annotations"
proj.collect_results("v1", "annotations", "annotations")

