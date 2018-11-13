from sklearn import tree

###Extracting data from the training file###
with open("DataSet-Release 1/ds1/ds1Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

#Extracting the training labels
train_labels = [row[1024] for row in train_features]

# train_data = train_features
for row in train_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.



###Extracting Validation data###
with open("DataSet-Release 1/ds1/ds1Val.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
val_features = [[int(element) for element in row] for row in data]

#Extracting the validation labels
val_labels = [row[1024] for row in val_features]

# train_data = train_features
for row in val_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.



DTclassifier = tree.DecisionTreeClassifier(criterion="entropy", max_depth=40)
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

DTclassifier.fit(train_features, train_labels)

validation_predicted = DTclassifier.predict(val_features)

DTScore = DTclassifier.score(val_features,val_labels)
print(DTScore)