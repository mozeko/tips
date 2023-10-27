#load libraries

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


st.set_page_config(page_title='Tips Dashboard', page_icon=None, layout="wide", initial_sidebar_state="expanded")
# load data
df = sns.load_dataset("tips")

#st.dataframe(df.sample(5))

#sidebar

st.sidebar.title("Tips Dashboard")
st.sidebar.title("ـــــــــــــــــــــــــــــــــــ")
st.sidebar.image("tips.jpg")
st.sidebar.write("This is Dashboard is using Tips dataset from seaborn for educational purposes.")
c_filtr = st.sidebar.selectbox("Categorical Filtring",[None,'sex','smoker','day','time'])
Num_filtr = st.sidebar.selectbox("Numrrical Filtring",[None,'total_bill','tip'])

row_filtr = st.sidebar.selectbox("Roew Filtring",[None,'sex','smoker','day','time'])
colu_filtr = st.sidebar.selectbox("Column Filtring",[None,'sex','smoker','day','time'])


st.sidebar.write("")
st.sidebar.markdown("Made with :muscle: by Analyst. [Zakaria Mostafa](https://www.linkedin.com/in/zakaria-mostafa/)")

# body

#row a
a1,a2,a3,a4 = st.columns(4)
a1.metric("Max.Total Bill",df['total_bill'].max())
a2.metric("Min.Total Bill",df['total_bill'].min())

a3.metric("Max.Tip",df['tip'].max())
a4.metric("Min.Tip",df['tip'].min())

#row b
st.subheader("Total Bill Vs.Tips")
fig = px.scatter(data_frame=df, x='total_bill', y = 'tip',color = c_filtr ,size = Num_filtr,
                 facet_row= row_filtr,facet_col= colu_filtr)
st.plotly_chart(fig,use_container_width=True)

# row c
c1,c2,c3 = st.columns((4,3,3))

with c1:
     st.text('Gender Vs. Total Bill')
     fig =px.bar(data_frame=df ,x='sex' , y='total_bill', color= c_filtr)
     st.plotly_chart(fig,use_container_width=True)
with c2:
     st.text('Smoker/NonSmoker Vs. Tips')
     fig =px.pie(data_frame=df ,names='smoker' , values='tip')
     st.plotly_chart(fig,use_container_width=True)

with c3:
    st.text('Day Vs. Tips')
    fig =px.pie(data_frame=df ,names='day' , values='tip',hole=0.3)
    st.plotly_chart(fig,use_container_width=True)


bt = st.button("Sample from Data")
if bt:
     st.dataframe(df.sample(5))
     df