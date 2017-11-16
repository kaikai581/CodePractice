#!/usr/bin/env python

import h5py

# Open an existing file using default properties.
inf = h5py.File('h5tutr_dset.h5', 'r')

dataset = inf['/dset']

print('Reading data...')
data_read = dataset[...]
print('Printing data...')
print(data_read)

inf.close()
