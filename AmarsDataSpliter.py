# --- Imports ---
import pickle
import os
import numpy as np
from shutil import copy
from pathlib import Path

pkl_file16k = open('smiles_IDtoSplit.pkl', 'rb')

data16k = pickle.load(pkl_file16k)

pkl_file16k.close()

print(data16k)

pkl_file1k = open('1k_test_train_split.pkl', 'rb')

data1k = pickle.load(pkl_file1k)

pkl_file1k.close()

print(data1k)



# --- Check pickle load + make directories ---
if (len(data16k['ID']) == len(data16k['split'])):
    print("---Just making sure the number of id's matches the total number of splitted 16k examples ({0})---".format(len(data16k['ID'])))

if (len(data1k['ID']) == len(data1k['split'])):
    print("---Just making sure the number of id's matches the total number of splitted 16k examples ({0})---".format(len(data1k['ID'])))
    
    
try:
    os.mkdir('New_DSSI_Dataset/')
    os.mkdir('New_DSSI_Dataset/16k_cif')
    os.mkdir('New_DSSI_Dataset/16k_mol')
    os.mkdir('New_DSSI_Dataset/16k_cif/train')
    os.mkdir('New_DSSI_Dataset/16k_cif/test')
    os.mkdir('New_DSSI_Dataset/16k_mol/train')
    os.mkdir('New_DSSI_Dataset/16k_mol/test')
    os.mkdir('New_DSSI_Dataset/1k_cif')
    os.mkdir('New_DSSI_Dataset/1k_mol')
    os.mkdir('New_DSSI_Dataset/1k_cif/train')
    os.mkdir('New_DSSI_Dataset/1k_cif/test')
    os.mkdir('New_DSSI_Dataset/1k_mol/train')
    os.mkdir('New_DSSI_Dataset/1k_mol/test')
except:
    print("New_DSSI_Dataset folder made already, delete it to recreate it...")
    
    
    
    
# --- Search Function ---
def findSplitByID(ID, data16or1k):
    result = np.where(data16or1k['ID'] == ID)
    if (len(result[0]) == 0):
        return -1
    else:
        return result[0][0]
    
# --- Splitter Function ---
def splitter(folderPath, trainSplitPath, testSplitPath, data16or1k):
    allFilePaths = list(folderPath.iterdir())

    for file in allFilePaths:
        fileName = file.name
        ID = fileName.split('.')[0]
        index = findSplitByID(ID, data16or1k)
        if (index != -1):
            splitVal = data16or1k['split'][index]
            if (splitVal == '0'):
                copy(file, trainSplitPath)
            elif (splitVal == '2'):
                copy(file, testSplitPath)
                
                
                
                
# --- 16k cif's into split folders ---
print("--- Splitting 16k cifs... ---")
splitter(Path('DSSI_Dataset/16k_HE_materials_cif'),
        Path('New_DSSI_Dataset/16k_cif/train'),
        Path('New_DSSI_Dataset/16k_cif/test'),
        data16k
        )

# --- 16k mol's into split folders ---
print("--- Splitting 16k mols... ---")
splitter(Path('DSSI_Dataset/16k_HE_materials_mol'),
        Path('New_DSSI_Dataset/16k_mol/train'),
        Path('New_DSSI_Dataset/16k_mol/test'),
        data16k
        )

# --- 1k cif's into split folders ---
print("--- Splitting 1k cifs... ---")
splitter(Path('DSSI_Dataset/1k_Aromatic_hydrocarbons_cif'),
        Path('New_DSSI_Dataset/1k_cif/train'),
        Path('New_DSSI_Dataset/1k_cif/test'),
        data1k
        )

# --- 1k mol's into split folders ---
print("--- Splitting 1k mols... ---")
splitter(Path('DSSI_Dataset/1k_Aromatic_hydrocarbons_mol'),
        Path('New_DSSI_Dataset/1k_mol/train'),
        Path('New_DSSI_Dataset/1k_mol/test'),
        data1k
        )

print("Done!")