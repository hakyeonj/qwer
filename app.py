import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep


st.set_page_config(page_icon="🍸", page_title="칵테일 한잔해~ 마싯자나~", layout="wide")

with st.spinner(text="칵테일 만드는중......") :
    sleep(3)

st.header("칵테일 페이지에 온걸 환영한다")
st.subheader("WELCOME TO HELL")

cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

cols[2].line_chart(chart_data)
