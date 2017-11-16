UNAME := $(shell uname)

BIN_DIR = bin

ifeq ($(UNAME), Linux)
all: directories
	g++ -std=c++11 -Wall -o $(BIN_DIR)/vector3d vector3d.cpp -I/usr/include/hdf5/serial -L/usr/lib/x86_64-linux-gnu/hdf5/serial -lhdf5_cpp -lhdf5
endif

ifeq ($(UNAME), Darwin)
all: directories
	g++ -std=c++11 -Wall -o $(BIN_DIR)/vector3d vector3d.cpp -I/usr/local/Cellar/hdf5/1.10.1_2/include -L/usr/local/Cellar/hdf5/1.10.1_2/lib -lhdf5_cpp -lhdf5
endif

directories: $(BIN_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)
