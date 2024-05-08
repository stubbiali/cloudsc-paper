[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains the data and scripts to produce the figures contained in the manuscript ``Exploring a high-level programming model for the NWP domain using ECMWF microphysics schemes'' by S. Ubbiali, C. Kühnlein, C. Schär, L. Schlemmer, T. C. Schulthess, M. Staneker, and H. Wernli, to be submitted for peer-review to Geoscientific Model Development (GMD). The article presents the Python rewrites using GT4Py of two IFS microphysics schemes from ECMWF: CLOUDSC and CLOUDSC2. For the latter, the corresponding tangent-linear and adjoint formulations are considered too.

All figures can be generated in PDF format either by exporting diagrams from `src/img/cloudsc_paper.drawio`, or using the Python scripts available in `src/img/`. The Python scripts can be run as follows:

```bash
$ pushd src/img

# create a virtual environment
$ python -m venv venv

# activate the virtual environment
$ source venv/bin/activate

# upgrade basic packages
(venv) $ pip install --upgrade pip setuptools wheel

# install requirements
(venv) $ pip install -r requirements.txt

# run any script; the option --save will save the image as PDF under out/img
(venv) $ python plot_<something>.py [--show/--no-show] [--save]

# deactivate the virtual environment
(venv) $ deactivate
```

The performance numbers shown in the figures are retrieved from `data/`.
