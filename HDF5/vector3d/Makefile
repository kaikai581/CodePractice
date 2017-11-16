UNAME := $(shell uname)

BIN_DIR = bin

ifeq ($(UNAME), Linux)
all: directories
	g++ -Wall vector3d.cpp -I/usr/include/hdf5/serial -o $(BIN_DIR)/vector3d
endif

ifeq ($(UNAME), Darwin)
all: directories
	g++ -Wall vector3d.cpp -I/usr/local/Cellar/hdf5/1.10.1_2/include -o $(BIN_DIR)/vector3d
endif

directories: $(BIN_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)
