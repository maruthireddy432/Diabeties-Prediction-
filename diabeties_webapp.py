import streamlit as st
import pickle
import numpy as np
#loading the model
loaded_model=pickle.load(open(r'D:\skill vertex\Major_project\trained_model.sav','rb'))
#prediction
def prediction(input_data):
    #changing data into numpy array
    input_data_numpy_array=np.asarray(input_data)
    #reshape the array 
    reshaped_array=input_data_numpy_array.reshape(1,-1)
    #prediction=classifier.predict(std_data)
    prediction=loaded_model.predict(reshaped_array)

    print(prediction)
    if prediction==0:
        return('The person non diabetic')
    else:
        return('The person is diabetic')
def main():
    #title
    st.title('Diabeties Prediction')
    # getting input from user
    
    pregnencies=st.text_input('Number of pregninces')
    glucose=st.text_input('Glucose Level')
    blood_pressure=st.text_input('Blood Presure level')
    skin_thickness=st.text_input('Skin Thickness level')
    insulin=st.text_input('Insuline level')
    bmi=st.text_input('BMI level')
    dp_function=st.text_input('Diabetes Pedigree Function value')
    age=st.text_input('Enter Age')

    # code for prediction
    diagonise=''

    #creating a button 
    if st.button('Diagonise'):
        diagonise=prediction([pregnencies,glucose,blood_pressure,skin_thickness,insulin,bmi,dp_function,age])
    st.success(diagonise)

if __name__=='__main__':
    main()
