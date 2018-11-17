from sklearn import naive_bayes
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

###Extracting data from the training file###
with open("DataSet-Release 1/ds2/ds2Train.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
train_features = [[int(element) for element in row] for row in data]

#Extracting the training labels
train_labels = [row[1024] for row in train_features]

# train_data = train_features
for row in train_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.



###Extracting Validation data###
with open("DataSet-Release 1/ds2/ds2Val.csv", 'r') as file:
    data = [line.split(',') for line in file.read().split('\n')]
val_features = [[int(element) for element in row] for row in data]

#Extracting the validation labels
val_labels = [row[1024] for row in val_features]

# train_data = train_features
for row in val_features:
    del row[1024]  # 0 for column 1, 1 for column 2, etc.



NBclassifier = naive_bayes.MultinomialNB(alpha=0.1, fit_prior=True, class_prior=None)

NBclassifier.fit(train_features, train_labels)

validation_predicted = NBclassifier.predict(val_features)

NBScore = accuracy_score(val_labels,validation_predicted)
print(NBScore)


joblib.dump(NBclassifier, 'DS1Val_nb.joblib')

#load saved model:
#clf = joblib.load('DTModel.joblib')
