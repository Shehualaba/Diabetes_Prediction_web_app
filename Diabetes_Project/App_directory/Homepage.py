import streamlit as st

st.title("Diabetes Prediction Project")
st.markdown('''This projects involves using the CDC diabetes data to create a machine learning model that can
predict if some has diabetes or not based on the values entered. 
### About the data
The Diabetes Health Indicators Dataset contains healthcare statistics and lifestyle survey information about people in general along with their diagnosis of diabetes. The 21 features consist of some demographics, lab test results, and answers to survey questions for each patient. The target variable for classification is whether a patient has diabetes, is pre-diabetic, or healthy.
''')
st.header("PROJECT WORKFLOW")
st.markdown('''
##### **1. Data Collection**  
The data was gotten from UCI Machine learning repository
[Data_source](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators)
#### **2.Data Cleaning and Exploratory Data Analysis**  
The data was cleaned and exploratory data analysis was done on the data, so that we can understand the data
structure of the data
#### **3.Data Preprocessing**  
* IsolationForest : Due to how highly imbalanced the data was, I used IsolationForest to detect the outliers
and anomaly in the dataset and they were removed
* I turned the categorical values into numerical
* I used StandardScalar to scale the categorical variables

#### **4. Model Building**  
The main model was built using XGBClassifier
#### **5. Hyperparameter Tuning**  
#### **6. Model Evaluation**  
#### **Model Deployment**

**For full details about how the model was created click the link below**  
[Project on GitHub](https://github.com/Shehualaba/Diabetes_prediction)

To access predictor click the Diabetes predictor tab on the sidebar
''')