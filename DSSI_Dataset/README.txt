

This folder is meant to house the datasets to answer the two following questions: 

1. Are there identifiable trends between molecules and the beta packing motif for polycyclic aromatic hydrocarbons? Subject matter experts believe there are trends but only examined a dataset of roughly 40 molecules. 

2. Are there identifiable trends between molecules and the adopted packing motif for our dataset of small nitro-group molecules? This relationship has not been studied for this subset of molecules. Likewise, the molecules are much more exotic. 

The datasets:

        The datasets you will work with are in the form of cif and mol files, with labels for the packing motifs in csv. Cif files define the entire
        unit cell packing, which will generally have more than one individual molecule in it. Mol files define just a single base molecule, but also 
        provide the coordinates of the unit cell. Generally speaking, we want to try to finding relationships between the information in the Mol file,
        as this is the base unit, and information in the cif file/provided labels. 

        The associated label files for each problem is set up as follows:
        Unique index, Identifier of molecule, SMILE string (text encoding of molecule), space group header, actual space group value, inversion sym 
        header, binary value where 0 is no inversion symmetry and 1 is inversion symmetry, beta packing motif header, binary value where 0 is a non-beta
        packing and 1 is a beta packing, density header, density value, packing coefficient header, packing coefficient value. 

	Problem 1: We have a set of roughly 1200 mol and cif files for all polycyclic aromatic hydrocarbons in the CCSD. These are further cleaned 
        by removing any molecule files that contain errors. Likewise, we restrict our set to relatively planar molecules to align with the studies 
        people have done on the molecule type. The final dataset is roughly 700 labeled molecules with a 'b' indicating a beta packing motif and an 
        'n' for a non-beta packing motif. 

        	Files:
                  - 1k_Aromatic_hydrocarbons_cif : This holds the cif files for the various molecules
                  - 1k_Aromatic_hydrocarbons_mol : This holds the mol file for the various molecules 
                  - 1k_Aromatic_hydrocarbons_labels.txt: This holds possible labels to use for either classification or regression. For the particular 
                                                         question of interest we would focus on the packing motif. Some files will exist in the original 
                                                         directory that are not referenced in the label file due to the cleaning explained above.  

	Problem 2: We have a set of roughly 16000 mol and cif files of various nitro-group molecules in the CCSD. These are cleaned by removing files
        with errors. What is left is a set of roughly 13000 molecules with a 'b' indicating a beta packing motif and an 'n' for a non-beta packing motif. 
 
                Files:
                  - 16k_HE_materials_cif : This holds the cif files for the various molecules
                  - 16k_HE_materials_mol : This holds the mol files for the various molecules
                  - 16k_HE_materials_labels.txt: This holds possible labels to use for either classification or regression. As above, some molecules 
                                                 might exist in the original files that do not have labels. 

The motivations behind these two questions come from scientific experimentation and necessary use. The polycyclic aromatic hydrocarbons are a small subset of molecules that have been explored by chemists which known correlations between performance and chemical structure. This is a good place to start to see if we can find trends in the full set of polycyclic aromatic hydrocarbons rather than just the 40 the scientists explored. The second question takes this a step further, and looks at a more difficult but highly valuable dataset. Finding correlations between the molecular structure and the performances helps solve many unanswered problems. 

It is also important to mention that the motif labels do not need to be the only outputs to explore. The cif files and label files have many different values and classes that are essential to various fields. The goal should be to focus on a strong featurization technique for the molecular structure and from there explore the performance on different output types. 
