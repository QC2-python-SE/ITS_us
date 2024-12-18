# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ITS_us'
copyright = '2024, Sara Cender, Theo Iosif, Ivan Shalashilin'
author = 'Sara Cender, Theo Iosif, Ivan Shalashilin'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../../its_us'))
html_theme = 'sphinx_rtd_theme'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'nbsphinx', 'sphinx.ext.mathjax']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
