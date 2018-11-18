from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

######################## Dataset 1 ########################
### Extracting data from the test file ###
with open("DataSet-Release 2/ds1/ds1Test.csv", 'r') as file:
    data_ds1 = [line.split(',') for line in file.read().split('\n')]
test_features_ds1 = [[int(element) for element in row] for row in data_ds1]

# load saved model
DTClassifier_ds1 = joblib.load('Models/DTModelDs1.joblib')

# Predicting the test set
test_predicted_ds1 = DTClassifier_ds1.predict(test_features_ds1)

# print (test_predicted_ds1)
# Saving test predictions 
with open('Results/Test/ds1Test-dt.csv', 'w') as file:
    for i in range(len(test_predicted_ds1)):
        file.write('%d,%d\n' % (i + 1, test_predicted_ds1[i]))


######################## Dataset 2 ########################
### Extracting data from the test file ###
with open("DataSet-Release 2/ds2/ds2Test.csv", 'r') as file:
    data_ds2 = [line.split(',') for line in file.read().split('\n')]
test_features_ds2 = [[int(element) for element in row] for row in data_ds2]

# load saved model
DTClassifier_ds2 = joblib.load('Models/DTModelDs2.joblib')

# Predicting the test set
test_predicted_ds2 = DTClassifier_ds2.predict(test_features_ds2)

# print (test_predicted_ds1)
# Saving test predictions 
with open('Results/Test/ds2Test-dt.csv', 'w') as file:
    for i in range(len(test_predicted_ds2)):
        file.write('%d,%d\n' % (i + 1, test_predicted_ds2[i]))

