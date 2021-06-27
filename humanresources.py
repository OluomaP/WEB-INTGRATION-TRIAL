import streamlit as st
import pandas as pd


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_Training = st.beta_container()

with header:
	st.title("Human Resources Project")

with dataset:
	st.header("Human Resources")
	st.text("The HR Team collected extensive data on their employees and are asked to develop a model that could predict which employees are more likely to quit")
	human_Resources = pd.read_csv("Human_Resources.csv")
	st.write(human_Resources.head(20))

with model_Training:
	st.header("Time to train the model")

	sel_col, dis_col = st.beta_columns(2)

input1 = sel_col.selectbox('How often did the Employee Travel for Business?',options=('Travel_Rarely', 'Travel_Frequently',"Non-Travel"))
input2 = sel_col.selectbox('Employee Department',options=('Research and Development', 'Human resources', 'Sales'))
input3 = sel_col.selectbox("Employee Gender", options=("Female","Male"))
input4 = sel_col.slider("Emplyee Job Level", min_value=1,max_value=3, value=2)
input5 = sel_col.text_input('Employee Daily Rate')

    
