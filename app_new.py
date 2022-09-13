
import streamlit as st
import pickle
import pandas as pd
from PIL import Image


st.sidebar.title('İnsurance Charge Prediction')
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Insurance Charge Prediction </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)


smoker=st.sidebar.selectbox("Do you smoke?:",(0,1))
bmi=st.sidebar.slider("What is your bmi?", 15, 54)
age=st.sidebar.slider("How old are you?", 18,64)

img = Image.open("ins.jpeg")
st.image(img, caption="insurance", width=700)

model=pickle.load(open("final_model_insurance.pkl","rb"))




my_dict = {
    "smoker": smoker,
    "bmi": bmi,
    "age": age}

df = pd.DataFrame.from_dict([my_dict])


if st.button("Predict"):
    prediction = model.predict(df)
    st.success("The estimated charge is €{}. ".format(int(prediction[0])))
    
