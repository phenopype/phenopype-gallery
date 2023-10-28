# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:30:05 2023

@author: mluerig
"""

#%% imports

import os
import sys
import zipfile
import nbformat
from nbconvert import PythonExporter

## change to current dir
if hasattr(sys, 'ps1'):
    os.chdir(r"D:\git-repos\phenopype\phenopype-gallery")
else:
    os.chdir(sys.path[0])
    
## convert notebook to python script
def convertNotebook(notebookPath, modulePath):

  with open(notebookPath) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  exporter = PythonExporter()
  source, meta = exporter.from_notebook_node(nb)

  with open(modulePath, 'w+') as fh:
    fh.writelines(source)

#%% create zips

print("converting ipynb to py:\n")

project_dir = r"source/projects"

for project in os.listdir(project_dir):
    project_path = os.path.join(project_dir, project)
    if os.path.isdir(project_path):
        print(project)

        path1 = os.path.join(project_path, "jupyter-notebook.ipynb")
        path2 = os.path.join(project_path, "python-script.py")
    
        convertNotebook(path1, path2)

