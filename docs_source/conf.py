# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'phenopype-gallery'
copyright = 'Moritz Lürig'
author = 'Moritz Lürig'


# -- General configuration ---------------------------------------------------

extensions = [
    # 'myst_parser',
    # 'nbsphinx',
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxemoji.sphinxemoji",
    "sphinxcontrib.youtube"

]

suppress_warnings = ["mystnb.nbcell", "myst.header", "myst.strikethrough"]
myst_enable_extensions = [
    "colon_fence",
    "strikethrough",
]

sphinxemoji_style = 'twemoji'
sphinxemoji_source = 'https://unpkg.com/twemoji@latest/dist/twemoji.min.js'

myst_heading_anchors = 3
nb_execution_mode = "off"
nb_remove_code_outputs = True

master_doc = 'index'

# language = "english"

exclude_patterns = [
    "source/projects/_assets/md*" # include not working yet by jupyterlab_myst
    ".ipynb_checkpoints", 
    "README.md", 
    "conf.py", 
    ".git", 
    "docs",
]

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# html_baseurl = 'https://www.phenopype.org/gallery/'
html_logo = "../../phenopype/assets/phenopype_logo.png"
html_theme = "furo"
html_show_sourcelink = True
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"
html_title = "phenopype gallery"
html_static_path = ["_assets"]
html_css_files = ['css/custom.css']
html_js_files = ["https://cdn.jsdelivr.net/gh/phenopype/phenopype-gallery/docs_source/_assets/js/custom.js"]
templates_path = ["_templates"]
html_theme_options = {
    "source_repository": "https://github.com/phenopype/phenopype-gallery",
    "source_branch": "main",
    "source_directory": "docs_source",
}

