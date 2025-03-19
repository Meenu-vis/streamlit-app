import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Chart in Streamlit")

# Generating random data
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['X', 'Y']
)

# Displaying the line chart
st.line_chart(data)
