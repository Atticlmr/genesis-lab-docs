import os
import sys


YOUR_PACKAGE_NAME = "genesis_lab"  # ←←← 改这里！

# Prefer local source: add monorepo root (two levels up) if it contains your package
_local_repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
if os.path.isdir(os.path.join(_local_repo_root, YOUR_PACKAGE_NAME)):
    sys.path.insert(0, _local_repo_root)

# Dynamically import your package to get __version__
try:
    your_pkg = __import__(YOUR_PACKAGE_NAME)
    __version__ = getattr(your_pkg, "__version__", "0.1.0")
except (ImportError, AttributeError):
    __version__ = "0.1.0"  # fallback version

# -- Project information -----------------------------------------------------

project = "genesis_lab"
copyright = "2025, LI MINGRUI"
author = "LI MINGRUI"
release = __version__
version = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_subfigure",
    "sphinxcontrib.video",
    "sphinx_togglebutton",
    "sphinx_design",
]

# MyST Markdown extensions
myst_enable_extensions = ["colon_fence", "dollarmath", "amsmath"]
myst_heading_anchors = 4

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_logo = "_static/bigger_text.png"
html_favicon = "_static/option2_shadow_1.svg"

# Version switcher — disabled by default (remove if you don't have version_switcher.json)
# json_url = "_static/version_switcher.json"
# version_match = os.environ.get("READTHEDOCS_VERSION") or f"v{__version__}"

html_theme_options = {
    "show_nav_level": 2,
    "use_edit_page_button": True,
    "logo": {
        "image_dark": "_static/bigger_text_white.png",  # optional
    },
    "navbar_center": ["navbar-nav"],  # removed version-switcher to avoid error
    "show_version_warning_banner": False,
    # If you later add version_switcher.json, uncomment the lines below:
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
}


html_context = {
    "display_github": True,
    "github_user": "Atticlmr",      
    "github_repo": "genesis_lab_doc",    
    "github_version": "main",
    "conf_py_path": "/source/",
    "doc_path": "/source",
}

html_css_files = ["css/custom.css"]
html_static_path = ["_static"]

# -- Autodoc settings --------------------------------------------------------
autodoc_typehints = "signature"
autodoc_typehints_description_target = "all"
autodoc_default_flags = ["members", "show-inheritance", "undoc-members"]
autodoc_member_order = "bysource"
autosummary_generate = True