from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

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



MLPClassifier = MLPClassifier(solver = "adam",
                            activation = "relu",
                            hidden_layer_sizes=(100, 3), 
                            alpha=0.0001, 
                            learning_rate_init = 0.0001, 
                            max_iter=200)
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

MLPClassifier.fit(train_features, train_labels)

validation_predicted = MLPClassifier.predict(val_features)

MLPScore = accuracy_score(val_labels,validation_predicted)
print(MLPScore)

joblib.dump(MLPClassifier, 'DS1Val_mlp.joblib')

#load saved model:
#clf = joblib.load('DTModel.joblib')
