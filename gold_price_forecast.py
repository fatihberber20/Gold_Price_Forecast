import pandas as pd
veriseti=pd.read_csv('gld_price_data.csv')
X=veriseti.iloc[:,2].values
y=veriseti.iloc[:,4].values
X=X.reshape(len(X),1)

#Train-Split 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42)

#Fitting the training set according to linear regression
from sklearn.linear_model import LinearRegression
model_Regresyon=LinearRegression()
model_Regresyon.fit(X_train, y_train)

#Estimation of test set results
y_pred=model_Regresyon.predict(X_test)

#Plotting the training set results
import matplotlib.pyplot as plt
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, model_Regresyon.predict(X_train), color='blue')
plt.title('Gold Prices(Train Data Set)')
plt.xlabel('EUR/USD Price')
plt.ylabel('Gold Price')
plt.show()

#Plotting the test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, model_Regresyon.predict(X_train), color='blue')
plt.title('Gold Prices(Test Data Set)')
plt.xlabel('EUR/USD Price')
plt.ylabel('Gold Price')
plt.show()


#Regression Equation
print("y=%0.2f"%model_Regresyon.coef_+"x%0.2f"%model_Regresyon.intercept_)

#Performance of Test Data Set
from sklearn.metrics import median_absolute_error, r2_score, explained_variance_score, mean_squared_error, mean_absolute_error
print("R^2: ", r2_score(y_test, y_pred))
print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", mean_squared_error(y_test, y_pred))
print("MedAE: ", median_absolute_error(y_test, y_pred))
print("EVS: ", explained_variance_score(y_test, y_pred))