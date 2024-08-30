import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

#In this case, we will be using a diabetes dataset provided by the Scikit-Learn library.
diabetes = datasets.load_diabetes()

#We use the Body Mass Index column against the target, a quantitative measure of disease progression one year after baseline.
x = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

#We create a scatter plot with Matplotlib to observe the correlation between BMI and the target.
plt.scatter(x,y)
plt.show()

from sklearn.model_selection import train_test_split

#Now we need to split the dataset into training and test data. In this case, we take 20% of the data without specifying which ones.
#This will yield slightly different results each time the script is run, as the model is trained with different data each time.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#The other option is the one commented out below. The same data is always used, so the results do not vary.
#x_train = x[:-20]
#x_test = x[-20:]
#y_train = y[:-20]
#y_test = y[-20:]

#Creation of a linear regression algorithm
algoritmo = linear_model.LinearRegression()

#Training the algorithm
algoritmo.fit(x_train, y_train)

#Based on the test set of BMI predictors, the target is predicted by assigning it to the variable `y_predic`.
y_predic = algoritmo.predict(x_test)


#Here, a scatter plot is created with the pair of real values (x_test and y_test) and a linear regression with the pair of predicted values (x_test and y_predic). 
#It can be observed that the linear regression model is not the best option for this dataset.
plt.scatter(x_test, y_test)
plt.plot(x_test, y_predic, color="green")
plt.grid()
plt.show()

#The equation of the model is detailed as follows: y = a + bx.
print(f"La ecuación es y = {algoritmo.intercept_} + {algoritmo.coef_} x")

#Model accuracy is around 0.35. It is measured from 0 to 1, where values close to 1 indicate a precise model and values close to 0 indicate a less precise model. 
#In this case, the model's predictions are not very accurate.
print(algoritmo.score(x_train, y_train))


#Let's make our own prediction! The user inputs a body mass index, and the model will predict disease progression.
my_array = []
my_array.append(float(input("Please enter the body mass index: ")))
my_array = np.array(my_array)
#We need to input the user's data into a NumPy array and then convert it to a 2D array.
nuevo_array = my_array.reshape(-1, 1)
resultado = algoritmo.predict(nuevo_array)
print("The disease progression is:" , resultado)

#Finally, we can make the prediction manually using the equation to verify that it matches.
x_user = float(input("Please enter the same body mass index: "))
y_user = algoritmo.intercept_ + algoritmo.coef_ * x_user
print("The disease progression is:" , y_user)
