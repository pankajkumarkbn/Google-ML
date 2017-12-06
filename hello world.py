from sklearn import tree
features = [[[140,1], [130,1], [150,0], [170,0]]
#below the first value denotes the weight of the fruit and second value denotes the texture i.e bumpy=0 or smooth=1.
labels = [0, 0, 1, 1]
#Here label values denotes the type of fruit i.e 0=apple and 1=orange.clf = tree.DecisionTreeClassifier()
clf = tree.DEcisionTreeClassifier()
#clf is a classifier which is a decision tree.
clf = clf.fit(features,labels)
#here the fit method is finding the patters in the data(i.e between features and labels).
print clf.predict([[150,0]])
#finnaly prediciting the label using the weight 150 and texture bumpy i.e 0
#the predicted value comes to be 1 i.e orange
