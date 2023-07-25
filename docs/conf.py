# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# All the existing imports here
import subprocess
import packaging.version
from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink
from sphinx.ext.autodoc import ClassDocumenter
from sphinx.application import Sphinx
from sphinx.util.docstrings import prepare_docstring

# Project --------------------------------------------------------------

project = "konanai"
copyright = "2023 KonanAI LLC"
author = "Joseph Konan"

release = '0.1'
version = '0.1.0'

# release, version = get_version("konanai")

# General --------------------------------------------------------------

master_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
    "sphinx_issues",
    "sphinx_tabs.tabs",
]
autodoc_typehints = "description"
autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
}
add_module_names = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
issues_github_path = "KonanAI-LLC/konanai"

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("PyPI Releases", "https://pypi.org/project/konanai/"),
        ProjectLink("Source Code", "https://github.com/KonanAI-LLC/konanai"),
        ProjectLink("Issue Tracker", "https://github.com/KonanAI-LLC/konanai/issues/"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}
html_static_path = ["_static"]
html_favicon = "_static/shortcut-icon.png"
html_logo = "_static/konanai-logo.png"
html_title = f"konanai Documentation ({version})"
html_show_sourcelink = False

exclude_patterns = ['**/konanai/src/konanai/externals/lib']

# LaTeX ----------------------------------------------------------------

latex_documents = [(master_doc, f"konanai-{version}.tex", html_title, author, "manual")]

# Local Extensions -----------------------------------------------------

def github_link(name, rawtext, text, lineno, inliner, options=None, content=None):
    app = inliner.document.settings.env.app
    release = app.config.release
    base_url = "https://github.com/KonanAI-LLC/konanai/tree/"

    if text.endswith(">"):
        words, text = text[:-1].rsplit("<", 1)
        words = words.strip()
    else:
        words = None

    if packaging.version.parse(release).is_devrelease:
        url = f"{base_url}main/{text}"
    else:
        url = f"{base_url}{release}/{text}"

    if words is None:
        words = url

    from docutils.nodes import reference
    from docutils.parsers.rst.roles import set_classes

    options = options or {}
    set_classes(options)
    node = reference(rawtext, words, refuri=url, **options)
    return [node], []

def setup(app: Sphinx):
    app.add_role("gh", github_link)
    app.connect('build-finished', run_postprocess)

def find_index_html(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'index.html' in files:
            print(os.path.join(root, 'index.html'))

def run_postprocess(app, exception):
    # The script and html directory paths
    script_path = os.path.join(os.path.dirname(__file__), "postprocess.py")
    
    # The path to the 'index.html' file
    html_file_path = os.path.join(app.outdir, "_readthedocs", "html", "index.html")

    find_index_html('.')
    print(f"Running postprocess on: {html_file_path}")  # print statement

    # Call the postprocess script on the 'index.html' file
    subprocess.check_call([sys.executable, script_path, html_file_path])
