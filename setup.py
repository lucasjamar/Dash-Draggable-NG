import json
from pathlib import Path

from setuptools import setup

HERE = Path(__file__).parent

with open(HERE / "package.json") as f:
    package = json.load(f)

# The import/namespace package name (what users `import`) stays the same so
# this remains a drop-in replacement. The PyPI *distribution* name differs
# because `dash-draggable` is already taken on PyPI by the original project.
import_name = package["name"].replace(" ", "_").replace("-", "_")  # dash_draggable
distribution_name = "dash-draggable-ng"

long_description = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name=distribution_name,
    version=package["version"],
    author=package["author"],
    maintainer="dash-draggable-ng contributors",
    packages=[import_name],
    include_package_data=True,
    package_data={import_name: ["*.js", "*.js.map", "*.json"]},
    license=package["license"],
    description=package.get("description", import_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasjamar/Dash-Draggable-NG",
    project_urls={
        "Source": "https://github.com/lucasjamar/Dash-Draggable-NG",
        "Original project": "https://github.com/MehdiChelh/dash-draggable",
    },
    python_requires=">=3.9",
    install_requires=["dash>=2.0"],
    classifiers=[
        "Framework :: Dash",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
