MEDIA_ROOT = ../img
PYTHON_SRC_DIR = $(MEDIA_ROOT)/src
PYTHON_SCRIPTS = \
	$(PYTHON_SRC_DIR)/plot_runtime_daint.py \
	$(PYTHON_SRC_DIR)/plot_runtime_fraction_composite.py \
	$(PYTHON_SRC_DIR)/plot_runtime_lumi.py \
	$(PYTHON_SRC_DIR)/plot_runtime_mlux.py

all: v0 v1 v1_review v1_diff clean_main

.PHONY: v0 v1 v1_review v1_diff clean clean_main distclean img

v0:
	cd v0 && $(MAKE)

v1:
	cd v1 && $(MAKE)

v1_review:
	cd v1-review && $(MAKE)

v1_diff:
	cd v1-diff && $(MAKE)

clean:
	cd v0 && $(MAKE) clean
	cd v1 && $(MAKE) clean
	cd v1-review && $(MAKE) clean
	cd v1-diff && $(MAKE) clean

clean_main:
	cd v0 && $(MAKE) clean_main
	cd v1 && $(MAKE) clean_main
	cd v1-review && $(MAKE) clean_main
	cd v1-diff && $(MAKE) clean_main

distclean:
	cd v0 && $(MAKE) distclean
	cd v1 && $(MAKE) distclean
	cd v1-review && $(MAKE) distclean
	cd v1-diff && $(MAKE) distclean

img:
	for script in $(PYTHON_SCRIPTS) ; do \
        python $$script --no-show --save ; \
    done
