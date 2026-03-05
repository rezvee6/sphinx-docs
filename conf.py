import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))

project = "Sample Sphinx + PlantUML Docs"
author = "Your Name"
year = datetime.now().year
copyright = f"{year}, {author}"

extensions = [
    "sphinxcontrib.plantuml",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_css_files = [
    "plantuml_panzoom.css",
]

html_js_files = [
    "plantuml_panzoom.js",
]

# --- PlantUML configuration -------------------------------------------------

# Prefer SVG output so pan/zoom works cleanly
plantuml_output_format = "svg"

# Use the PlantUML jar located in the local ./bin folder
plantuml = "java -jar " + os.path.abspath(os.path.join(os.path.dirname(__file__), "bin", "plantuml.jar"))

