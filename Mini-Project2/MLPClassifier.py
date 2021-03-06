from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

######################################### Dataset 1 #########################################

### Extracting data from the training file ###
with open("DataSet-Release 2/ds1/ds1Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

# Extracting the training labels
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
MLPClassifier_ds1 = MLPClassifier(hidden_layer_sizes=(100, 100),
                            max_iter=100,
                            solver = "adam",
                            activation = "tanh", 
                            alpha=0.001, 
                            learning_rate_init = 0.001)
# (hidden_layer_sizes=(100, 3),
#  activation=’relu’,
#  solver=’adam’,
#  alpha=0.0001,
#  batch_size=’auto’,
#  learning_rate=’constant’,
#  learning_rate_init=0.001,
#  power_t=0.5,
#  max_iter=200,
#  shuffle=True,
#  random_state=None,
#  tol=0.0001,
#  verbose=False,
#  warm_start=False,
#  momentum=0.9,
#  nesterovs_momentum=True,
#  early_stopping=False,
#  validation_fraction=0.1,
#  beta_1=0.9,
#  beta_2=0.999,
#  epsilon=1e-08,
#  n_iter_no_change=10)

# fitting the model
MLPClassifier_ds1.fit(train_features, train_labels)

# Predicting the validation set
validation_predicted = MLPClassifier_ds1.predict(val_features)

# Getting the accuracy score
MLPScore = accuracy_score(val_labels,validation_predicted)
print("accuracy score of the MLP model for DS1:", MLPScore)

# Saving validation predictions 
with open('Results/Validation/ds1Val-mlp.csv', 'w') as file:
    for i in range(len(validation_predicted)):
        file.write('%d,%d\n' % (i + 1, validation_predicted[i]))

# Saving the Model
joblib.dump(MLPClassifier_ds1, 'Models/MLPModelDs1.joblib')

######################################### Dataset 2 #########################################

### Extracting data from the training file ###
with open("DataSet-Release 2/ds2/ds2Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

# Extracting the training labels
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
MLPClassifier_ds2 = MLPClassifier(hidden_layer_sizes=(100, 100),
                            max_iter=100,
                            solver = "adam",
                            activation = "tanh", 
                            alpha=0.001, 
                            learning_rate_init = 0.001)
# (hidden_layer_sizes=(100, 3),
#  activation=’relu’,
#  solver=’adam’,
#  alpha=0.0001,
#  batch_size=’auto’,
#  learning_rate=’constant’,
#  learning_rate_init=0.001,
#  power_t=0.5,
#  max_iter=200,
#  shuffle=True,
#  random_state=None,
#  tol=0.0001,
#  verbose=False,
#  warm_start=False,
#  momentum=0.9,
#  nesterovs_momentum=True,
#  early_stopping=False,
#  validation_fraction=0.1,
#  beta_1=0.9,
#  beta_2=0.999,
#  epsilon=1e-08,
#  n_iter_no_change=10)

# fitting the model
MLPClassifier_ds2.fit(train_features, train_labels)

# Predicting the validation set
validation_predicted = MLPClassifier_ds2.predict(val_features)

# Getting the accuracy score
MLPScore = accuracy_score(val_labels,validation_predicted)
print("accuracy score of the MLP model for DS2:", MLPScore)

# Saving validation predictions 
with open('Results/Validation/ds2Val-mlp.csv', 'w') as file:
    for i in range(len(validation_predicted)):
        file.write('%d,%d\n' % (i + 1, validation_predicted[i]))

# Saving the Model
joblib.dump(MLPClassifier_ds2, 'Models/MLPModelDs2.joblib')
