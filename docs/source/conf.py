"""Sphinx configuration for banknote_utils documentation."""

import os
import sys
import banknote_utils

# Add the project root directory to the path
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'banknote_utils'
copyright = '2025, DSCI-310'
author = 'Danny Pirouz, William Ho, Sayana Imash, Arad Sabet'
version = banknote_utils.__version__
release = banknote_utils.__version__

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Inter-sphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
}

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True