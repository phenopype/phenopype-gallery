# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:30:05 2023

@author: mluerig
"""

#%% imports

import os
import sys
import zipfile
import argparse

import nbformat
import shutil

from nbconvert import PythonExporter
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

#%% setup

## set paths
git_root_dir = "D:\git-repos\phenopype\phenopype-gallery"
git_project_dir = os.path.join(git_root_dir, r"docs_source\projects")
git_asset_dir = os.path.join(git_root_dir, r"docs_source\projects\_assets")

exec_root_dir = "D:\science\packages\phenopype\phenopype-gallery_exec"
exec_notebook_dir = os.path.join(exec_root_dir, "notebooks")
exec_script_dir = os.path.join(exec_root_dir, "scripts")
exec_template_dir = os.path.join(exec_root_dir, "phenopype_templates")
exec_asset_dir = os.path.join(exec_root_dir, "_assets")
exec_zip_dir = os.path.join(exec_root_dir, r".local\zips")

os.chdir(exec_root_dir)

if not os.path.isdir(exec_zip_dir):
    os.makedirs(exec_zip_dir)
    
## args
if not hasattr(sys, 'ps1'):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--upload-gdrive",
        type=bool,
        help="upload to google drive",
        default=False,
    )
    parser.add_argument(
        "--upload-gdrive-ow",
        type=bool,
        help="update files on google drive",
        default=False,
    )
    parser.add_argument(
        "--compile-zips",
        type=bool,
        help="compile zips",
        default=False,
    )
    parser.add_argument(
        "--find-notebooks",
        type=bool,
        help="find notebooks and copy over to github repo",
        default=False,
    )
    args = parser.parse_args()
    
else:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.find_notebooks = True
    args.compile_zips = True
    args.upload_gdrive = False
    args.upload_gdrive_ow = False
    print(args)

    
## gdrive auth
if args.upload_gdrive or args.upload_gdrive_ow:
    
    gauth = GoogleAuth() 
    gauth.LocalWebserverAuth()        
    drive = GoogleDrive(gauth) 
    args.upload_gdrive = True
    
if args.upload_gdrive:
    args.compile_zips = True
    
    
#%% functions

## find ID of gdrive objects by name and parent ID
def find_gdrive_file_ID(drive, parent_id, filename):
    """
    Find a Google Drive File ID.
    Parameters
    ----------
    drive: GoogleDrive object
    parent_id : str
        Parent folder File ID
    filename : str
        filename of the file to be found
    Returns
    -------
    str
        Google Drive File ID
    None
        if the file doesn't exist
    """
    file_list = drive.ListFile(
        {'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    if file_list and len(file_list) != 0:
        for file in file_list:
            if filename.lower() == file['title'].lower():
                file_id = file['id']
                return file_id
    return None
    
## convert notebook to python script
def convertNotebook(notebookPath, modulePath):

  with open(notebookPath) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  exporter = PythonExporter()
  source, meta = exporter.from_notebook_node(nb)

  with open(modulePath, 'w+') as fh:
    fh.writelines(source)
    

#%% deploy loop

## find notebooks
notebook_paths = []
for notebook_name in os.listdir(exec_notebook_dir):
    notebook_paths.append(os.path.join(exec_notebook_dir, notebook_name))
    
## find templates
template_paths = []
for template_name in os.listdir(exec_template_dir):
    template_paths.append(os.path.join(exec_template_dir, template_name))
    
## go through projects
for project_name in os.listdir(git_project_dir):
    git_project_path = os.path.join(git_project_dir, project_name)
    if os.path.isdir(git_project_path):
        
        ## find different notebook versions
        notebook_paths_copy = []
        for notebook_path in notebook_paths:
            if notebook_path.endswith(".ipynb") and project_name in notebook_path:
                notebook_paths_copy.append(notebook_path)
                
        ## find different template versions
        template_paths_copy = []
        for template_path in template_paths:
            if project_name in template_path:
                template_paths_copy.append(template_path)
                
        ## start zip file
        if args.compile_zips:
            zip_path = os.path.join(exec_zip_dir, project_name + ".zip")
            archive = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
            
            ## data
            data_dir = os.path.join("data_raw", project_name)
            if os.path.isdir(data_dir):
                archive.write(data_dir, arcname="data")    
                for file in os.listdir(data_dir):
                    archive.write(os.path.join(data_dir, file),
                                  arcname=os.path.join("data", file))
                    
            ## template
            for template_path in template_paths_copy:
                archive.write(template_path, arcname=os.path.basename(template_path))    
              
        ## prep copying to git dir
        print(f"processing {project_name}")
        for idx, notebook_path_src in enumerate(notebook_paths_copy):
            notebook_dst_name = "jupyter-notebook-" + str(idx+1) + ".ipynb"
            notebook_path_dst = os.path.join(
                git_project_path, notebook_dst_name)
            
            ## save python script
            script_name = os.path.splitext(os.path.basename(notebook_path_src))[0] + ".py"
            script_path = os.path.join(exec_script_dir, script_name)
            convertNotebook(notebook_path_src, script_path)
            print(f"- successfully converted notebook {idx+1}")

            ## copy over notebooks to git dir
            if args.find_notebooks:
                shutil.copyfile(notebook_path_src, notebook_path_dst)
                print(f"- successfully copied notebook {idx+1}")
                
            ## populate zip
            if args.compile_zips:
                
                ## notebook
                archive.write(notebook_path_src, 
                              arcname=os.path.basename(notebook_path_src))    
                
                ## script
                archive.write(script_path, 
                              arcname=os.path.basename(script_path))    
                
                print(f"- successfully zipped notebook + script {idx+1}")

                
        ## close zip
        if args.compile_zips:
            archive.close()
        
        ## next
        print("\n")
   
#%% copy asset folder

print("copying assets folder")
shutil.copytree(exec_asset_dir, git_asset_dir, dirs_exist_ok = True)

         
#%% upload to gdrive
if args.upload_gdrive:
    for zip_file in os.listdir(exec_zip_dir):
        zip_file_ID = find_gdrive_file_ID(drive, '1Q9yXe1zeYRs4f_PO6LT6loWhhuSftoVy', zip_file)
        zip_file_path = os.path.join(exec_zip_dir, zip_file)
        if zip_file_ID.__class__.__name__ == "NoneType":
            print(f"\nuploading {zip_file} to gdrive...")
            gdrive_file = drive.CreateFile({'parents' : [{'id' : '1Q9yXe1zeYRs4f_PO6LT6loWhhuSftoVy'}], 'title' : zip_file})
            gdrive_file.SetContentFile(zip_file_path)
            gdrive_file.Upload()   
        elif zip_file_ID.__class__.__name__ == "str" and args.upload_gdrive_ow:
            gdrive_file = drive.CreateFile({'id': zip_file_ID})
            gdrive_file.SetContentFile(zip_file_path)
            gdrive_file.Upload()
            print(f"\nupdating {zip_file} on gdrive...")
        elif zip_file_ID.__class__.__name__ == "str":
            print(f"\n{zip_file} exists - skipping ")

            
        
        

    
