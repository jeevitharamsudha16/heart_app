# create virtual environment
# windows
# python -m venv venv
# venv\Scripts\activate
# install streamlit
# pip install streamlit
#pip install scikit-learn
# pip install seaborn
#pip install matplotlib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

# load the model
model = pickle.load(open('svc.pkl','rb'))

# Title for application
st.title('Heart Attack Risk Classification App❤️')

# Collect user inputs
Age = st.number_input('Age',min_value=18,max_value=90,value=30)
RestingBP = st.number_input('RestingBP',min_value=80,max_value=200,value=85)
Cholesterol =st.number_input('Cholesterol',min_value=80,max_value=650,value=100)
MaxHR = st.number_input('MaxHR',min_value=60,max_value=250,value=100)
Oldpeak = st.number_input('Oldpeak',min_value=-2.0,max_value=6.2,value=3.0)
Sex = st.selectbox('Gender',('male','female'))
ChestPainType = st.selectbox('ChestPainType',('ATA' ,'NAP' ,'ASY' ,'TA'))
RestingECG = st.selectbox('RestingECG',('Normal' ,'ST' ,'LVH'))
ExerciseAngina = st.selectbox('ExerciseAngina',('N','Y'))
ST_Slope = st.selectbox('ST_Slope',('Up', 'Flat' ,'Down'))
FastingBS = st.selectbox('Fasting Blood Sugar >120 mg/dL',(0,1))

# encoding logic for all categorical columns
# ExerciseAngina(Y,N)
Exercise_Angina = 1 if ExerciseAngina=='Y' else 0
# Sex
Sex_F = 1 if Sex=='female' else 0
Sex_M = 1 if Sex=='male' else 0

#  ChestPainType
ChestPainType_ASY	 = 1 if ChestPainType=='ASY' else 0
ChestPainType_ATA	 = 1 if ChestPainType=='ATA' else 0
ChestPainType_NAP = 1 if ChestPainType=='NAP' else 0
ChestPainType_TA = 1 if ChestPainType=='TA' else 0


# RestingECG
RestingECG_LVH	= 1 if RestingECG=='LVH' else 0
RestingECG_Normal = 1 if RestingECG=='Normal' else 0
RestingECG_ST = 1 if RestingECG=='ST' else 0

# ST_Slope
ST_Slope_Down = 1 if ST_Slope=='Down' else 0
ST_Slope_Flat	= 1 if ST_Slope=='Flat' else 0
ST_Slope_Up = 1 if ST_Slope=='Up' else 0

# create dataframe
data = pd.DataFrame({'Age':[Age],'RestingBP':[RestingBP],
          'Cholesterol':[Cholesterol],'FastingBS':[FastingBS],
        'MaxHR':[MaxHR],'Oldpeak':[Oldpeak],'Exercise_Angina':[Exercise_Angina],
         'Sex_F':[Sex_F],'Sex_M':[Sex_M],'ChestPainType_ASY':[ChestPainType_ASY],
                     'ChestPainType_ATA':[ChestPainType_ATA],	
 'ChestPainType_NAP':[ChestPainType_NAP], 'ChestPainType_TA':[ChestPainType_TA],	
 'RestingECG_LVH':[RestingECG_LVH],'RestingECG_Normal':[RestingECG_Normal],
                    'RestingECG_ST': [RestingECG_ST],
                     'ST_Slope_Down':[ST_Slope_Down],
                     'ST_Slope_Flat':[ST_Slope_Flat],
                     'ST_Slope_Up':[ST_Slope_Up]            
})
sc = StandardScaler()
data[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']]=sc.fit_transform(
    data[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']])

# predictions
if st.button('Predict'):
  predictions=model.predict(data)[0]
  if predictions==1:
    st.error('⚠️High Risk of Heart attack❗')
  else:
    st.error('Low Risk of Heart attack😎😊')