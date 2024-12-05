PYTHON_SRC_DIR = src
PYTHON_SCRIPTS = \
	$(PYTHON_SRC_DIR)/plot_key_figure.py \
	$(PYTHON_SRC_DIR)/plot_runtime_daint.py \
	$(PYTHON_SRC_DIR)/plot_runtime_fraction.py \
	$(PYTHON_SRC_DIR)/plot_runtime_fraction_fp64.py \
	$(PYTHON_SRC_DIR)/plot_runtime_lumi.py \
	$(PYTHON_SRC_DIR)/plot_runtime_lumi_fp64.py \
	$(PYTHON_SRC_DIR)/plot_runtime_mlux.py

all: img

.PHONY: img

img:
	for script in $(PYTHON_SCRIPTS) ; do \
        python $$script --no-show --save ; \
    done
