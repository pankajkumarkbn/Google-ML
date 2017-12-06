#This is the task given in the hello world of Google's Machine Learning Tutorial
from sklearn import tree
features = [[300,2], [450,2], [200,8], [150,9]]
#here the this array first value denotes the Horse power and the second value denotes the number of seats
labels = [0, 0, 1, 1]
#here in this array 0 denotes sports car and 1 denotes minivan
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[850,4]])
