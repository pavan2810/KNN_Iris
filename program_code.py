# import data set
from sklearn.datasets import load_iris
iris=load_iris()
print("Feature Names:", iris.feature_names, "Iris Data:", iris.data,"Target Names:" iris.target_names, "Target:", iris.target)

# splitting data for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(iris.data, iris.target, test_size=.25)

# import model
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(X_train, y_train)



print("predicted data")
print(clf.predict(X_test))

prediction=model.predict(X_test))

print("test data")
print(y_test)

# To identify miss classificatin
diff=prediction-y_test
print("Result is")
print(diff)
print("total no of sample miss clasified=", sum(abs(diff)))
      
