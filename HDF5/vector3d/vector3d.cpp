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

int main(int argc, char* argv[])
{
  // Data initialization.
  vector<vector<vector<unsigned char*> > > data(2, vector<vector<unsigned char*> >(3, vector<unsigned char*>(4, NULL)));
  // Assign the memory address
  unsigned char* ctr = new unsigned char();
  for(int i = 0; i < 2; i++)
  {
    for(int j = 0; j < 3; j++)
    {
      for(int k = 0; k < 4; k++)
      {
        data[i][j][k] = ctr++;
        *data[i][j][k] = i + j + k;
        cout << (int)*data[i][j][k] << " ";
      }
      cout << endl;
    }
    cout << endl;
  }
  
  /// Code for simple array.
  //~ unsigned char data[2][3][4];
  //~ cout << endl << "data:" << endl << endl;
  //~ for(int i = 0; i < 2; i++)
  //~ {
    //~ for(int j = 0; j < 3; j++)
    //~ {
      //~ for(int k = 0; k < 4; k++)
      //~ {
        //~ data[i][j][k] = i + j + k;
        //~ cout << (int)data[i][j][k] << " ";
      //~ }
      //~ cout << endl;
    //~ }
    //~ cout << endl;
  //~ }
  
  try
  {
    // Turn off the auto-printing when failure occurs so that we can
    // handle the errors appropriately
    Exception::dontPrint();
    
    // Create a new file using the default property lists.
    H5File file(FILE_NAME, H5F_ACC_TRUNC);
    
    // Create the data space for the dataset.
    hsize_t dims[3];               // dataset dimensions
    dims[0] = 2;
    dims[1] = 3;
    dims[2] = 4;
    DataSpace dataspace(3, dims);
    
    // Create the dataset.
    DataSet dataset = file.createDataSet(DATASET_NAME, PredType::STD_U8LE, dataspace);
    
    // Write the data to the dataset using default memory space, file
    // space, and transfer properties.
    //~ dataset.write(data, PredType::STD_U8LE); // Code for simple array.
    dataset.write(data[0][0][0], PredType::STD_U8LE);
  }
  // catch failure caused by the H5File operations
  catch(FileIException error)
  {
    error.printError();
    return -1;
  }
  
  return 0;
}
