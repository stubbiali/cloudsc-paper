This repository contains the source code for the manuscript ``Exploring a high-level programming model for the NWP domain using the IFS microphysics schemes'' by S. Ubbiali, C. Kühnlein, C. Schär, L. Schlemmer, T. C. Schulthess, M. Staneker, and H. Wernli, to be submitted to Geoscientific Model Development (GMD). The article presents the Python rewrites using GT4Py of two IFS microphysics schemes from ECMWF: CLOUDSC and CLOUDSC2. For the latter, the corresponding tangent-linear and adjoint formulations are considered too.

The LaTeX source files for the manuscript are stored under `src/latex/` and can be compiled to generate the latest version of the article in PDF format using the Makefile contained in that folder:

```bash
$ pushd src/latex
$ make  # the generated PDF is called main.pdf
```

The images included in the paper can be found in `img/`. All figures are in PDF format, and are either diagrams exported from `img/cloudsc_paper.drawio`, or can be produced using the Python scripts available in `src/python/`. The Python scripts can be run as follows:

```bash
$ pushd src/python

# create a virtual environment
$ python -m venv venv

# activate the virtual environment
$ source venv/bin/activate

# upgrade basic packages
(venv) $ pip install --upgrade pip setuptools wheel

# install requirements
(venv) $ pip install -r requirements.txt

# run any script
(venv) $ python plot_<something>.py [--show/--no-show] [--save]

# deactivate the virtual environment
(venv) $ deactivate
```

The performance numbers shown in the figures are retrieved from `data/`.

Older versions of the article can be found in `pdf/`.