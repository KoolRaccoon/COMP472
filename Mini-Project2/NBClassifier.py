from sklearn import naive_bayes
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

######################################### Dataset 1 #########################################

### Extracting data from the training file ###
with open("DataSet-Release 2/ds1/ds1Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

#Extracting the training labels
train_labels = [row[1024] for row in train_features]

# train_data = train_features
for row in train_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.



### Extracting Validation data ###
with open("DataSet-Release 2/ds1/ds1Val.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
val_features = [[int(element) for element in row] for row in data]

# Extracting the validation labels
val_labels = [row[1024] for row in val_features]

# train_data = train_features
for row in val_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.

# Creating the classifier 
NBclassifier = naive_bayes.MultinomialNB(alpha=0.1, fit_prior=True, class_prior=None)

# fitting the model
NBclassifier.fit(train_features, train_labels)

# Predicting the validation set
validation_predicted = NBclassifier.predict(val_features)

# Getting the accuracy score
NBScore = accuracy_score(val_labels,validation_predicted)
print("accuracy score of the NB model for DS1:", NBScore)

# Saving validation predictions 
with open('Results/Validation/ds1Val-nb.csv', 'w') as file:
    for i in range(len(validation_predicted)):
        file.write('%d,%d\n' % (i + 1, validation_predicted[i]))

# Saving the Model
joblib.dump(NBclassifier, 'Models/NBModelDs1.joblib')

######################################### Dataset 2 #########################################

### Extracting data from the training file ###
with open("DataSet-Release 2/ds2/ds2Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

#Extracting the training labels
train_labels = [row[1024] for row in train_features]

# train_data = train_features
for row in train_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.

### Extracting Validation data ###
with open("DataSet-Release 2/ds2/ds2Val.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
val_features = [[int(element) for element in row] for row in data]

# Extracting the validation labels
val_labels = [row[1024] for row in val_features]

# train_data = train_features
for row in val_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.

# Creating the classifier 
NBclassifier = naive_bayes.MultinomialNB(alpha=0.1, fit_prior=True, class_prior=None)

# fitting the model
NBclassifier.fit(train_features, train_labels)

# Predicting the validation set
validation_predicted = NBclassifier.predict(val_features)

# Getting the accuracy score
NBScore = accuracy_score(val_labels,validation_predicted)
print("accuracy score of the NB model for DS2:", NBScore)

# Saving validation predictions 
with open('Results/Validation/ds2Val-nb.csv', 'w') as file:
    for i in range(len(validation_predicted)):
        file.write('%d,%d\n' % (i + 1, validation_predicted[i]))

# Saving the Model
joblib.dump(NBclassifier, 'Models/NBModelDs2.joblib')
