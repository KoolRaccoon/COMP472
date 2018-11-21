from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


### Extracting data from the training file ###
with open("DataSet-Release 2/ds1/ds1Train.csv", 'r') as file:
    data_ds1 = [line.split(',') for line in file.read().split('\n')]
train_features_ds1 = [[int(element) for element in row] for row in data_ds1]

# Extracting the training labels
train_labels_ds1 = [row[1024] for row in train_features_ds1]

# train_data = train_features
for row in train_features_ds1:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.


### Extracting Validation data ###
with open("DataSet-Release 2/ds1/ds1Val.csv", 'r') as file:
    data_ds1 = [line.split(',') for line in file.read().split('\n')]
val_features_ds1 = [[int(element) for element in row] for row in data_ds1]

# Extracting the validation labels
val_labels_ds1 = [row[1024] for row in val_features_ds1]

# train_data = train_features_ds1
for row in val_features_ds1:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.

DTclassifier_ds1 = tree.DecisionTreeClassifier(criterion="entropy", max_depth = 40)
# given in slides: criterion = "entropy", max_depth = 10)

# (criterion=’gini’, 
# splitter=’best’, 
# max_depth=None, 
# min_samples_split=2, 
# min_samples_leaf=1, 
# min_weight_fraction_leaf=0.0,
# max_features=None, 
# random_state=None, 
# max_leaf_nodes=None,
# min_impurity_decrease=0.0, 
# min_impurity_split=None, 
# class_weight=None, 
# presort=False)

# fitting the model
DTclassifier_ds1.fit(train_features_ds1, train_labels_ds1)

# Predicting the validation set
validation_predicted_ds1 = DTclassifier_ds1.predict(val_features_ds1)

# Getting the accuracy score
DTScore_ds1 = accuracy_score(val_labels_ds1, validation_predicted_ds1)
print("accuracy score of the DT model for DS1:", DTScore_ds1)

# Saving validation predictions 
with open('Results/Validation/ds1Val-dt.csv', 'w') as file:
	for i in range(len(validation_predicted_ds1)):
		file.write('%d,%d\n' % (i + 1, validation_predicted_ds1[i]))

# Saving the Model
joblib.dump(DTclassifier_ds1, 'Models/DTModelDs1.joblib')

######################################### Dataset 2 #########################################

### Extracting data from the training file ###
with open("DataSet-Release 2/ds2/ds2Train.csv", 'r') as file:
    data_ds2 = [line.split(',') for line in file.read().split('\n')]
train_features_ds2 = [[int(element) for element in row] for row in data_ds2]

# Extracting the training labels
train_labels_ds2 = [row[1024] for row in train_features_ds2]

# train_data = train_features
for row in train_features_ds2:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.


### Extracting Validation data ###
with open("DataSet-Release 2/ds2/ds2Val.csv", 'r') as file:
    data_ds2 = [line.split(',') for line in file.read().split('\n')]
val_features_ds2 = [[int(element) for element in row] for row in data_ds2]

# Extracting the validation labels
val_labels_ds2 = [row[1024] for row in val_features_ds2]

# train_data = train_features_ds1
for row in val_features_ds2:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.

DTclassifier_ds2 = tree.DecisionTreeClassifier(criterion="gini", max_depth = 40)
# given in slides: criterion = "entropy", max_depth = 10)

# (criterion=’gini’, 
# splitter=’best’, 
# max_depth=None, 
# min_samples_split=2, 
# min_samples_leaf=1, 
# min_weight_fraction_leaf=0.0,
# max_features=None, 
# random_state=None, 
# max_leaf_nodes=None,
# min_impurity_decrease=0.0, 
# min_impurity_split=None, 
# class_weight=None, 
# presort=False)

# fitting the model
DTclassifier_ds2.fit(train_features_ds2, train_labels_ds2)

# Predicting the validation set
validation_predicted_ds2 = DTclassifier_ds2.predict(val_features_ds2)

# Getting the accuracy score
DTScore_ds2 = accuracy_score(val_labels_ds2, validation_predicted_ds2)
print("accuracy score of the DT model for DS2:", DTScore_ds2)

# Saving validation predictions 
with open('Results/Validation/ds2Val-dt.csv', 'w') as file:
    for i in range(len(validation_predicted_ds2)):
        file.write('%d,%d\n' % (i + 1, validation_predicted_ds2[i]))

# Saving the Model
joblib.dump(DTclassifier_ds2, 'Models/DTModelDs2.joblib')
