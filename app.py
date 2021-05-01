import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from lyrics_v1.model import LyricsGeneratorModel

model = LyricsGeneratorModel()
# print('\n'.join(model.predict('ขอ')))

st.title("NLP Project: Thai Song Generation")

st.header("First model")
st.subheader("Input")
text_input = st.text_input('Seed word')
st.subheader("Output")
st.write('\n'.join(model.predict(text_input)))
