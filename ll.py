import numpy as np
import pandas as pd
import streamlit as st

st.title("測驗 numpy/pandas")
a=np.array([89,71,69,77,63,85,92])
b=st.number_input("輸入成績:",key="nim_b")

if st.button:
    a=np.append(a,b)
    st.write(a)