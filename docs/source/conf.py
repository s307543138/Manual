# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RinasWeld Offline Manual Test'
copyright = '2025, KPS'
author = 'KPS'

release = '1.0'
version = '1.0.0'

html_title = "RinasWeld Offline Manual"
html_short_title = "RinasWeld Manual"

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    # 新增： Sphinx 支持 Markdown（myst）
    'myst_parser',
]

# Sphinx：.rst 和 .md 都是文档源文件
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
