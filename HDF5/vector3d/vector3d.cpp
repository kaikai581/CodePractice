/*
 * This program tries to write data to an hdf5 file from data in C++ vectors.
 */

#include <iostream>
#include <vector>
#include "H5Cpp.h"

using namespace H5;
using namespace std;

const H5std_string FILE_NAME("h5tutr_dset.h5");
const H5std_string DATASET_NAME("dset");
const int NN = 4000;
const int NC = 4;
const int NH = 100;
const int NW = 100;

int main(int argc, char* argv[])
{
  unsigned char**** A = new unsigned char***[NN];
  unsigned char***  B = new unsigned char**[NN*NC];
  unsigned char**   C = new unsigned char*[NN*NC*NH];
  unsigned char*    D = new unsigned char[NN*NC*NH*NW];
  for(int i = 0; i < NN; i++) {
    for(int j = 0; j < NC; j++) {
      for(int k = 0; k < NH; k++) {
        C[NH*(NC*i+j)+k] = D+(NH*(NC*i+j)+k)*NW;
      }
      B[NC*i+j] = C+NH*(NC*i+j);
    }
    A[i] = B+NC*i;
  }
  for(int i = 0; i < NN; i++) {
    for(int j = 0; j < NC; j++) {
      for(int k = 0; k < NH; k++) {
        for(int l = 0; l < NW; l++) {
          A[i][j][k][l] = i+j+k+l;
          //~ cout << (int)A[i][j][k][l] << " ";
        }
        //~ cout << endl;
      }
      //~ cout << endl;
    }
    //~ cout << endl;
  }
        

  try
  {
    // Turn off the auto-printing when failure occurs so that we can
    // handle the errors appropriately
    Exception::dontPrint();
    
    // Create a new file using the default property lists.
    H5File file(FILE_NAME, H5F_ACC_TRUNC);
    
    // Create the data space for the dataset.
    hsize_t dims[4];               // dataset dimensions
    dims[0] = NN;
    dims[1] = NC;
    dims[2] = NH;
    dims[3] = NW;
    DataSpace dataspace(4, dims);
    
    // Create the dataset.
    DataSet dataset = file.createDataSet(DATASET_NAME, PredType::STD_U8LE, dataspace);
    
    // Write the data to the dataset using default memory space, file
    // space, and transfer properties.
    dataset.write(&A[0][0][0][0], PredType::STD_U8LE);
  }
  // catch failure caused by the H5File operations
  catch(FileIException error)
  {
    error.printError();
    return -1;
  }

  return 0;
}
