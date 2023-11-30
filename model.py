# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# import pandas as pd

# # laoding my datasets
# data = pd.read_csv("data/dataset.csv")

# features = ['Symptom_1','Symptom_2','Symptom_3','Symptom_4','Symptom_5','Symptom_6','Symptom_7','Symptom_8','Symptom_9','Symptom_10','Symptom_11','Symptom_12','Symptom_13','Symptom_14','Symptom_15','Symptom_16','Symptom_17']
# target = 'Disease'
# X = pd.get_dummies(data[features], columns=features)
# y = data[target]

# # spliting datasets to train and train
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # loading models
# # linear_model = LinearRegression()
# # linear_model.fit(X_train, y_train)
# # linear_score = linear_model.score(X_test, y_test)

# # print("linear regression R^2: ", linear_score)

# logistic_model = LogisticRegression()
# logistic_model.fit(X_train, y_train)
# accuracy = logistic_model.score(X_test, y_test)

# print("Accuracy of Logistic Regression:", accuracy)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
data = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")

features = ['anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','smoking']
target = 'age'
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_score = linear_model.score(X_test, y_test)

rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_score = rf_model.score(X_test, y_test)


print("Linear Regression R^2 Score:", linear_score)
print("Random Forest Regressor R^2 Score:", rf_score)