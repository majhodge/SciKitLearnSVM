import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

prob_y = []
prob_x = []
datafeatures = []

f = open('usps', 'r')
for line in f:
	line = line.split(None, 1)
	# In case an instance with all zero features
	if len(line) == 1: line += ['']
	label, features = line
	xi = {}
	for e in features.split():
		ind, val = e.split(":")
		xi[int(ind)] = float(val)
	prob_y += [float(label)]
	prob_x += [xi]
f.close()

for x in prob_x:
	new_array = []
	for y in range(1,257):
		if y not in x.keys():
			new_array.append(0)
		else:
			new_array.append(x.get(y))
	datafeatures.append(new_array)
#print(prob_y)

test_x = []
test_y = []
datafeaturesTest = []

f = open('usps.t', 'r')
for line in f:
	line = line.split(None, 1)
	# In case an instance with all zero features
	if len(line) == 1: line += ['']
	label, features = line
	xi = {}
	for e in features.split():
		ind, val = e.split(":")
		xi[int(ind)] = float(val)
	test_y += [float(label)]
	test_x += [xi]
f.close()

for x in test_x:
	new_array = []
	for y in range(1,257):
		if y not in x.keys():
			new_array.append(0)
		else:
			new_array.append(x.get(y))
	datafeaturesTest.append(new_array)
# print(test_y)


train_x,train_y = datafeatures, prob_y

print 'trainX: ', train_x
print 'testX: ', test_x
print 'trainY: ', train_y
print 'testX: ', test_y


#print("One vs Rest: ", OneVsRestClassifier(LinearSVC(random_state=0)).fit(train_x, train_y).score(datafeaturesTest, test_y))
#print("Multiclass: ", LinearSVC(multi_class='crammer_singer', random_state=0).fit(train_x, train_y).score(datafeaturesTest, test_y))




