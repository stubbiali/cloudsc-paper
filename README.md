[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/741397037.svg)](https://zenodo.org/doi/10.5281/zenodo.11155353)

This repository contains the source files and data for the manuscript ``Exploring a high-level programming model for the NWP domain using ECMWF microphysics schemes'' by S. Ubbiali, C. Kühnlein, C. Schär, L. Schlemmer, T. C. Schulthess, M. Staneker, and H. Wernli, submitted for peer-review to Geoscientific Model Development (GMD). The article presents the Python rewrites using GT4Py of the IFS microphysics schemes CLOUDSC and CLOUDSC2. For the latter, the corresponding tangent-linear and adjoint formulations are also considered.

The LaTeX source files of the article can be found in `latex/`. The files are arranged into subdirectories, corresponding to different versions of the article:

* `latex/v0/` is the original submission;
* `latex/v1/` is the revised submission;
* `latex/v1-diff/` is the revised submission, with track changes enabled;
* `latex/v1-review/` is the revised submission, with changes to the original submission highlighted.

Makefiles are provided to automate compilation of the LaTeX source files. To generate the PDF of any version, go into the corresponding folder and type `make`. To compile all versions in one shot, type `make` from the `latex/` folder.

**Remark #1**: The makefiles rely on the commands `pdflatex` and, for `latex/v1-diff/` only, `latexdiff`. Either make sure that both commands are in your path, or adapt the makefiles to suit your needs.

**Remark #2**: We make use of some LaTeX packages which may not ship with common LaTeX distributions. If so, please use your preferred LaTeX package manager to install them.

All figures of the manuscript are contained in `img/`, and can be generated in PDF format either by exporting diagrams from `img/src/cloudsc_paper.drawio`, or using the Python scripts available in `img/src/`. The Python scripts can be run as follows:

```bash
# create a virtual environment
$ python -m venv venv

# activate the virtual environment
$ source venv/bin/activate

# upgrade basic packages
(venv) $ pip install --upgrade pip setuptools wheel

# install requirements
(venv) $ pip install -r requirements.txt

# run any script; the option --save will save the image as PDF under img/
(venv) $ python img/src/plot_<something>.py [--show/--no-show] [--save]

# deactivate the virtual environment
(venv) $ deactivate
```

The performance numbers shown in the figures are retrieved from `data/`.
