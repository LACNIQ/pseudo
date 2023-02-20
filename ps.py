# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 01:12:12 2023

@author: uth2001
"""

import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings('ignore')


st.title('Pseudo')
input1 = st.file_uploader("Upload input report")
output = st.file_uploader("Upload output file")
if input1 and output is not None:

    df = pd.read_excel(input1)
    df1 = pd.read_excel(output, sheet_name='Unique')
    condition = df1['FFU plus 1 day'].isna(
    ) & df1['REFERENCE CODE'].isin(df['REFERENCE CODE'])
    x = df['GIC'].loc[df['REFERENCE CODE'].isin(df1['REFERENCE CODE'])]
    y = df1['GIC']
    df1['GIC'] = np.where(condition, x, y)
    test = df1.astype(str)
    st.dataframe(test)
