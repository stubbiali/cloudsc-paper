all: final v0 v1 v1_review v1_diff clean_main

.PHONY: final v0 v1 v1_review v1_diff clean clean_main distclean img

final:
	cd final && $(MAKE)

v0:
	cd v0 && $(MAKE)

v1:
	cd v1 && $(MAKE)

v1_review:
	cd v1-review && $(MAKE)

v1_diff:
	cd v1-diff && $(MAKE)

clean:
	cd final && $(MAKE) clean
	cd v0 && $(MAKE) clean
	cd v1 && $(MAKE) clean
	cd v1-review && $(MAKE) clean
	cd v1-diff && $(MAKE) clean

clean_main:
	cd final && $(MAKE) clean_main
	cd v0 && $(MAKE) clean_main
	cd v1 && $(MAKE) clean_main
	cd v1-review && $(MAKE) clean_main
	cd v1-diff && $(MAKE) clean_main

distclean:
	cd final && $(MAKE) distclean
	cd v0 && $(MAKE) distclean
	cd v1 && $(MAKE) distclean
	cd v1-review && $(MAKE) distclean
	cd v1-diff && $(MAKE) distclean
