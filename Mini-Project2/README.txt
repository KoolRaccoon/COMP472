This README explains how the program works and should be executed

There are three classifier files: DTClassifier.py, NBClassifier.py and MLPClassifier.py. Each one creates a model for each dataset which gets stored in the the Models folder. Each one must be run individual using the python command, i.e. python DTClassifier.py. The results for the validation will be stored inside Results/Validation

Executing these scripts will also output the accuracy scores obtained for each dataset.

Each model can then be loaded and run on the test sets that are found in the DataSet-Release 2 folder.
To test the test sets run each Model file individually. The files for the models are called DT_Model_Test.py, NB_Model_Test.py and MLP_Model_Test.py. The results computed for the test set will be stored inside Results/Test.
