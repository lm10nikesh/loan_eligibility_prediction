import streamlit as st
import pickle
import pandas as pd 
import numpy as np 
from PIL import Image

#loading saved model
model_filename = 'model.pkl'
with open(model_filename, 'rb') as file:
	model = pickle.load(file)

st.title('Loan Eligiblity Prediction')
img1 = Image.open('loan1.png')
img1 = img1.resize((500,300))
st.image(img1,use_column_width=False)

#taking input from user 

name = st.text_input('Full Name')  
account_no = st.text_input('Account number')

left,right = st.columns((2,2))
Gender = left.selectbox('Gender', ('Male', 'Female'))
Married = right.selectbox('Married', ('Yes', 'No'))
Dependents = left.selectbox('Dependents', ('None', 'One', 'Two', 'More Than Three'))
Education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
Self_Employed = left.selectbox('Self-Employed', ('Yes', 'No'))
ApplicantIncome = right.number_input('Applicant Monthly Income')
CoapplicantIncome = left.number_input('Coapplicant Monthly Income')
LoanAmount = right.slider('Loan Amount(per 1000)',0,700000)
Loan_Amount_Term = left.selectbox('Loan Tenure (in months)',[12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,342.0,360.0,480.0])
Credit_History = right.selectbox('Credit History',("Unclear Debts", "Cleared Debts"))
Property_Area = st.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))

# processing user input
gen = 1 if Gender == 'Male' else 0
mar = 1 if Married == 'Yes' else 0
dep = float(0 if Dependents == 'None' else 1 if Dependents == 'One' else 2 if Dependents == 'Two' else 4)
edu = 1 if Education == 'Graduate' else 0
sem = 1 if Self_Employed == 'Yes' else 0
pro = 0 if Property_Area == 'Urban' else 1 if Property_Area == 'Rural' else 2
ch = 0 if Credit_History == 'Unclear Debts' else 1
Lam = LoanAmount/1000 

if st.button('Predict'):
    data = {'Gender':[gen],
		    'Married':[mar],
		    'Dependents':[dep],
		    'Education':[edu],
		    "Self_Employed":[sem],
		    "ApplicantIncome":[ApplicantIncome],
		    'CoapplicantIncome':[CoapplicantIncome],
		    'LoanAmount':[Lam],
		    'Loan_Amount_Term':[Loan_Amount_Term],
		    'Credit_History':[ch],
		    'Property_Area':[pro]}
    
    df1 = pd.DataFrame(data)
    df1
    prediction = model.predict(df1)
    
    if prediction == 0:
        st.error("Hello: " + name +" , " + "Account number: "+account_no +' , '
                'We are sorry to inform that you will not get the loan from Bank.')
    else:
        st.success("Hello: " + name +" , " + "Account number: "+account_no +' , '
                'Congratulations!!! you will get the loan from Bank.')

st.sidebar.subheader("About App")
st.sidebar.info("This web app helps you to find out whether you are eligible for Loan from the bank or not.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you are eligible for the Loan or not")

 