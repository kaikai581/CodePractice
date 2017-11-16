UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
all:
	g++ -Wall vector3d.cpp -I/usr/include/hdf5/serial -o vector3d
endif

ifeq ($(UNAME), Darwin)
all:
	g++ -Wall vector3d.cpp -I/usr/local/Cellar/hdf5/1.10.1_2/include -o vector3d
endif
