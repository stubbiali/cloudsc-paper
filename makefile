all: latex img

.PHONY: latex img

latex:
	cd latex && $(MAKE)

img:
	cd img && $(MAKE)
